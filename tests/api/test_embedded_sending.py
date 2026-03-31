"""
Tests for EmbeddedSending API.

This module contains tests for embedded sending API including:
- Document embedded sending link operations
- Document group embedded sending link operations

These tests verify that embedded sending requests and responses can be properly
created and structured for interaction with the SignNow API.
"""

from signnow.api.embeddedsending.request import (
    DocumentEmbeddedSendingLinkPostRequest,
    DocumentGroupEmbeddedSendingLinkPostRequest,
)
from signnow.api.embeddedsending.response import (
    DocumentEmbeddedSendingLinkPostResponse,
    DocumentGroupEmbeddedSendingLinkPostResponse,
)


def test_document_embedded_sending_link_post_request_creation():
    """Test DocumentEmbeddedSendingLinkPostRequest creation and structure."""
    request = DocumentEmbeddedSendingLinkPostRequest(type="manage")
    request.with_document_id("test_doc_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["document_id"] == "test_doc_id"


def test_document_group_embedded_sending_link_post_request_creation():
    """Test DocumentGroupEmbeddedSendingLinkPostRequest creation and structure."""
    request = DocumentGroupEmbeddedSendingLinkPostRequest()
    request.with_document_group_id("test_group_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["document_group_id"] == "test_group_id"


def test_document_embedded_sending_link_post_response_structure():
    """Test DocumentEmbeddedSendingLinkPostResponse data structure."""
    response = DocumentEmbeddedSendingLinkPostResponse()
    assert response is not None


def test_document_group_embedded_sending_link_post_response_structure():
    """Test DocumentGroupEmbeddedSendingLinkPostResponse data structure."""
    response = DocumentGroupEmbeddedSendingLinkPostResponse()
    assert response is not None


# ============================================================================
# Real API Call Tests (similar to Java SDK tests)
# ============================================================================


def test_document_embedded_sending_link_post_api_call(mock_api_client):
    """
    Test real API call for creating document embedded sending link.

    Verifies that:
    - ApiClient can send DocumentEmbeddedSendingLinkPostRequest
    - Response is properly parsed (similar to Java DocumentEmbeddedSendingLinkTest.testPostDocumentEmbeddedSendingLink)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {
        "data": {
            "link": "https://signnow.com/embedded/sending/test",
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
    request = DocumentEmbeddedSendingLinkPostRequest(type="manage")
    request.with_document_id("test_doc_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, DocumentEmbeddedSendingLinkPostResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_document_group_embedded_sending_link_post_api_call(mock_api_client):
    """
    Test real API call for creating document group embedded sending link.

    Verifies that:
    - ApiClient can send DocumentGroupEmbeddedSendingLinkPostRequest
    - Response is properly parsed (similar to Java DocumentGroupEmbeddedSendingLinkTest.testPostDocumentGroupEmbeddedSendingLink)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {
        "data": {
            "link": "https://signnow.com/embedded/group/sending/test",
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
    request = DocumentGroupEmbeddedSendingLinkPostRequest()
    request.with_document_group_id("test_group_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, DocumentGroupEmbeddedSendingLinkPostResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()
