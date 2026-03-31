"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

import importlib
import json
import os
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Generic, Optional, Type, TypeVar

from signnow.core.exception import SignNowApiException
from signnow.core.request import ApiEndpoint

T = TypeVar("T")

# Cache for dynamically resolved response classes to avoid repeated imports.
_response_class_cache: Dict[str, Type[Any]] = {}


@dataclass
class ResponseData:
    """
    Represents the response data of an HTTP request, including the status code, content type,
    response body, and an optional download directory.
    """

    code: int
    content_type: str
    content_disposition: str
    download_directory: str
    content: bytes = b""
    file_path: Optional[str] = None

    def get_content_as_string(self) -> str:
        """Returns the content as a string."""
        try:
            return self.content.decode("utf-8")
        except UnicodeDecodeError:
            return ""

    def has_file(self) -> bool:
        """Checks if the response contains a file."""
        return (
            "attachment" in self.content_disposition.lower()
            or "download" in self.content_disposition.lower()
        )


@dataclass
class Reply(Generic[T]):
    """
    This class represents a server reply.

    Args:
        http_status_code: The HTTP status code of the server response
        json: The raw JSON string of the server response
        response: The deserialized response body
    """

    http_status_code: int
    json: str
    response: T

    def get_status_code(self) -> int:
        """Returns the HTTP status code of the server response."""
        return self.http_status_code

    def is_ok(self) -> bool:
        """Checks if the server response was successful."""
        return 200 <= self.http_status_code < 300

    def is_empty(self) -> bool:
        """Checks if the server response has no body."""
        if self.response is None:
            return True
        # Check if response is an empty dict or has no attributes
        if isinstance(self.response, dict):
            return len(self.response) == 0
        # Check if response is an empty class (no attributes or only default values)
        if hasattr(self.response, "__dict__"):
            # Check if all attributes are empty/default
            attrs = vars(self.response)
            if not attrs:
                return True
            # Check if all values are empty/default
            for value in attrs.values():
                if value not in (None, "", [], {}, 0, False):
                    return False
            return True
        return False

    def to_json(self) -> str:
        """Returns the raw JSON string of the server response."""
        return self.json

    def get_response(self) -> T:
        """Returns the deserialized response body."""
        return self.response


class ResponseParser:
    """This class parses signNow API response JSON and deserializes it into a data object."""

    @staticmethod
    def capitalize_first_letter(text: str) -> str:
        """Capitalizes the first letter of the input string."""
        if not text:
            return text
        if len(text) > 1:
            return text[0].upper() + text[1:]
        return text.upper()

    @staticmethod
    def parse(response_data: ResponseData, api_endpoint: ApiEndpoint) -> Reply[Any]:
        """
        Parses the response from the signNow API and deserializes it into a data object.

        Args:
            response_data: The downloading response data object
            api_endpoint: The endpoint of the API that was called

        Returns:
            A Reply object containing the status code, JSON response, and deserialized data

        Raises:
            SignNowApiException: If there is an error during deserialization or if the response
                class for mapping is not found
        """
        entity = ResponseParser.capitalize_first_letter(api_endpoint.entity)
        method = ResponseParser.capitalize_first_letter(api_endpoint.method.lower())
        namespace = api_endpoint.namespace.lower()

        class_name = f"signnow.api.{namespace}.response.{entity}{method}Response"

        try:
            if namespace == "proxy":
                if "download" in api_endpoint.url and response_data.has_file():
                    class_name = "signnow.api.proxy.response.ProxyFileResponse"
                else:
                    class_name = "signnow.api.proxy.response.ProxyJsonResponse"

            # Dynamic import with caching
            if class_name in _response_class_cache:
                map_class = _response_class_cache[class_name]
            else:
                module_parts = class_name.split(".")
                module_name = ".".join(module_parts[:-1])
                class_name_only = module_parts[-1]

                module = importlib.import_module(module_name)
                map_class = getattr(module, class_name_only)
                _response_class_cache[class_name] = map_class

            # Check if this is a file download response
            if (
                "download" in api_endpoint.url
                and response_data.has_file()
                or api_endpoint.type in ["application/pdf", "application/zip"]
            ):
                return ResponseParser.parse_file(map_class, response_data, api_endpoint)
            return ResponseParser.parse_json(map_class, response_data, api_endpoint)
        except (ImportError, AttributeError) as e:
            raise SignNowApiException(
                f"Response class {class_name} not found for mapping.",
                api_endpoint.method.upper() + " " + api_endpoint.url,
                None,
                response_data.get_content_as_string(),
                response_data.code,
                e,
            )

    @staticmethod
    def parse_file(
        response_class: Type[Any],
        response_data: ResponseData,
        api_endpoint: ApiEndpoint,
    ) -> Reply[Any]:
        """
        Parses a file response and saves it to disk.

        Args:
            response_class: The response class to instantiate
            response_data: The response data containing the file
            api_endpoint: The API endpoint information

        Returns:
            A Reply object containing the file path

        Raises:
            SignNowApiException: If there is an error saving the file
        """
        try:
            # If the file was already streamed to disk by ApiClient, reuse that path.
            if response_data.file_path:
                file_path = Path(response_data.file_path)
            else:
                # Fallback: write content bytes to disk (non-streamed path)
                filename = ResponseParser.extract_filename(
                    response_data.content_disposition
                )
                if not filename:
                    filename = f"download_{uuid.uuid4().hex[:8]}"

                download_dir = Path(response_data.download_directory)
                download_dir.mkdir(parents=True, exist_ok=True)

                file_path = download_dir / filename

                with open(file_path, "wb") as f:
                    f.write(response_data.content)

            # Create response object with file path
            # Check if response_class expects file_path parameter
            if hasattr(response_class, "__dataclass_fields__"):
                if "file_path" in response_class.__dataclass_fields__:
                    response = response_class(file_path=str(file_path))
                else:
                    # Fallback for classes that might use different parameter names
                    response = response_class(str(file_path))
            else:
                # For non-dataclass responses, try to instantiate with file_path
                try:
                    response = response_class(file_path=str(file_path))
                except TypeError:
                    response = response_class(str(file_path))

            return Reply(
                http_status_code=response_data.code,
                json="",
                response=response,
            )
        except Exception as e:
            raise SignNowApiException(
                "Error on saving the downloaded file.",
                api_endpoint.method.upper() + " " + api_endpoint.url,
                None,
                None,
                response_data.code,
                e,
            )

    @staticmethod
    def extract_filename(content_disposition: str) -> Optional[str]:
        """Extracts filename from Content-Disposition header."""
        if not content_disposition:
            return None

        # Try to extract filename from Content-Disposition header
        # Format: attachment; filename="document.pdf"
        if "filename=" in content_disposition:
            parts = content_disposition.split("filename=", 1)
            if len(parts) > 1:
                filename = parts[1].strip().strip('"').strip("'")
                # Sanitize to prevent path traversal
                filename = os.path.basename(filename)
                if not filename or filename.startswith("."):
                    return None
                return filename
        return None

    @staticmethod
    def parse_json(
        response_class: Type[Any],
        response_data: ResponseData,
        api_endpoint: ApiEndpoint,
    ) -> Reply[Any]:
        """
        Parses a JSON response and deserializes it into a data object.

        Args:
            response_class: The response class to deserialize into
            response_data: The response data containing the JSON
            api_endpoint: The API endpoint information

        Returns:
            A Reply object containing the deserialized response

        Raises:
            SignNowApiException: If there is an error during deserialization
        """
        json_response = response_data.get_content_as_string()
        if not json_response or not json_response.strip():
            json_response = "{}"

        try:
            data = json.loads(json_response)
            # Special handling for ProxyJsonResponse - it takes the entire JSON as raw_json
            if response_class.__name__ == "ProxyJsonResponse":
                response = response_class(raw_json=data)
            # If response_class is a dataclass, instantiate it
            elif hasattr(response_class, "__dataclass_fields__"):
                # Filter data to only include fields that exist in the dataclass
                # and handle default values
                field_names = {
                    field.name for field in response_class.__dataclass_fields__.values()
                }
                filtered_data = {}
                for k, v in data.items():
                    if k in field_names:
                        filtered_data[k] = v
                response = response_class(**filtered_data)
            elif isinstance(data, dict):
                # Try to instantiate with **data
                response = response_class(**data)
            else:
                response = response_class(data)

            return Reply(
                http_status_code=response_data.code,
                json=json_response,
                response=response,
            )
        except (json.JSONDecodeError, TypeError, ValueError) as e:
            raise SignNowApiException(
                f"Failed to deserialize the response JSON to class {response_class.__name__} instance.",
                api_endpoint.method.upper() + " " + api_endpoint.url,
                None,
                json_response,
                response_data.code,
                e,
            )
