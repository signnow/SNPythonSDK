"""
Tests for request classes and API endpoint resolver.

This module contains tests for API request handling including:
- Token requests (POST and GET) for authentication
- Document requests for document operations
- User requests for user information
- API endpoint resolver for resolving request endpoints

These tests verify that requests can be properly created, configured,
and resolved to correct API endpoints with proper parameters and payloads.
"""

from signnow.api.auth.request import TokenGetRequest, TokenPostRequest
from signnow.api.document.request import DocumentGetRequest
from signnow.api.user.request import UserGetRequest
from signnow.core.request import ApiEndpointResolver


def test_token_post_request():
    """
    Test TokenPostRequest for OAuth2 token generation.

    Verifies that:
    - TokenPostRequest can be created with user credentials
    - Request payload contains username, password, scope, and grant_type
    - URI parameters are correctly set (empty for POST)
    - Request has API endpoint annotation
    """
    request = TokenPostRequest(
        user="test_user",
        password="test_password",
        scope="*",
        grant_type="password",
        code="",
    )
    assert request.uri_params() == {}
    payload = request.payload()
    assert payload["username"] == "test_user"
    assert payload["password"] == "test_password"
    assert payload["scope"] == "*"
    assert payload["grant_type"] == "password"
    assert hasattr(request, "__api_endpoint__")


def test_token_get_request():
    """
    Test TokenGetRequest for OAuth2 token verification.

    Verifies that:
    - TokenGetRequest can be created without parameters
    - URI parameters and payload are empty for GET request
    - Request has API endpoint annotation
    """
    request = TokenGetRequest()
    assert request.uri_params() == {}
    assert request.payload() == {}
    assert hasattr(request, "__api_endpoint__")


def test_document_get_request():
    """
    Test DocumentGetRequest for retrieving document information.

    Verifies that:
    - DocumentGetRequest can be created and configured with document ID
    - Document ID is correctly set in URI parameters
    - Payload is empty for GET request
    - Request has API endpoint annotation
    """
    request = DocumentGetRequest()
    request.with_document_id("test_doc_id")
    uri_params = request.uri_params()
    assert uri_params["document_id"] == "test_doc_id"
    assert request.payload() == {}
    assert hasattr(request, "__api_endpoint__")


def test_user_get_request():
    """
    Test UserGetRequest for retrieving user information.

    Verifies that:
    - UserGetRequest can be created without parameters
    - URI parameters and payload are empty for GET request
    - Request has API endpoint annotation
    """
    request = UserGetRequest()
    assert request.uri_params() == {}
    assert request.payload() == {}
    assert hasattr(request, "__api_endpoint__")


def test_api_endpoint_resolver():
    """
    Test ApiEndpointResolver for resolving request endpoints.

    Verifies that:
    - ApiEndpointResolver can resolve request to endpoint
    - Endpoint name, URL, method, and auth type are correctly resolved
    - Endpoint namespace and entity are correctly identified
    - Endpoint information matches the request type
    """
    request = TokenGetRequest()
    resolver = ApiEndpointResolver()
    endpoint = resolver.resolve(request)
    assert endpoint.name == "getToken"
    assert endpoint.url == "/oauth2/token"
    assert endpoint.method == "get"
    assert endpoint.auth == "bearer"
    assert endpoint.namespace == "auth"
    assert endpoint.entity == "token"
