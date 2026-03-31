"""
Tests for EmbeddedEditor API.

This module contains tests for embedded editor API including:
- Document embedded editor link operations
- Document group embedded editor link operations

These tests verify that embedded editor requests and responses can be properly
created and structured for interaction with the SignNow API.
"""

from signnow.api.embeddededitor.request import (
    DocumentEmbeddedEditorLinkPostRequest,
    DocumentGroupEmbeddedEditorLinkPostRequest,
)
from signnow.api.embeddededitor.response import (
    DocumentEmbeddedEditorLinkPostResponse,
    DocumentGroupEmbeddedEditorLinkPostResponse,
)


def test_document_embedded_editor_link_post_request_creation():
    """Test DocumentEmbeddedEditorLinkPostRequest creation and structure."""
    request = DocumentEmbeddedEditorLinkPostRequest()
    request.with_document_id("test_doc_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["document_id"] == "test_doc_id"


def test_document_group_embedded_editor_link_post_request_creation():
    """Test DocumentGroupEmbeddedEditorLinkPostRequest creation and structure."""
    request = DocumentGroupEmbeddedEditorLinkPostRequest()
    request.with_document_group_id("test_group_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["document_group_id"] == "test_group_id"


def test_document_embedded_editor_link_post_response_structure():
    """Test DocumentEmbeddedEditorLinkPostResponse data structure."""
    response = DocumentEmbeddedEditorLinkPostResponse()
    assert response is not None


def test_document_group_embedded_editor_link_post_response_structure():
    """Test DocumentGroupEmbeddedEditorLinkPostResponse data structure."""
    response = DocumentGroupEmbeddedEditorLinkPostResponse()
    assert response is not None


# ============================================================================
# Real API Call Tests (similar to Java SDK tests)
# ============================================================================


def test_document_embedded_editor_link_post_api_call(mock_api_client):
    """
    Test real API call for creating document embedded editor link.

    Verifies that:
    - ApiClient can send DocumentEmbeddedEditorLinkPostRequest
    - Response is properly parsed (similar to Java DocumentEmbeddedEditorLinkTest.testPostDocumentEmbeddedEditorLink)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {
        "data": {
            "link": "https://signnow.com/embedded/editor/test",
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
    request = DocumentEmbeddedEditorLinkPostRequest()
    request.with_document_id("test_doc_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, DocumentEmbeddedEditorLinkPostResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_document_group_embedded_editor_link_post_api_call(mock_api_client):
    """
    Test real API call for creating document group embedded editor link.

    Verifies that:
    - ApiClient can send DocumentGroupEmbeddedEditorLinkPostRequest
    - Response is properly parsed (similar to Java DocumentGroupEmbeddedEditorLinkTest.testPostDocumentGroupEmbedEditorLink)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {
        "data": {
            "link": "https://signnow.com/embedded/group/editor/test",
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
    request = DocumentGroupEmbeddedEditorLinkPostRequest()
    request.with_document_group_id("test_group_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, DocumentGroupEmbeddedEditorLinkPostResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()
