"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from pathlib import Path
from typing import Dict, Optional, Union

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="uploadDocument",
    url="/document",
    method="post",
    auth="bearer",
    namespace="document",
    entity="document",
    content_type="multipart/form-data",
)
class DocumentPostRequest(RequestInterface):
    """
    Represents a request to upload a document to the server.
    This class is used to build the request payload and parameters.
    """

    def __init__(
        self,
        file: Union[str, Path],
        name: Optional[str] = None,
        check_fields: bool = False,
        save_fields: int = 0,
        make_template: int = 0,
        password: Optional[str] = None,
        folder_id: Optional[str] = None,
        origin_template_id: Optional[str] = None,
        client_timestamp: int = 0,
    ):
        """
        Constructs a new DocumentPostRequest.

        Args:
            file: The file to be uploaded (path as string or Path object)
            name: The name of the file (optional)
            check_fields: Flag to check fields (default: False)
            save_fields: Flag to save fields (default: 0)
            make_template: Flag to make template (default: 0)
            password: The password for the document (optional)
            folder_id: The ID of the folder where the document will be stored (optional)
            origin_template_id: The ID of the original template (optional)
            client_timestamp: The client timestamp (default: 0)
        """
        self._file = Path(file) if isinstance(file, str) else file
        self._name = name
        self._check_fields = check_fields
        self._save_fields = save_fields
        self._make_template = make_template
        self._password = password
        self._folder_id = folder_id
        self._origin_template_id = origin_template_id
        self._client_timestamp = client_timestamp

    def uri_params(self) -> Dict[str, str]:
        """Returns an empty dict as there are no URI parameters."""
        return {}

    def payload(self) -> Dict[str, Union[str, Path, bool, int]]:
        """
        Returns a dict with the payload of the request.

        Returns:
            A dict with the payload of the request
        """
        payload: Dict[str, Union[str, Path, bool, int]] = {
            "file": self._file,
        }

        if self._name:
            payload["name"] = self._name
        if self._check_fields:
            payload["check_fields"] = str(self._check_fields).lower()
        if self._save_fields:
            payload["save_fields"] = str(self._save_fields)
        if self._make_template:
            payload["make_template"] = str(self._make_template)
        if self._password:
            payload["password"] = self._password
        if self._folder_id:
            payload["folder_id"] = self._folder_id
        if self._origin_template_id:
            payload["origin_template_id"] = self._origin_template_id
        if self._client_timestamp:
            payload["client_timestamp"] = str(self._client_timestamp)

        return payload
