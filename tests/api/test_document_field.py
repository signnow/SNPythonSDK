"""
Tests for DocumentField API.

This module contains tests for document field API including:
- Document prefill operations

These tests verify that document field requests and responses can be properly
created and structured for interaction with the SignNow API.
"""

from signnow.api.documentfield.request import DocumentPrefillPutRequest
from signnow.api.documentfield.response import DocumentPrefillPutResponse


def test_document_prefill_put_request_creation():
    """Test DocumentPrefillPutRequest creation and structure."""
    from signnow.api.documentfield.request.data.field_collection import FieldCollection

    field_collection = FieldCollection()
    request = DocumentPrefillPutRequest(fields=field_collection)
    request.with_document_id("test_doc_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["document_id"] == "test_doc_id"
    payload = request.payload()
    assert "fields" in payload


def test_document_prefill_put_response_structure():
    """Test DocumentPrefillPutResponse data structure."""
    response = DocumentPrefillPutResponse()
    assert response is not None


# ============================================================================
# Real API Call Tests (similar to Java SDK tests)
# ============================================================================


def test_document_prefill_put_api_call(mock_api_client):
    """
    Test real API call for prefilling document fields.

    Verifies that:
    - ApiClient can send DocumentPrefillPutRequest
    - Response is properly parsed (similar to Java DocumentPrefillTest.testPutDocumentPrefill)
    """
    from unittest.mock import MagicMock
    import httpx
    import json
    from signnow.api.documentfield.request.data.field_collection import FieldCollection

    # Mock response data
    mock_response_data = {"status": "success"}

    # Create mock httpx.Response
    mock_response = MagicMock(spec=httpx.Response)
    mock_response.status_code = 200
    mock_response.text = json.dumps(mock_response_data)
    mock_response.content = json.dumps(mock_response_data).encode()
    mock_response.headers = {"Content-Type": "application/json"}
    mock_response.json.return_value = mock_response_data

    # Configure mock client
    mock_api_client._client.request.return_value = mock_response

    # Execute API call
    field_collection = FieldCollection()
    request = DocumentPrefillPutRequest(fields=field_collection)
    request.with_document_id("test_doc_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, DocumentPrefillPutResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()
