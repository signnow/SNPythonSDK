"""
Tests for EmbeddedInvite API.

This module contains tests for embedded invite API including:
- Embedded document invite operations
- Embedded document invite link operations

These tests verify that embedded invite requests and responses can be properly
created and structured for interaction with the SignNow API.
"""

from signnow.api.embeddedinvite.request import (
    DocumentInviteDeleteRequest,
    DocumentInviteLinkPostRequest,
    DocumentInvitePostRequest,
)
from signnow.api.embeddedinvite.response import (
    DocumentInviteDeleteResponse,
    DocumentInviteLinkPostResponse,
    DocumentInvitePostResponse,
)


def test_document_invite_post_request_creation():
    """Test DocumentInvitePostRequest creation and structure."""
    request = DocumentInvitePostRequest(invites=[])
    request.with_document_id("test_doc_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["document_id"] == "test_doc_id"
    payload = request.payload()
    assert "invites" in payload


def test_document_invite_link_post_request_creation():
    """Test DocumentInviteLinkPostRequest creation and structure."""
    request = DocumentInviteLinkPostRequest()
    request.with_document_id("test_doc_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["document_id"] == "test_doc_id"


def test_document_invite_delete_request_creation():
    """Test DocumentInviteDeleteRequest creation and structure."""
    request = DocumentInviteDeleteRequest()
    request.with_document_id("test_doc_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["document_id"] == "test_doc_id"


def test_document_invite_post_response_structure():
    """Test DocumentInvitePostResponse data structure."""
    response = DocumentInvitePostResponse()
    assert response is not None


def test_document_invite_link_post_response_structure():
    """Test DocumentInviteLinkPostResponse data structure."""
    response = DocumentInviteLinkPostResponse()
    assert response is not None


def test_document_invite_delete_response_structure():
    """Test DocumentInviteDeleteResponse data structure."""
    response = DocumentInviteDeleteResponse()
    assert response is not None


# ============================================================================
# Real API Call Tests (similar to Java SDK tests)
# ============================================================================


def test_document_invite_post_api_call(mock_api_client):
    """
    Test real API call for creating embedded document invite.

    Verifies that:
    - ApiClient can send DocumentInvitePostRequest
    - Response is properly parsed (similar to Java DocumentInviteTest.testPostDocumentInvite)
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
    request = DocumentInvitePostRequest(invites=[])
    request.with_document_id("test_doc_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, DocumentInvitePostResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_document_invite_link_post_api_call(mock_api_client):
    """
    Test real API call for creating embedded document invite link.

    Verifies that:
    - ApiClient can send DocumentInviteLinkPostRequest
    - Response is properly parsed (similar to Java DocumentInviteLinkTest.testPostDocumentInviteLink)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {
        "data": {
            "link": "https://signnow.com/embedded/invite/test",
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
    request = DocumentInviteLinkPostRequest()
    request.with_document_id("test_doc_id")
    request.with_field_invite_id("test_invite_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, DocumentInviteLinkPostResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_document_invite_delete_api_call(mock_api_client):
    """
    Test real API call for deleting embedded document invite.

    Verifies that:
    - ApiClient can send DocumentInviteDeleteRequest
    - Response is properly parsed (similar to Java DocumentInviteTest.testDeleteDocumentInvite)
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
    request = DocumentInviteDeleteRequest()
    request.with_document_id("test_doc_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, DocumentInviteDeleteResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()
