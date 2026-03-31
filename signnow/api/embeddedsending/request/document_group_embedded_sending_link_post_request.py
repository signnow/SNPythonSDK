"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Any, Dict, Optional

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="createDocumentGroupEmbeddedSendingLink",
    url="/v2/document-groups/{document_group_id}/embedded-sending",
    method="post",
    auth="bearer",
    namespace="embeddedSending",
    entity="documentGroupEmbeddedSendingLink",
    content_type="application/json",
)
class DocumentGroupEmbeddedSendingLinkPostRequest(RequestInterface):
    """
    Represents a request to create a document group embedded sending link.
    """

    def __init__(
        self,
        redirect_uri: Optional[str] = None,
        link_expiration: Optional[int] = None,
        redirect_target: Optional[str] = None,
        type: Optional[str] = None,
    ):
        """
        Constructs a new DocumentGroupEmbeddedSendingLinkPostRequest.

        Args:
            redirect_uri: The redirect URI for the request. Optional.
            link_expiration: The link expiration time for the request. Optional.
            redirect_target: The redirect target for the request. Optional.
            type: The type of the embedded link: manage (default), edit, send-invite. Optional.
        """
        self.redirect_uri = redirect_uri
        self.link_expiration = link_expiration
        self.redirect_target = redirect_target
        self.type = type if type is not None else "manage"
        self._uri_params: Dict[str, str] = {}

    def with_document_group_id(
        self, document_group_id: str
    ) -> "DocumentGroupEmbeddedSendingLinkPostRequest":
        """
        Adds the document group ID to the URI parameters.

        Args:
            document_group_id: The document group ID to add.

        Returns:
            The current instance of DocumentGroupEmbeddedSendingLinkPostRequest.
        """
        self._uri_params["document_group_id"] = document_group_id
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
            A dictionary containing redirect_uri, link_expiration, redirect_target, and type.
        """
        payload: Dict[str, Any] = {}
        if self.redirect_uri is not None:
            payload["redirect_uri"] = self.redirect_uri
        if self.link_expiration is not None:
            payload["link_expiration"] = self.link_expiration
        if self.redirect_target is not None:
            payload["redirect_target"] = self.redirect_target
        if self.type is not None:
            payload["type"] = self.type
        return payload
