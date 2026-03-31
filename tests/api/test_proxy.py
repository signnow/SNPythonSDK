"""
Tests for Proxy API.

This module contains tests for proxy API including:
- Proxy JSON request operations
- Proxy file request operations

These tests verify that proxy requests and responses can be properly
created and structured for interaction with the SignNow API.
"""

from __future__ import annotations

from typing import Optional

from signnow.api.proxy.response import ProxyFileResponse, ProxyJsonResponse
from signnow.core.request import RequestInterface, api_endpoint


@api_endpoint(
    name="proxy",
    url="/document/{document_id}",
    method="get",
    auth="bearer",
    namespace="proxy",
    entity="proxy",
    content_type="application/json",
)
class CustomProxyJsonRequest(RequestInterface):
    """Custom proxy request for JSON responses."""

    def __init__(self):
        """Initializes a new CustomProxyJsonRequest."""
        self._uri_params: dict[str, str] = {}

    def with_document_id(self, document_id: str) -> "CustomProxyJsonRequest":
        """Adds document ID to URI parameters."""
        self._uri_params["document_id"] = document_id
        return self

    def uri_params(self) -> dict[str, str]:
        """Returns URI parameters."""
        return dict(self._uri_params)

    def payload(self) -> dict[str, str]:
        """Returns empty payload."""
        return {}


@api_endpoint(
    name="proxy",
    url="/document/{document_id}/download",
    method="get",
    auth="bearer",
    namespace="proxy",
    entity="proxy",
    content_type="application/pdf",
)
class CustomProxyFileRequest(RequestInterface):
    """Custom proxy request for file responses."""

    def __init__(self):
        """Initializes a new CustomProxyFileRequest."""
        self._uri_params: dict[str, str] = {}
        self._query_params: dict[str, str] = {}

    def with_document_id(self, document_id: str) -> "CustomProxyFileRequest":
        """Adds document ID to URI parameters."""
        self._uri_params["document_id"] = document_id
        return self

    def with_type(self, type: str) -> "CustomProxyFileRequest":
        """Adds type to query parameters."""
        self._query_params["type"] = type
        return self

    def with_history(self, with_history: str) -> "CustomProxyFileRequest":
        """Adds with_history to query parameters."""
        self._query_params["with_history"] = with_history
        return self

    def uri_params(self) -> dict[str, str]:
        """Returns URI parameters."""
        return dict(self._uri_params)

    def query_params(self) -> Optional[dict[str, str]]:
        """Returns query parameters."""
        return dict(self._query_params) if self._query_params else None

    def payload(self) -> dict[str, str]:
        """Returns empty payload."""
        return {}


def test_proxy_json_request_creation():
    """
    Test CustomProxyJsonRequest creation and structure.

    Verifies that:
    - CustomProxyJsonRequest can be created and configured with document ID
    - Document ID is correctly set in URI parameters
    - Request has correct API endpoint annotation with proxy namespace
    """
    request = CustomProxyJsonRequest()
    request.with_document_id("test_doc_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["document_id"] == "test_doc_id"
    assert request.payload() == {}


def test_proxy_file_request_creation():
    """
    Test CustomProxyFileRequest creation and structure.

    Verifies that:
    - CustomProxyFileRequest can be created and configured with document ID
    - Document ID is correctly set in URI parameters
    - Query parameters (type, with_history) can be set
    - Request has correct API endpoint annotation with proxy namespace
    """
    request = CustomProxyFileRequest()
    request.with_document_id("test_doc_id")
    request.with_type("collapsed")
    request.with_history("yes")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["document_id"] == "test_doc_id"
    query_params = request.query_params()
    assert query_params["type"] == "collapsed"
    assert query_params["with_history"] == "yes"
    assert request.payload() == {}


def test_proxy_json_response_structure():
    """
    Test ProxyJsonResponse data structure.

    Verifies that:
    - ProxyJsonResponse can be instantiated with raw JSON
    - Raw JSON is correctly stored and retrieved
    """
    response = ProxyJsonResponse(raw_json={"id": "test_id", "name": "test"})

    assert response.raw_json == {"id": "test_id", "name": "test"}
    assert response.get_raw_json() == {"id": "test_id", "name": "test"}


def test_proxy_file_response_structure():
    """
    Test ProxyFileResponse data structure.

    Verifies that:
    - ProxyFileResponse can be instantiated with file path
    - File path is correctly stored and retrieved as Path object
    """
    response = ProxyFileResponse(file_path="/tmp/test_file.pdf")

    assert response.file_path == "/tmp/test_file.pdf"
    assert response.get_file() is not None
    assert str(response.get_file()) == "/tmp/test_file.pdf"


# ============================================================================
# Real API Call Tests (similar to Java SDK tests)
# ============================================================================


def test_proxy_json_api_call(mock_api_client):
    """
    Test real API call for proxy JSON request.

    Verifies that:
    - ApiClient can send CustomProxyJsonRequest
    - Response is properly parsed as ProxyJsonResponse (similar to Java ProxyJsonTest.testCustomProxyRequest)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {
        "id": "test_doc_id",
        "user_id": "test_user_id",
        "document_name": "Test Document",
        "page_count": "5",
        "created": 1234567890,
        "updated": 1234567890,
        "original_filename": "test.pdf",
        "origin_user_id": "origin_user_id",
        "origin_document_id": "origin_doc_id",
        "owner": "owner@example.com",
        "owner_name": "Owner Name",
        "is_template": False,
        "parent_id": "parent_id",
        "recently_used": False,
        "originator_logo": None,
        "pages": [],
        "default_folder": "default_folder_id",
        "entity_labels": [],
        "version_time": 1234567890,
        "routing_details": None,
        "thumbnail": None,
        "signatures": [],
        "tags": [],
        "fields": [],
        "roles": [],
        "viewer_roles": [],
        "field_invites": [],
        "viewer_field_invites": [],
        "signing_session_settings": None,
        "enumeration_options": None,
        "payments": None,
        "integrations": [],
        "integration_objects": [],
        "exported_to": [],
        "radiobuttons": [],
        "seals": [],
        "checks": [],
        "texts": [],
        "lines": [],
        "attachments": [],
        "hyperlinks": [],
        "requests": [],
        "inserts": [],
        "fields_data": [],
        "field_validators": [],
        "originator_organization_settings": None,
        "document_group_info": None,
        "document_group_template_info": None,
        "settings": None,
        "share_info": None,
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
    request = CustomProxyJsonRequest()
    request.with_document_id("test_doc_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, ProxyJsonResponse)
    assert response is not None
    assert response.raw_json is not None
    assert response.raw_json["id"] == "test_doc_id"

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_proxy_file_api_call(mock_api_client):
    """
    Test real API call for proxy file request.

    Verifies that:
    - ApiClient can send CustomProxyFileRequest
    - Response is properly parsed as ProxyFileResponse (similar to Java ProxyFileTest.testProxyFile)
    """
    from unittest.mock import MagicMock

    # Create mock streaming response
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.headers = {
        "Content-Type": "application/pdf",
        "Content-Disposition": 'attachment; filename="test.pdf"',
    }
    mock_response.iter_bytes.return_value = [b"%PDF-1.4\n%test content"]

    # Configure mock client stream context manager
    mock_api_client._client.stream.return_value.__enter__ = MagicMock(
        return_value=mock_response
    )
    mock_api_client._client.stream.return_value.__exit__ = MagicMock(return_value=False)

    # Execute API call
    request = CustomProxyFileRequest()
    request.with_document_id("test_doc_id")
    request.with_type("collapsed")
    request.with_history("yes")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, ProxyFileResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.stream.assert_called_once()
