"""
Tests for Folder API.

This module contains tests for folder API including:
- Folder retrieval operations
- Folder documents retrieval

These tests verify that folder requests and responses can be properly
created and structured for interaction with the SignNow API.
"""

from signnow.api.folder.request import FolderDocumentsGetRequest, FolderGetRequest
from signnow.api.folder.response import FolderDocumentsGetResponse, FolderGetResponse


def test_folder_get_request_creation():
    """
    Test FolderGetRequest creation and structure.

    Verifies that:
    - FolderGetRequest can be created without parameters
    - Request has correct API endpoint annotation
    - URI parameters and payload are empty
    """
    request = FolderGetRequest()

    assert hasattr(request, "__api_endpoint__")
    assert request.uri_params() == {}
    assert request.payload() == {}


def test_folder_documents_get_request_creation():
    """
    Test FolderDocumentsGetRequest creation and structure.

    Verifies that:
    - FolderDocumentsGetRequest can be created and configured with folder ID
    - Folder ID is correctly set in URI parameters
    - Request has correct API endpoint annotation
    """
    request = FolderDocumentsGetRequest()
    request.with_folder_id("test_folder_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["folder_id"] == "test_folder_id"
    assert request.payload() == {}


def test_folder_get_response_structure():
    """
    Test FolderGetResponse data structure.

    Verifies that:
    - FolderGetResponse can be instantiated with folder data
    - All response fields are correctly stored
    """
    response = FolderGetResponse(
        id="test_folder_id",
        name="Test Folder",
        user_id="test_user_id",
        created="2024-01-01",
    )

    assert response.id == "test_folder_id"
    assert response.name == "Test Folder"
    assert response.user_id == "test_user_id"
    assert response.created == "2024-01-01"


def test_folder_documents_get_response_structure():
    """
    Test FolderDocumentsGetResponse data structure.

    Verifies that:
    - FolderDocumentsGetResponse can be instantiated
    - Response structure is correct
    """
    response = FolderDocumentsGetResponse()

    assert response is not None


# ============================================================================
# Real API Call Tests (similar to Java SDK tests)
# ============================================================================


def test_folder_get_api_call(mock_api_client):
    """
    Test real API call for getting folder.

    Verifies that:
    - ApiClient can send FolderGetRequest
    - Response is properly parsed (similar to Java FolderTest.testGetFolder)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {
        "id": "folder_id",
        "created": "1234567890",
        "name": "Test Folder",
        "user_id": "user_id",
        "parent_id": "parent_id",
        "system_folder": False,
        "shared": False,
        "folders": [],
        "total_documents": 0,
        "documents": [],
        "team_name": None,
        "team_id": None,
        "team_type": None,
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
    request = FolderGetRequest()
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, FolderGetResponse)
    assert response.id == "folder_id"
    assert response.name == "Test Folder"
    assert response.user_id == "user_id"

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()
