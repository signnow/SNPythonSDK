"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Dict

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="getDocumentGroupTemplateRecipients",
    url="/v2/document-group-templates/{template_group_id}/recipients",
    method="get",
    auth="bearer",
    namespace="documentGroupTemplate",
    entity="documentGroupTemplateRecipients",
    content_type="application/json",
)
class DocumentGroupTemplateRecipientsGetRequest(RequestInterface):
    """
    Represents a request to get the recipients of a document group template.
    """

    def __init__(self):
        """Constructs a new DocumentGroupTemplateRecipientsGetRequest."""
        self._uri_params: Dict[str, str] = {}

    def with_template_group_id(
        self, template_group_id: str
    ) -> "DocumentGroupTemplateRecipientsGetRequest":
        """
        Sets the template group id in the URI parameters.

        Args:
            template_group_id: The id of the document group template.

        Returns:
            The current instance.
        """
        self._uri_params["template_group_id"] = template_group_id
        return self

    def uri_params(self) -> Dict[str, str]:
        """Returns a copy of the URI parameters."""
        return dict(self._uri_params)

    def payload(self) -> Dict[str, str]:
        """Returns an empty dictionary for the payload."""
        return {}
