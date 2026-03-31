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
    name="bulkInvite",
    url="/template/{document_id}/bulkinvite",
    method="post",
    auth="bearer",
    namespace="template",
    entity="bulkInvite",
    content_type="multipart/form-data",
)
class BulkInvitePostRequest(RequestInterface):
    """
    Represents a bulk invite post request.
    This class is used to send a bulk invite request to the API.
    """

    def __init__(
        self,
        file: Union[str, Path],
        folder_id: Optional[str] = None,
        client_timestamp: Optional[int] = None,
        document_name: Optional[str] = None,
        subject: Optional[str] = None,
        email_message: Optional[str] = None,
    ):
        """
        Constructs a new BulkInvitePostRequest.

        Args:
            file: The file to be sent in the request.
            folder_id: The ID of the folder where the document is located. Optional.
            client_timestamp: The client timestamp when the request is made. Optional.
            document_name: The name of the document. Optional.
            subject: The subject of the email. Optional.
            email_message: The message of the email. Optional.
        """
        self.file = Path(file) if isinstance(file, str) else file
        self.folder_id = folder_id
        self.client_timestamp = client_timestamp
        self.document_name = document_name
        self.subject = subject
        self.email_message = email_message
        self._uri_params: Dict[str, str] = {}

    def with_document_id(self, document_id: str) -> "BulkInvitePostRequest":
        """
        Adds the document ID to the URI parameters.

        Args:
            document_id: The ID of the document.

        Returns:
            This BulkInvitePostRequest instance.
        """
        self._uri_params["document_id"] = document_id
        return self

    def uri_params(self) -> Dict[str, str]:
        """
        Returns a copy of the URI parameters.

        Returns:
            A dictionary containing the URI parameters.
        """
        return dict(self._uri_params)

    def payload(self) -> Dict[str, Union[Path, Optional[str], Optional[int]]]:
        """
        Returns a dictionary containing the payload for the request.

        Returns:
            A dictionary containing the payload.
        """
        payload: Dict[str, Union[Path, Optional[str], Optional[int]]] = {
            "file": self.file,
        }
        if self.folder_id is not None:
            payload["folder_id"] = self.folder_id
        if self.client_timestamp is not None:
            payload["client_timestamp"] = self.client_timestamp
        if self.document_name is not None:
            payload["document_name"] = self.document_name
        if self.subject is not None:
            payload["subject"] = self.subject
        if self.email_message is not None:
            payload["email_message"] = self.email_message
        return payload
