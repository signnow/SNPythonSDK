"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Dict

from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="getFolder",
    url="/folder",
    method="get",
    auth="bearer",
    namespace="folder",
    entity="folder",
    content_type="application/json",
)
class FolderGetRequest(RequestInterface):
    """
    Represents a request to get a folder from the API.
    """

    def uri_params(self) -> Dict[str, str]:
        """
        Returns an empty dictionary for URI parameters.

        Returns:
            An empty dictionary.
        """
        return {}

    def payload(self) -> Dict[str, str]:
        """
        Returns an empty dictionary for the payload.

        Returns:
            An empty dictionary.
        """
        return {}
