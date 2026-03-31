"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Any, Dict, Optional

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="createDocumentEmbeddedSendingLink",
    url="/v2/documents/{document_id}/embedded-sending",
    method="post",
    auth="bearer",
    namespace="embeddedSending",
    entity="documentEmbeddedSendingLink",
    content_type="application/json",
)
class DocumentEmbeddedSendingLinkPostRequest(RequestInterface):
    """
    Represents a request to create a document embedded sending link.
    """

    def __init__(
        self,
        type: str,
        redirect_uri: Optional[str] = None,
        link_expiration: Optional[int] = None,
        redirect_target: Optional[str] = None,
    ):
        """
        Constructs a new DocumentEmbeddedSendingLinkPostRequest.

        Args:
            type: The type of the request (e.g., "manage", "edit", "send-invite").
            redirect_uri: The redirect URI of the request. Optional.
            link_expiration: The link expiration time of the request. Optional.
            redirect_target: The redirect target of the request. Optional.
        """
        self.type = type
        self.redirect_uri = redirect_uri
        self.link_expiration = link_expiration
        self.redirect_target = redirect_target
        self._uri_params: Dict[str, str] = {}

    def with_document_id(
        self, document_id: str
    ) -> "DocumentEmbeddedSendingLinkPostRequest":
        """
        Adds the document ID to the URI parameters.

        Args:
            document_id: The document ID to be added.

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
            A dictionary containing type, redirect_uri, link_expiration, and redirect_target.
        """
        payload: Dict[str, Any] = {
            "type": self.type,
        }
        if self.redirect_uri is not None:
            payload["redirect_uri"] = self.redirect_uri
        if self.link_expiration is not None:
            payload["link_expiration"] = self.link_expiration
        if self.redirect_target is not None:
            payload["redirect_target"] = self.redirect_target
        return payload
