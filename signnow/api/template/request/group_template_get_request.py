"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Dict

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="getDocumentGroupTemplate",
    url="/documentgroup/template/{template_id}",
    method="get",
    auth="bearer",
    namespace="template",
    entity="groupTemplate",
    content_type="application/json",
)
class GroupTemplateGetRequest(RequestInterface):
    """
    Represents a request to get a group template.
    """

    def __init__(self):
        """Constructs a new GroupTemplateGetRequest."""
        self._uri_params: Dict[str, str] = {}

    def with_template_id(self, template_id: str) -> "GroupTemplateGetRequest":
        """
        Adds a template ID to the URI parameters.

        Args:
            template_id: The ID of the template to get.

        Returns:
            The current instance of GroupTemplateGetRequest.
        """
        self._uri_params["template_id"] = template_id
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
        Returns an empty payload.

        Returns:
            An empty dictionary.
        """
        return {}
