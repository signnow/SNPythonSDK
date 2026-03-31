"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

import json
import mimetypes
import os
import uuid
from pathlib import Path
from typing import Any, Dict, Optional
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

import httpx

from signnow.core.config import ConfigRepository
from signnow.core.exception import SignNowApiException
from signnow.core.request import ApiEndpoint, ApiEndpointResolver, RequestInterface
from signnow.core.response import Reply, ResponseData, ResponseParser
from signnow.core.token import BasicToken, BearerToken


class ApiClient:
    """This class is responsible for sending API requests to the signNow server."""

    def __init__(
        self,
        client: httpx.Client,
        api_endpoint_resolver: ApiEndpointResolver,
        config_repository: ConfigRepository,
        basic_token: BasicToken,
        bearer_token: Optional[BearerToken] = None,
    ):
        """
        Constructs an ApiClient with the provided parameters.

        Args:
            client: The HTTP client to send API requests
            api_endpoint_resolver: The resolver to retrieve the ApiEndpoint data object from request object
            config_repository: The signNow SDK configuration
            basic_token: The Authorization Basic token to retrieve Bearer token
            bearer_token: The Authorization Bearer token for API requests
        """
        self._client = client
        self._api_endpoint_resolver = api_endpoint_resolver
        self._config_repository = config_repository
        self._basic_token = basic_token
        self._bearer_token = bearer_token

    def send(self, request: RequestInterface) -> Reply[Any]:
        """
        Sends a request to the signNow server.

        Args:
            request: The request to be sent

        Returns:
            The response from the server

        Raises:
            SignNowApiException: If there is an error processing the request
        """
        api_endpoint = self._api_endpoint_resolver.resolve(request)
        url = self._build_url(api_endpoint, request)
        headers = self._build_headers(api_endpoint)
        body = self._build_body(api_endpoint, request)

        response_code = 0
        json_content = "{}"

        try:
            # Handle multipart/form-data separately
            if api_endpoint.type == "multipart/form-data" and body is None:
                # Build multipart form data
                files = {}
                file_handles = []
                form_data = {}
                payload = request.payload()

                for key, value in payload.items():
                    if value is None:
                        continue
                    if isinstance(value, (str, Path)):
                        path = Path(value)
                        if path.exists() and path.is_file():
                            handle = open(path, "rb")
                            file_handles.append(handle)
                            files[key] = (
                                path.name,
                                handle,
                                self._get_mime_type(path),
                            )
                        else:
                            form_data[key] = str(value)
                    elif hasattr(value, "read"):  # File-like object
                        files[key] = value
                    else:
                        form_data[key] = str(value)

                # Remove Content-Type header for multipart (httpx sets it automatically)
                multipart_headers = {
                    k: v for k, v in headers.items() if k != "Content-Type"
                }

                try:
                    if files:
                        response = self._client.request(
                            method=api_endpoint.method.upper(),
                            url=url,
                            headers=multipart_headers,
                            files=files,
                            data=form_data if form_data else None,
                            timeout=self._config_repository.read_timeout(),
                        )
                    else:
                        response = self._client.request(
                            method=api_endpoint.method.upper(),
                            url=url,
                            headers=multipart_headers,
                            data=form_data,
                            timeout=self._config_repository.read_timeout(),
                        )
                finally:
                    for handle in file_handles:
                        handle.close()
            else:
                # Use streaming for file download endpoints
                if self._is_file_download(api_endpoint):
                    return self._stream_download(api_endpoint, url, headers, body)

                response = self._client.request(
                    method=api_endpoint.method.upper(),
                    url=url,
                    headers=headers,
                    content=body,
                    timeout=self._config_repository.read_timeout(),
                )

            response_code = response.status_code
            json_content = response.text if response.text else "{}"

            self._validate_response(
                response_code,
                endpoint=api_endpoint.method.upper() + " " + api_endpoint.url,
                payload=self._get_payload(body),
                response_body=json_content,
            )

            response_data = ResponseData(
                code=response_code,
                content_type=response.headers.get("Content-Type", ""),
                content_disposition=response.headers.get("Content-Disposition", ""),
                download_directory=self._config_repository.downloads_directory(),
                content=response.content,
            )

            return ResponseParser.parse(response_data, api_endpoint)
        except httpx.HTTPError as e:
            raise SignNowApiException(
                "Failed processing signNow API request.",
                api_endpoint.method.upper() + " " + api_endpoint.url,
                self._get_payload(body),
                json_content,
                response_code,
                e,
            )

    def set_bearer_token(self, token: BearerToken) -> None:
        """Sets the Bearer token for API requests."""
        self._bearer_token = token

    def get_bearer_token(self) -> Optional[BearerToken]:
        """Retrieves the Bearer token for API requests."""
        return self._bearer_token

    def _build_url(self, endpoint: ApiEndpoint, request: RequestInterface) -> str:
        """Builds the full URL for the request."""
        host = self._config_repository.host()
        uri = endpoint.url
        uri_params = request.uri_params()

        # Replace URI parameters
        for param, value in uri_params.items():
            uri = uri.replace(f"{{{param}}}", value)

        # Build base URL
        url = host + uri

        # Add query parameters if they exist
        query_params = getattr(request, "query_params", None)
        if query_params and callable(query_params):
            try:
                params = query_params()
                if params:
                    parsed = urlparse(url)
                    query_dict = dict(parse_qsl(parsed.query))
                    query_dict.update(params)
                    query_string = urlencode(query_dict)
                    parsed = parsed._replace(query=query_string)
                    url = urlunparse(parsed)
            except Exception:
                pass  # Ignore errors with query_params

        return url

    def _build_headers(self, endpoint: ApiEndpoint) -> Dict[str, str]:
        """Builds the headers for the request."""
        headers = {
            "Accept": "application/json",
            "Content-Type": endpoint.type,
            "User-Agent": self._config_repository.client_name(),
        }

        # Add authorization header
        auth_header = self._build_auth_header(endpoint)
        if auth_header:
            headers["Authorization"] = auth_header

        return headers

    def _build_auth_header(self, endpoint: ApiEndpoint) -> str:
        """Builds the authorization header."""
        if endpoint.auth == "basic":
            return f"Basic {self._basic_token.token()}"
        elif endpoint.auth == "bearer":
            if not self._bearer_token:
                raise SignNowApiException(
                    f"Bearer token is required for endpoint: {endpoint.url}",
                    endpoint.method.upper() + " " + endpoint.url,
                )
            return f"Bearer {self._bearer_token.token()}"
        else:
            raise SignNowApiException(
                f"Unknown request authentication type: {endpoint.auth}",
                endpoint.method.upper() + " " + endpoint.url,
            )

    def _build_body(
        self, endpoint: ApiEndpoint, request: RequestInterface
    ) -> Optional[bytes]:
        """Builds the request body."""
        if endpoint.method.upper() not in ["POST", "PUT", "PATCH"]:
            return None

        payload = request.payload()

        if endpoint.type == "application/json":
            # Remove None values from payload
            clean_payload = {k: v for k, v in payload.items() if v is not None}
            return json.dumps(clean_payload).encode("utf-8")

        elif endpoint.type == "application/x-www-form-urlencoded":
            form_data = urlencode(payload)
            return form_data.encode("utf-8")

        elif endpoint.type == "multipart/form-data":
            # Multipart is handled in the send method
            return None

        return None

    def _validate_response(
        self,
        code: int,
        endpoint: Optional[str] = None,
        payload: Optional[str] = None,
        response_body: Optional[str] = None,
    ) -> None:
        """Validates the response code."""
        if 400 <= code < 500:
            raise SignNowApiException(
                "SignNow API request was invalid.",
                endpoint=endpoint,
                payload=payload,
                response=response_body,
                response_code=code,
            )
        if code >= 500:
            raise SignNowApiException(
                "SignNow API request has failed due to server error.",
                endpoint=endpoint,
                payload=payload,
                response=response_body,
                response_code=code,
            )

    def _get_payload(self, body: Optional[bytes]) -> Optional[str]:
        """Gets the payload as a string for error messages."""
        if body:
            try:
                return body.decode("utf-8")
            except UnicodeDecodeError:
                return "<binary data>"
        return None

    def _get_mime_type(self, file_path: Path) -> str:
        """Gets the MIME type of a file."""
        mime_type, _ = mimetypes.guess_type(str(file_path))
        return mime_type or "application/octet-stream"

    @staticmethod
    def _is_file_download(api_endpoint: ApiEndpoint) -> bool:
        """Checks whether the endpoint is expected to return a binary file."""
        if api_endpoint.type in ("application/pdf", "application/zip"):
            return True
        # Match endpoints whose URL ends with a download segment (e.g.
        # /download, /downloadall) but not those that merely contain "download"
        # as part of a longer path like /download/link which returns JSON.
        url = api_endpoint.url.rstrip("/")
        last_segment = url.rsplit("/", 1)[-1]
        if last_segment in ("download", "downloadall"):
            return True
        return False

    def _stream_download(
        self,
        api_endpoint: ApiEndpoint,
        url: str,
        headers: Dict[str, str],
        body: Optional[bytes],
    ) -> Reply[Any]:
        """
        Streams the response body to disk in chunks so that the full file is
        never buffered in memory.
        """
        download_dir = Path(self._config_repository.downloads_directory())
        download_dir.mkdir(parents=True, exist_ok=True)

        # Temporary name until we know the real filename from headers.
        tmp_path = download_dir / f".tmp_download_{uuid.uuid4().hex[:8]}"

        try:
            with self._client.stream(
                method=api_endpoint.method.upper(),
                url=url,
                headers=headers,
                content=body,
                timeout=self._config_repository.read_timeout(),
            ) as response:
                response_code = response.status_code
                self._validate_response(
                    response_code,
                    endpoint=api_endpoint.method.upper() + " " + api_endpoint.url,
                    payload=self._get_payload(body),
                )

                content_disposition = response.headers.get("Content-Disposition", "")

                # Stream chunks to disk (default 8 KiB)
                with open(tmp_path, "wb") as f:
                    for chunk in response.iter_bytes(chunk_size=8192):
                        f.write(chunk)

            # Determine the final filename
            from signnow.core.response import ResponseParser

            filename = ResponseParser.extract_filename(content_disposition)
            if not filename:
                filename = f"download_{uuid.uuid4().hex[:8]}"

            final_path = download_dir / filename
            os.replace(tmp_path, final_path)

            response_data = ResponseData(
                code=response_code,
                content_type=response.headers.get("Content-Type", ""),
                content_disposition=content_disposition,
                download_directory=str(download_dir),
                file_path=str(final_path),
            )

            return ResponseParser.parse(response_data, api_endpoint)

        except httpx.HTTPError as e:
            # Clean up partial download
            if tmp_path.exists():
                tmp_path.unlink()
            raise SignNowApiException(
                "Failed processing signNow API request.",
                api_endpoint.method.upper() + " " + api_endpoint.url,
                self._get_payload(body),
                "{}",
                0,
                e,
            )
        except Exception:
            if tmp_path.exists():
                tmp_path.unlink()
            raise
