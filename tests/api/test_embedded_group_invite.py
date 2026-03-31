"""
Tests for EmbeddedGroupInvite API.

This module contains tests for embedded group invite API including:
- Embedded group invite operations
- Embedded group invite link operations

These tests verify that embedded group invite requests and responses can be properly
created and structured for interaction with the SignNow API.
"""

from signnow.api.embeddedgroupinvite.request import (
    GroupInviteDeleteRequest,
    GroupInviteLinkPostRequest,
    GroupInvitePostRequest,
)
from signnow.api.embeddedgroupinvite.response import (
    GroupInviteDeleteResponse,
    GroupInviteLinkPostResponse,
    GroupInvitePostResponse,
)


def test_group_invite_post_request_creation():
    """Test GroupInvitePostRequest creation and structure."""
    request = GroupInvitePostRequest(invites=[])
    request.with_document_group_id("test_group_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["document_group_id"] == "test_group_id"
    payload = request.payload()
    assert "invites" in payload


def test_group_invite_link_post_request_creation():
    """Test GroupInviteLinkPostRequest creation and structure."""
    request = GroupInviteLinkPostRequest()
    request.with_document_group_id("test_group_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["document_group_id"] == "test_group_id"


def test_group_invite_post_response_structure():
    """Test GroupInvitePostResponse data structure."""
    response = GroupInvitePostResponse()
    assert response is not None


def test_group_invite_link_post_response_structure():
    """Test GroupInviteLinkPostResponse data structure."""
    response = GroupInviteLinkPostResponse()
    assert response is not None


def test_group_invite_delete_request_creation():
    """Test GroupInviteDeleteRequest creation and structure."""
    request = GroupInviteDeleteRequest()
    request.with_document_group_id("test_group_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["document_group_id"] == "test_group_id"


def test_group_invite_delete_response_structure():
    """Test GroupInviteDeleteResponse data structure."""
    response = GroupInviteDeleteResponse()
    assert response is not None


# ============================================================================
# Real API Call Tests (similar to Java SDK tests)
# ============================================================================


def test_group_invite_post_api_call(mock_api_client):
    """
    Test real API call for creating embedded group invite.

    Verifies that:
    - ApiClient can send GroupInvitePostRequest
    - Response is properly parsed (similar to Java EmbeddedGroupInviteTest.testPostGroupInvite)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {
        "data": {
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
    request = GroupInvitePostRequest(invites=[])
    request.with_document_group_id("test_group_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, GroupInvitePostResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_group_invite_link_post_api_call(mock_api_client):
    """
    Test real API call for creating embedded group invite link.

    Verifies that:
    - ApiClient can send GroupInviteLinkPostRequest
    - Response is properly parsed (similar to Java EmbeddedGroupInviteLinkTest.testPostGroupInviteLink)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {
        "data": {
            "link": "https://signnow.com/embedded/group/invite/test",
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
    request = GroupInviteLinkPostRequest()
    request.with_document_group_id("test_group_id")
    request.with_embedded_invite_id("test_invite_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, GroupInviteLinkPostResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_group_invite_delete_api_call(mock_api_client):
    """
    Test real API call for deleting embedded group invite.

    Verifies that:
    - ApiClient can send GroupInviteDeleteRequest
    - Response is properly parsed (similar to Java EmbeddedGroupInviteTest.testDeleteGroupInvite)
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
    request = GroupInviteDeleteRequest()
    request.with_document_group_id("test_group_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, GroupInviteDeleteResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()
