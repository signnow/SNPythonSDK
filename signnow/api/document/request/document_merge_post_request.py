"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Dict, List, Union

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="mergeDocuments",
    url="/document/merge",
    method="post",
    auth="bearer",
    namespace="document",
    entity="documentMerge",
    content_type="application/json",
)
class DocumentMergePostRequest(RequestInterface):
    """
    This class represents a request to merge documents.
    """

    def __init__(
        self,
        name: str,
        document_ids: Union[List[str], Dict[str, List[str]]],
        upload_document: bool = False,
    ):
        """
        Constructs a new DocumentMergePostRequest.

        Args:
            name: The name of the merged document
            document_ids: List of document IDs to be merged, or dict with "document_ids" key
            upload_document: Flag indicating whether the document should be uploaded (default: False)
        """
        self._name = name
        # Handle both list and dict formats
        if isinstance(document_ids, list):
            self._document_ids = document_ids
        elif isinstance(document_ids, dict) and "document_ids" in document_ids:
            self._document_ids = document_ids["document_ids"]
        else:
            raise TypeError(
                f"document_ids must be a list of strings or a dict with "
                f"'document_ids' key, got {type(document_ids).__name__}"
            )
        self._upload_document = upload_document

    def uri_params(self) -> Dict[str, str]:
        """Returns an empty dict as there are no URI parameters."""
        return {}

    def payload(self) -> Dict[str, Union[str, List[str], bool]]:
        """
        Returns a map with the payload of the request.

        Returns:
            A dict with the payload of the request
        """
        return {
            "name": self._name,
            "document_ids": self._document_ids,
            "upload_document": self._upload_document,
        }
