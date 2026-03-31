"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Any, Dict, Optional

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="createDocumentEmbeddedEditorLink",
    url="/v2/documents/{document_id}/embedded-editor",
    method="post",
    auth="bearer",
    namespace="embeddedEditor",
    entity="documentEmbeddedEditorLink",
    content_type="application/json",
)
class DocumentEmbeddedEditorLinkPostRequest(RequestInterface):
    """
    Represents a request to create a document embedded editor link.
    """

    def __init__(
        self,
        redirect_uri: Optional[str] = None,
        redirect_target: Optional[str] = None,
        link_expiration: Optional[int] = None,
    ):
        """
        Constructs a new DocumentEmbeddedEditorLinkPostRequest.

        Args:
            redirect_uri: Link that opens after the user has completed editing the document. Optional.
            redirect_target: Determines on what browser's tab should be opened the redirectUri. Optional.
            link_expiration: The link expiration time in minutes. Optional.
        """
        self.redirect_uri = redirect_uri
        self.redirect_target = redirect_target
        self.link_expiration = link_expiration
        self._uri_params: Dict[str, str] = {}

    def with_document_id(
        self, document_id: str
    ) -> "DocumentEmbeddedEditorLinkPostRequest":
        """
        Adds the document ID to the URI parameters.

        Args:
            document_id: The document ID to add.

        Returns:
            The current instance with the updated URI parameters.
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

    def payload(self) -> Dict[str, Any]:
        """
        Returns a dictionary with the payload of the request.

        Returns:
            A dictionary containing redirect_uri, redirect_target, and link_expiration.
        """
        payload: Dict[str, Any] = {}
        if self.redirect_uri is not None:
            payload["redirect_uri"] = self.redirect_uri
        if self.redirect_target is not None:
            payload["redirect_target"] = self.redirect_target
        if self.link_expiration is not None:
            payload["link_expiration"] = self.link_expiration
        return payload
