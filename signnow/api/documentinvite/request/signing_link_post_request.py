"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Dict, Optional

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="createSigningLink",
    url="/link",
    method="post",
    auth="bearer",
    namespace="documentInvite",
    entity="signingLink",
    content_type="application/json",
)
class SigningLinkPostRequest(RequestInterface):
    """
    This class represents a request to create a signing link.
    """

    def __init__(self, document_id: str, redirect_uri: Optional[str] = None):
        """
        Constructor for SigningLinkPostRequest.

        Args:
            document_id: The ID of the document for which the signing link is to be created
            redirect_uri: The URI to which the user will be redirected after signing (optional)
        """
        self._document_id = document_id
        self._redirect_uri = redirect_uri or ""

    def uri_params(self) -> Dict[str, str]:
        """Returns an empty dict as there are no URI parameters."""
        return {}

    def payload(self) -> Dict[str, str]:
        """
        Returns a dict with the documentId and redirectUri.

        Returns:
            A dict with the documentId and redirectUri
        """
        return {
            "document_id": self._document_id,
            "redirect_uri": self._redirect_uri,
        }
