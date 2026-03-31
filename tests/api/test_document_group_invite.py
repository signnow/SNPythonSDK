"""
Tests for DocumentGroupInvite API.

This module contains tests for document group invite API including:
- Group invite operations
- Cancel group invite operations
- Resend group invite operations
- Reassign signer operations
- Pending invite operations

These tests verify that document group invite requests and responses can be properly
created and structured for interaction with the SignNow API.
"""

from signnow.api.documentgroupinvite.request import (
    CancelGroupInvitePostRequest,
    GroupInviteGetRequest,
    GroupInvitePostRequest,
    PendingInviteGetRequest,
    ReassignSignerPostRequest,
    ResendGroupInvitePostRequest,
)
from signnow.api.documentgroupinvite.response import (
    CancelGroupInvitePostResponse,
    GroupInviteGetResponse,
    GroupInvitePostResponse,
    PendingInviteGetResponse,
    ReassignSignerPostResponse,
    ResendGroupInvitePostResponse,
)


def test_group_invite_post_request_creation():
    """Test GroupInvitePostRequest creation and structure."""
    request = GroupInvitePostRequest(invite_steps=[{"step": 1}])
    request.with_document_group_id("test_group_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["document_group_id"] == "test_group_id"
    payload = request.payload()
    assert "invite_steps" in payload


def test_group_invite_get_request_creation():
    """Test GroupInviteGetRequest creation and structure."""
    request = GroupInviteGetRequest()
    request.with_document_group_id("test_group_id")
    request.with_invite_id("test_invite_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["document_group_id"] == "test_group_id"
    assert uri_params["invite_id"] == "test_invite_id"


def test_cancel_group_invite_post_request_creation():
    """Test CancelGroupInvitePostRequest creation and structure."""
    request = CancelGroupInvitePostRequest()
    request.with_document_group_id("test_group_id")
    request.with_invite_id("test_invite_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["document_group_id"] == "test_group_id"
    assert uri_params["invite_id"] == "test_invite_id"


def test_resend_group_invite_post_request_creation():
    """Test ResendGroupInvitePostRequest creation and structure."""
    request = ResendGroupInvitePostRequest(email="test@example.com")
    request.with_document_group_id("test_group_id")
    request.with_invite_id("test_invite_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["document_group_id"] == "test_group_id"
    assert uri_params["invite_id"] == "test_invite_id"


def test_reassign_signer_post_request_creation():
    """Test ReassignSignerPostRequest creation and structure."""
    request = ReassignSignerPostRequest(
        user_to_update="user1@example.com", replace_with_this_user="user2@example.com"
    )
    request.with_document_group_id("test_group_id")
    request.with_invite_id("test_invite_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["document_group_id"] == "test_group_id"
    assert uri_params["invite_id"] == "test_invite_id"


def test_pending_invite_get_request_creation():
    """Test PendingInviteGetRequest creation and structure."""
    request = PendingInviteGetRequest()
    request.with_document_group_id("test_group_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["document_group_id"] == "test_group_id"


def test_group_invite_post_response_structure():
    """Test GroupInvitePostResponse data structure."""
    response = GroupInvitePostResponse()
    assert response is not None


def test_group_invite_get_response_structure():
    """Test GroupInviteGetResponse data structure."""
    response = GroupInviteGetResponse()
    assert response is not None


def test_cancel_group_invite_post_response_structure():
    """Test CancelGroupInvitePostResponse data structure."""
    response = CancelGroupInvitePostResponse()
    assert response is not None


def test_resend_group_invite_post_response_structure():
    """Test ResendGroupInvitePostResponse data structure."""
    response = ResendGroupInvitePostResponse()
    assert response is not None


def test_reassign_signer_post_response_structure():
    """Test ReassignSignerPostResponse data structure."""
    response = ReassignSignerPostResponse()
    assert response is not None


def test_pending_invite_get_response_structure():
    """Test PendingInviteGetResponse data structure."""
    response = PendingInviteGetResponse()
    assert response is not None


# ============================================================================
# Real API Call Tests (similar to Java SDK tests)
# ============================================================================


def test_group_invite_post_api_call(mock_api_client):
    """
    Test real API call for creating group invite.

    Verifies that:
    - ApiClient can send GroupInvitePostRequest
    - Response is properly parsed (similar to Java GroupInviteTest.testPostGroupInvite)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {
        "id": "invite_id",
        "pending_invite_link": "https://signnow.com/invite/test",
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
    request = GroupInvitePostRequest(invite_steps=[])
    request.with_document_group_id("test_group_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, GroupInvitePostResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_group_invite_get_api_call(mock_api_client):
    """
    Test real API call for getting group invite.

    Verifies that:
    - ApiClient can send GroupInviteGetRequest
    - Response is properly parsed (similar to Java GroupInviteTest.testGetGroupInvite)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {
        "invite": {
            "id": "invite_id",
            "status": "pending",
        }
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
    request = GroupInviteGetRequest()
    request.with_document_group_id("test_group_id")
    request.with_invite_id("test_invite_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, GroupInviteGetResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_cancel_group_invite_post_api_call(mock_api_client):
    """
    Test real API call for canceling group invite.

    Verifies that:
    - ApiClient can send CancelGroupInvitePostRequest
    - Response is properly parsed (similar to Java CancelGroupInviteTest.testPostCancelGroupInvite)
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
    request = CancelGroupInvitePostRequest()
    request.with_document_group_id("test_group_id")
    request.with_invite_id("test_invite_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, CancelGroupInvitePostResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_resend_group_invite_post_api_call(mock_api_client):
    """
    Test real API call for resending group invite.

    Verifies that:
    - ApiClient can send ResendGroupInvitePostRequest
    - Response is properly parsed (similar to Java ResendGroupInviteTest.testPostResendGroupInvite)
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
    request = ResendGroupInvitePostRequest(email="signer@example.com")
    request.with_document_group_id("test_group_id")
    request.with_invite_id("test_invite_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, ResendGroupInvitePostResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_reassign_signer_post_api_call(mock_api_client):
    """
    Test real API call for reassigning signer.

    Verifies that:
    - ApiClient can send ReassignSignerPostRequest
    - Response is properly parsed (similar to Java ReassignSignerTest.testPostReassignSigner)
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
    request = ReassignSignerPostRequest(
        user_to_update="old@example.com",
        replace_with_this_user="new@example.com",
    )
    request.with_document_group_id("test_group_id")
    request.with_invite_id("test_invite_id")
    request.with_step_id("step_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, ReassignSignerPostResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_pending_invite_get_api_call(mock_api_client):
    """
    Test real API call for getting pending invites.

    Verifies that:
    - ApiClient can send PendingInviteGetRequest
    - Response is properly parsed (similar to Java PendingInviteTest.testGetPendingInvite)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {
        "invites": [],
        "document_group_name": "Test Group",
        "sign_as_merged": False,
        "owner_organization_id": "org_id",
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
    request = PendingInviteGetRequest()
    request.with_document_group_id("test_group_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, PendingInviteGetResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()
