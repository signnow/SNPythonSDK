"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass
from typing import Any, Dict, Optional, Protocol


@dataclass
class ApiEndpoint:
    """
    Data class to define API endpoint details.
    This is the Python equivalent of the Java @ApiEndpoint annotation.
    """

    name: str
    url: str
    method: str
    auth: str = "bearer"
    namespace: str = ""
    entity: str = ""
    type: str = "application/json"


class RequestInterface(Protocol):
    """
    This interface defines the structure of a Request.
    """

    def uri_params(self) -> Dict[str, str]:
        """
        This method is used to get the URI parameters present in the Request.

        Example: URL: /document/{document_id}/invite
        uri_params(): {"document_id": "e896ec9311a74a8a8ee9faff7049446fe452e461"}

        Returns:
            Dict containing the URI parameters as key-value pairs
        """
        ...

    def payload(self) -> Dict[str, Any]:
        """
        This method is used to get the actual Request's body (POST, PUT).

        Returns:
            Dict containing the payload of the request as key-value pairs
        """
        ...

    def query_params(self) -> Optional[Dict[str, str]]:
        """
        This method is used to get the query parameters for the Request.

        Returns:
            Dict containing the query parameters as key-value pairs, or None
        """
        return None


class ApiEndpointResolver:
    """
    This class retrieves required endpoint data for specified request.
    """

    @staticmethod
    def resolve(request: RequestInterface) -> ApiEndpoint:
        """
        This method is used to construct ApiEndpoint data object from request object.

        Args:
            request: The request object that needs to be resolved to an ApiEndpoint

        Returns:
            ApiEndpoint: The ApiEndpoint from the request object

        Raises:
            ValueError: If the request class is not annotated with ApiEndpoint
        """
        if not hasattr(request, "__api_endpoint__"):
            raise ValueError(
                f"Request class {request.__class__.__name__} is not annotated with ApiEndpoint."
            )
        return request.__api_endpoint__


def api_endpoint(
    name: str,
    url: str,
    method: str,
    auth: str = "bearer",
    namespace: str = "",
    entity: str = "",
    content_type: str = "application/json",
):
    """
    Decorator to define API endpoint details at runtime.
    This is the Python equivalent of the Java @ApiEndpoint annotation.

    Args:
        name: The name of the API endpoint
        url: The URL of the API endpoint
        method: The HTTP method to be used for the API endpoint
        auth: The authentication method to be used for the API endpoint (default: "bearer")
        namespace: The namespace of the API endpoint
        entity: The entity of the API endpoint
        content_type: The content type of the API endpoint (default: "application/json")

    Returns:
        A decorator function
    """

    def decorator(cls):
        endpoint = ApiEndpoint(
            name=name,
            url=url,
            method=method,
            auth=auth,
            namespace=namespace,
            entity=entity,
            type=content_type,
        )
        cls.__api_endpoint__ = endpoint
        return cls

    return decorator
