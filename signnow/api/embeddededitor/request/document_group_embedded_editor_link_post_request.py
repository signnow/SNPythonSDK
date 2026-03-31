"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Any, Dict, Optional

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="createDocumentGroupEmbeddedEditorLink",
    url="/v2/document-groups/{document_group_id}/embedded-editor",
    method="post",
    auth="bearer",
    namespace="embeddedEditor",
    entity="documentGroupEmbeddedEditorLink",
    content_type="application/json",
)
class DocumentGroupEmbeddedEditorLinkPostRequest(RequestInterface):
    """
    Represents a request to create a link to embedded document group editor.
    """

    def __init__(
        self,
        redirect_uri: Optional[str] = None,
        redirect_target: Optional[str] = None,
        link_expiration: Optional[int] = None,
    ):
        """
        Constructs a new DocumentGroupEmbeddedEditorLinkPostRequest.

        Args:
            redirect_uri: Link that opens after the user has completed editing the document group. Optional.
            redirect_target: Determines on what browser's tab should be opened the redirectUri. Optional.
            link_expiration: Link expiration time in minutes. Optional.
        """
        self.redirect_uri = redirect_uri
        self.redirect_target = redirect_target
        self.link_expiration = link_expiration
        self._uri_params: Dict[str, str] = {}

    def with_document_group_id(
        self, document_group_id: str
    ) -> "DocumentGroupEmbeddedEditorLinkPostRequest":
        """
        Adds a document group ID to the URI parameters.

        Args:
            document_group_id: The ID of the document group to be edited as embedded one.

        Returns:
            The current DocumentGroupEmbeddedEditorLinkPostRequest instance.
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
        Returns a dictionary containing the payload for the request.

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
