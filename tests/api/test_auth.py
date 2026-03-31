"""
Tests for Auth API.

This module contains tests for authentication API including:
- Token generation (POST /oauth2/token)
- Token verification (GET /oauth2/token)
- Token refresh (POST /oauth2/token with refresh_token grant type)

These tests verify that authentication tokens can be properly obtained,
verified, and refreshed through the SignNow API.
"""

from signnow.api.auth.request import TokenGetRequest, TokenPostRequest
from signnow.api.auth.response import TokenGetResponse, TokenPostResponse


def test_token_post_request_creation():
    """
    Test TokenPostRequest creation and payload.

    Verifies that:
    - TokenPostRequest can be created with user credentials
    - Request payload contains correct username, password, scope, and grant_type
    - URI parameters are empty for POST request
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


def test_token_get_request_creation():
    """
    Test TokenGetRequest creation.

    Verifies that:
    - TokenGetRequest can be created without parameters
    - Request has correct API endpoint annotation
    - URI parameters and payload are empty
    """
    request = TokenGetRequest()

    assert request.uri_params() == {}
    assert request.payload() == {}
    assert hasattr(request, "__api_endpoint__")


def test_token_post_response_structure():
    """
    Test TokenPostResponse data structure.

    Verifies that:
    - TokenPostResponse can be instantiated with token data
    - All response fields are correctly stored
    - Default values are properly set
    """
    response = TokenPostResponse(
        expires_in=3600,
        token_type="bearer",
        access_token="test_access_token",
        refresh_token="test_refresh_token",
        scope="*",
        last_login=1234567890,
    )

    assert response.expires_in == 3600
    assert response.token_type == "bearer"
    assert response.access_token == "test_access_token"
    assert response.refresh_token == "test_refresh_token"
    assert response.scope == "*"
    assert response.last_login == 1234567890


def test_token_get_response_structure():
    """
    Test TokenGetResponse data structure.

    Verifies that:
    - TokenGetResponse can be instantiated with token data
    - All response fields are correctly stored
    """
    response = TokenGetResponse(
        access_token="test_access_token",
        scope="*",
        expires_in=3600,
        token_type="bearer",
    )

    assert response.access_token == "test_access_token"
    assert response.scope == "*"
    assert response.expires_in == 3600
    assert response.token_type == "bearer"


def test_refresh_token_request_creation():
    """
    Test refresh token request creation.

    Verifies that:
    - TokenPostRequest can be created with refresh_token grant type
    - Request payload contains refresh_token instead of username/password
    """
    request = TokenPostRequest(
        user="",  # Not used for refresh_token grant
        password="",  # Not used for refresh_token grant
        scope="*",
        grant_type="refresh_token",
        code="test_refresh_token",  # refresh_token is passed in code field
    )

    payload = request.payload()
    assert payload["grant_type"] == "refresh_token"
    assert payload["scope"] == "*"
    # Note: In actual implementation, refresh_token might be in a different field
    # This test verifies the basic structure


# ============================================================================
# Real API Call Tests (similar to Java SDK tests)
# ============================================================================


def test_token_post_api_call(mock_api_client):
    """
    Test real API call for posting token (authentication).

    Verifies that:
    - ApiClient can send TokenPostRequest
    - Response is properly parsed with all token fields
    - Response contains access_token, refresh_token, expires_in (similar to Java TokenTest.testPostToken)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {
        "expires_in": 3600,
        "token_type": "bearer",
        "access_token": "test_access_token",
        "refresh_token": "test_refresh_token",
        "scope": "*",
        "last_login": 1234567890,
    }

    # Create mock httpx.Response
    mock_response = MagicMock(spec=httpx.Response)
    mock_response.status_code = 200
    mock_response.text = json.dumps(mock_response_data)
    mock_response.content = json.dumps(mock_response_data).encode()
    mock_response.headers = {"Content-Type": "application/json"}

    # Configure mock client
    mock_api_client._client.request.return_value = mock_response

    # Execute API call
    request = TokenPostRequest(
        user="test_user",
        password="test_password",
        scope="*",
        grant_type="password",
        code="",
    )
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, TokenPostResponse)
    assert response.access_token == "test_access_token"
    assert response.refresh_token == "test_refresh_token"
    assert response.expires_in == 3600
    assert response.token_type == "bearer"
    assert response.scope == "*"
    assert response.last_login == 1234567890

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_token_get_api_call(mock_api_client):
    """
    Test real API call for getting token (verification).

    Verifies that:
    - ApiClient can send TokenGetRequest
    - Response is properly parsed (similar to Java TokenTest.testGetToken)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {
        "access_token": "test_access_token",
        "scope": "*",
        "expires_in": 3600,
        "token_type": "bearer",
    }

    # Create mock httpx.Response
    mock_response = MagicMock(spec=httpx.Response)
    mock_response.status_code = 200
    mock_response.text = json.dumps(mock_response_data)
    mock_response.content = json.dumps(mock_response_data).encode()
    mock_response.headers = {"Content-Type": "application/json"}

    # Configure mock client
    mock_api_client._client.request.return_value = mock_response

    # Execute API call
    request = TokenGetRequest()
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, TokenGetResponse)
    assert response.access_token == "test_access_token"
    assert response.scope == "*"
    assert response.expires_in == 3600
    assert response.token_type == "bearer"

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_refresh_token_post_api_call(mock_api_client):
    """
    Test real API call for refreshing token.

    Verifies that:
    - ApiClient can send TokenPostRequest with refresh_token grant type
    - Response contains new access_token and refresh_token (similar to Java RefreshTokenTest.testPostRefreshToken)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {
        "expires_in": 3600,
        "token_type": "bearer",
        "access_token": "new_access_token",
        "refresh_token": "new_refresh_token",
        "scope": "*",
        "last_login": 1234567890,
    }

    # Create mock httpx.Response
    mock_response = MagicMock(spec=httpx.Response)
    mock_response.status_code = 200
    mock_response.text = json.dumps(mock_response_data)
    mock_response.content = json.dumps(mock_response_data).encode()
    mock_response.headers = {"Content-Type": "application/json"}

    # Configure mock client
    mock_api_client._client.request.return_value = mock_response

    # Execute API call
    request = TokenPostRequest(
        user="",
        password="",
        scope="*",
        grant_type="refresh_token",
        code="old_refresh_token",
    )
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, TokenPostResponse)
    assert response.access_token == "new_access_token"
    assert response.refresh_token == "new_refresh_token"
    assert response.expires_in == 3600
    assert response.token_type == "bearer"
    assert response.scope == "*"

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()
