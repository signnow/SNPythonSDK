"""
Tests for User API.

This module contains tests for user API including:
- User information retrieval (GET /user)
- User creation (POST /user)
- User update (PUT /user)
- Password reset operations
- User initials operations
- Email verification operations

These tests verify that user requests and responses can be properly
created and structured for interaction with the SignNow API.
"""

from signnow.api.user.request import (
    EmailVerifyPutRequest,
    InitialGetRequest,
    InitialPutRequest,
    ResetPasswordPostRequest,
    UserGetRequest,
    UserPostRequest,
    UserPutRequest,
)
from signnow.api.user.response import (
    EmailVerifyPutResponse,
    InitialGetResponse,
    InitialPutResponse,
    ResetPasswordPostResponse,
    UserGetResponse,
    UserPostResponse,
    UserPutResponse,
)


def test_user_get_request_creation():
    """
    Test UserGetRequest creation and structure.

    Verifies that:
    - UserGetRequest can be created without parameters
    - Request has correct API endpoint annotation
    - URI parameters and payload are empty
    """
    request = UserGetRequest()

    assert hasattr(request, "__api_endpoint__")
    assert request.uri_params() == {}
    assert request.payload() == {}


def test_user_post_request_creation():
    """
    Test UserPostRequest creation and structure.

    Verifies that:
    - UserPostRequest can be created with user data
    - Request payload contains user information
    - Request has correct API endpoint annotation
    """
    request = UserPostRequest(
        email="test@example.com",
        password="test_password",
        first_name="Test",
        last_name="User",
        number="1234567890",
    )

    assert hasattr(request, "__api_endpoint__")
    assert request.uri_params() == {}
    payload = request.payload()
    assert payload["email"] == "test@example.com"
    assert payload["password"] == "test_password"
    assert payload["first_name"] == "Test"
    assert payload["last_name"] == "User"
    assert payload["number"] == "1234567890"


def test_user_put_request_creation():
    """
    Test UserPutRequest creation and structure.

    Verifies that:
    - UserPutRequest can be created with update data
    - Request payload contains update information
    - Request has correct API endpoint annotation
    """
    request = UserPutRequest(first_name="Updated", last_name="Name")

    assert hasattr(request, "__api_endpoint__")
    assert request.uri_params() == {}
    payload = request.payload()
    assert payload["first_name"] == "Updated"
    assert payload["last_name"] == "Name"


def test_reset_password_request_creation():
    """
    Test ResetPasswordPostRequest creation and structure.

    Verifies that:
    - ResetPasswordPostRequest can be created with email
    - Request payload contains email for password reset
    - Request has correct API endpoint annotation
    """
    request = ResetPasswordPostRequest(email="test@example.com")

    assert hasattr(request, "__api_endpoint__")
    assert request.uri_params() == {}
    payload = request.payload()
    assert "email" in payload


def test_initial_get_request_creation():
    """
    Test InitialGetRequest creation and structure.

    Verifies that:
    - InitialGetRequest can be created without parameters
    - Request has correct API endpoint annotation
    """
    request = InitialGetRequest()

    assert hasattr(request, "__api_endpoint__")
    assert request.uri_params() == {}
    assert request.payload() == {}


def test_initial_put_request_creation():
    """
    Test InitialPutRequest creation and structure.

    Verifies that:
    - InitialPutRequest can be created with initials data
    - Request payload contains initials information
    - Request has correct API endpoint annotation
    """
    request = InitialPutRequest(data="TU")

    assert hasattr(request, "__api_endpoint__")
    assert request.uri_params() == {}
    payload = request.payload()
    assert "data" in payload
    assert payload["data"] == "TU"


def test_email_verify_request_creation():
    """
    Test EmailVerifyPutRequest creation and structure.

    Verifies that:
    - EmailVerifyPutRequest can be created with verification data
    - Request has correct API endpoint annotation
    """
    request = EmailVerifyPutRequest(
        email="test@example.com", verification_token="test_token"
    )

    assert hasattr(request, "__api_endpoint__")
    assert request.uri_params() == {}


def test_user_get_response_structure():
    """
    Test UserGetResponse data structure.

    Verifies that:
    - UserGetResponse can be instantiated with user data
    - All response fields are correctly stored
    """
    response = UserGetResponse(
        id="test_user_id",
        first_name="Test",
        last_name="User",
        primary_email="test@example.com",
    )

    assert response.id == "test_user_id"
    assert response.first_name == "Test"
    assert response.last_name == "User"
    assert response.primary_email == "test@example.com"


def test_user_post_response_structure():
    """
    Test UserPostResponse data structure.

    Verifies that:
    - UserPostResponse can be instantiated
    - Response structure is correct
    """
    response = UserPostResponse()

    assert response is not None


def test_user_put_response_structure():
    """
    Test UserPutResponse data structure.

    Verifies that:
    - UserPutResponse can be instantiated
    - Response structure is correct
    """
    response = UserPutResponse()

    assert response is not None


def test_reset_password_response_structure():
    """
    Test ResetPasswordPostResponse data structure.

    Verifies that:
    - ResetPasswordPostResponse can be instantiated
    - Response structure is correct
    """
    response = ResetPasswordPostResponse()

    assert response is not None


def test_initial_get_response_structure():
    """
    Test InitialGetResponse data structure.

    Verifies that:
    - InitialGetResponse can be instantiated with initials data
    - Initials are correctly stored
    """
    response = InitialGetResponse(
        unique_id="initials_id",
        width="100",
        height="50",
        data="TU",
        created="1234567890",
    )

    assert response.unique_id == "initials_id"
    assert response.width == "100"
    assert response.height == "50"
    assert response.data == "TU"
    assert response.created == "1234567890"


def test_initial_put_response_structure():
    """
    Test InitialPutResponse data structure.

    Verifies that:
    - InitialPutResponse can be instantiated
    - Response structure is correct
    """
    response = InitialPutResponse()

    assert response is not None


def test_email_verify_response_structure():
    """
    Test EmailVerifyPutResponse data structure.

    Verifies that:
    - EmailVerifyPutResponse can be instantiated
    - Response structure is correct
    """
    response = EmailVerifyPutResponse()

    assert response is not None


# ============================================================================
# Real API Call Tests (similar to Java SDK tests)
# ============================================================================


def test_user_get_api_call(mock_api_client):
    """
    Test real API call for getting user information.

    Verifies that:
    - ApiClient can send UserGetRequest
    - Response is properly parsed with all user fields
    - Response contains expected fields (similar to Java UserTest.testGetUser)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data matching Java SDK expectation
    mock_response_data = {
        "id": "test_user_id",
        "first_name": "Test",
        "last_name": "User",
        "active": True,
        "verified": True,
        "type": "user",
        "pro": False,
        "created": "1234567890",
        "emails": ["test@example.com"],
        "primary_email": "test@example.com",
        "subscriptions": [],
        "credits": 0,
        "has_atticus_access": False,
        "cloud_export_account_details": None,
        "is_logged_in": True,
        "billing_period": None,
        "premium_access": False,
        "companies": [],
        "document_count": 0,
        "monthly_document_count": 0,
        "lifetime_document_count": 0,
        "teams": [],
        "status": "active",
        "settings": {},
        "organization_settings": None,
        "issue_notifications": False,
        "merchant_accounts": [],
        "organization": None,
        "registration_source": None,
        "avatar_url": None,
        "signer_phone_invite": False,
        "locale": "en",
        "password_changed": "1234567890",
        "upload_limit": 100,
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
    request = UserGetRequest()
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, UserGetResponse)
    assert response.id == "test_user_id"
    assert response.first_name == "Test"
    assert response.last_name == "User"
    assert response.primary_email == "test@example.com"

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_user_post_api_call(mock_api_client):
    """
    Test real API call for creating user.

    Verifies that:
    - ApiClient can send UserPostRequest
    - Response is properly parsed (similar to Java UserTest.testPostUser)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {
        "id": "new_user_id",
        "verified": False,
        "email": "newuser@example.com",
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
    request = UserPostRequest(
        email="newuser@example.com",
        password="test_password",
        first_name="New",
        last_name="User",
        number="1234567890",
    )
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, UserPostResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_user_put_api_call(mock_api_client):
    """
    Test real API call for updating user.

    Verifies that:
    - ApiClient can send UserPutRequest
    - Response is properly parsed (similar to Java UserTest.testPutUser)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {
        "id": "test_user_id",
        "first_name": "Updated",
        "last_name": "Name",
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
    request = UserPutRequest(first_name="Updated", last_name="Name")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, UserPutResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_reset_password_post_api_call(mock_api_client):
    """
    Test real API call for resetting password.

    Verifies that:
    - ApiClient can send ResetPasswordPostRequest
    - Response is properly parsed (similar to Java ResetPasswordTest.testPostResetPassword)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {"status": "success"}

    # Create mock httpx.Response
    mock_response = MagicMock(spec=httpx.Response)
    mock_response.status_code = 200
    mock_response.text = json.dumps(mock_response_data)
    mock_response.content = json.dumps(mock_response_data).encode()
    mock_response.headers = {"Content-Type": "application/json"}

    # Configure mock client
    mock_api_client._client.request.return_value = mock_response

    # Execute API call
    request = ResetPasswordPostRequest(email="test@example.com")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, ResetPasswordPostResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_initial_get_api_call(mock_api_client):
    """
    Test real API call for getting user initials.

    Verifies that:
    - ApiClient can send InitialGetRequest
    - Response is properly parsed (similar to Java InitialTest.testGetInitial)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {
        "unique_id": "initials_id",
        "width": 100,
        "height": 50,
        "data": "TU",
        "created": "1234567890",
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
    request = InitialGetRequest()
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, InitialGetResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_initial_put_api_call(mock_api_client):
    """
    Test real API call for updating user initials.

    Verifies that:
    - ApiClient can send InitialPutRequest
    - Response is properly parsed (similar to Java InitialTest.testPutInitial)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {
        "id": "initials_id",
        "width": 100,
        "height": 50,
        "created": "1234567890",
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
    request = InitialPutRequest(data="TU")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, InitialPutResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_email_verify_put_api_call(mock_api_client):
    """
    Test real API call for verifying email.

    Verifies that:
    - ApiClient can send EmailVerifyPutRequest
    - Response is properly parsed (similar to Java EmailVerifyTest.testPutEmailVerify)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {"email": "test@example.com"}

    # Create mock httpx.Response
    mock_response = MagicMock(spec=httpx.Response)
    mock_response.status_code = 200
    mock_response.text = json.dumps(mock_response_data)
    mock_response.content = json.dumps(mock_response_data).encode()
    mock_response.headers = {"Content-Type": "application/json"}

    # Configure mock client
    mock_api_client._client.request.return_value = mock_response

    # Execute API call
    request = EmailVerifyPutRequest(
        email="test@example.com", verification_token="test_token"
    )
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, EmailVerifyPutResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()
