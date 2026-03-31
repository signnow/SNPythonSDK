"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

import json
from pathlib import Path
from typing import Dict, List, Optional, Union

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="uploadDocumentWithTagsExtract",
    url="/document/fieldextract",
    method="post",
    auth="bearer",
    namespace="document",
    entity="fieldExtract",
    content_type="multipart/form-data",
)
class FieldExtractPostRequest(RequestInterface):
    """
    Represents a request to extract fields from a document.
    This request is sent as a POST request to the /document/fieldextract endpoint.
    """

    def __init__(
        self,
        file: Union[str, Path],
        tags: Union[List[Dict], Dict, str],
        parse_type: Optional[str] = None,
        password: Optional[str] = None,
        client_timestamp: int = 0,
    ):
        """
        Constructs a new FieldExtractPostRequest.

        Args:
            file: The file to be processed (path as string or Path object)
            tags: The collection of tags to be extracted (list of dicts, dict, or JSON string)
            parse_type: The type of parsing to be performed on the document (optional)
            password: The password for the document, if it is password-protected (optional)
            client_timestamp: The timestamp from the client (default: 0)
        """
        self._file = Path(file) if isinstance(file, str) else file
        # Convert tags to JSON string if needed
        if isinstance(tags, str):
            self._tags_json = tags
        elif isinstance(tags, (list, dict)):
            self._tags_json = json.dumps(tags)
        else:
            self._tags_json = json.dumps([])
        self._parse_type = parse_type
        self._password = password
        self._client_timestamp = client_timestamp

    def uri_params(self) -> Dict[str, str]:
        """Returns an empty dict as there are no URI parameters."""
        return {}

    def payload(self) -> Dict[str, Union[str, Path, int]]:
        """
        Returns a dict containing the payload for the request.

        Returns:
            A dict containing the payload for the request
        """
        payload: Dict[str, Union[str, Path, int]] = {
            "file": self._file,
            "Tags": self._tags_json,
        }

        if self._parse_type:
            payload["parse_type"] = self._parse_type
        if self._password:
            payload["password"] = self._password
        if self._client_timestamp:
            payload["client_timestamp"] = str(self._client_timestamp)

        return payload
