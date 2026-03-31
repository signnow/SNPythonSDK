"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Dict

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="getFolderDocuments",
    url="/folder/{folder_id}",
    method="get",
    auth="bearer",
    namespace="folder",
    entity="folderDocuments",
    content_type="application/json",
)
class FolderDocumentsGetRequest(RequestInterface):
    """
    Represents a request to get documents from a folder.
    """

    def __init__(self):
        """Constructs a new FolderDocumentsGetRequest."""
        self._uri_params: Dict[str, str] = {}

    def with_folder_id(self, folder_id: str) -> "FolderDocumentsGetRequest":
        """
        Adds a folder ID to the URI parameters.

        Args:
            folder_id: The ID of the folder.

        Returns:
            The current FolderDocumentsGetRequest instance.
        """
        self._uri_params["folder_id"] = folder_id
        return self

    def uri_params(self) -> Dict[str, str]:
        """
        Returns a copy of the URI parameters.

        Returns:
            A dictionary containing the URI parameters.
        """
        return dict(self._uri_params)

    def payload(self) -> Dict[str, str]:
        """
        Returns an empty dictionary for the payload.

        Returns:
            An empty dictionary.
        """
        return {}
