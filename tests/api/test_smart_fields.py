"""
Tests for SmartFields API.

This module contains tests for smart fields API including:
- Document prefill smart field operations

These tests verify that smart fields requests and responses can be properly
created and structured for interaction with the SignNow API.
"""

from signnow.api.smartfields.request import DocumentPrefillSmartFieldPostRequest
from signnow.api.smartfields.response import DocumentPrefillSmartFieldPostResponse


def test_document_prefill_smart_field_post_request_creation():
    """Test DocumentPrefillSmartFieldPostRequest creation and structure."""
    from signnow.api.smartfields.request.data.data_collection import DataCollection

    data_collection = DataCollection()
    request = DocumentPrefillSmartFieldPostRequest(
        data=data_collection,
        client_timestamp="1234567890",
    )
    request.with_document_id("test_doc_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["document_id"] == "test_doc_id"
    payload = request.payload()
    assert "data" in payload
    assert "client_timestamp" in payload


def test_document_prefill_smart_field_post_response_structure():
    """Test DocumentPrefillSmartFieldPostResponse data structure."""
    response = DocumentPrefillSmartFieldPostResponse()
    assert response is not None


# ============================================================================
# Real API Call Tests (similar to Java SDK tests)
# ============================================================================


def test_document_prefill_smart_field_post_api_call(mock_api_client):
    """
    Test real API call for prefilling smart fields.

    Verifies that:
    - ApiClient can send DocumentPrefillSmartFieldPostRequest
    - Response is properly parsed (similar to Java DocumentPrefillSmartFieldTest.testPostDocumentPrefillSmartField)
    """
    from unittest.mock import MagicMock
    import httpx
    import json
    from signnow.api.smartfields.request.data.data_collection import DataCollection

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
    data_collection = DataCollection()
    request = DocumentPrefillSmartFieldPostRequest(
        data=data_collection,
        client_timestamp="1234567890",
    )
    request.with_document_id("test_doc_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, DocumentPrefillSmartFieldPostResponse)
    assert response.status == "success"

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()
