"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Dict

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="createTemplate",
    url="/template",
    method="post",
    auth="bearer",
    namespace="template",
    entity="template",
    content_type="application/json",
)
class TemplatePostRequest(RequestInterface):
    """
    Represents a request to create a template.
    """

    def __init__(self, document_id: str, document_name: str):
        """
        Constructs a new TemplatePostRequest.

        Args:
            document_id: The ID of the document to be used as a template.
            document_name: The name of the document to be used as a template.
        """
        self.document_id = document_id
        self.document_name = document_name

    def uri_params(self) -> Dict[str, str]:
        """
        Returns an empty dictionary for URI parameters.

        Returns:
            An empty dictionary.
        """
        return {}

    def payload(self) -> Dict[str, str]:
        """
        Returns a dictionary with the document ID and name as the payload.

        Returns:
            A dictionary with the document ID and name.
        """
        return {
            "document_id": self.document_id,
            "document_name": self.document_name,
        }
