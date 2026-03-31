"""
Tests for Document API.

This module contains tests for document API including:
- Document CRUD operations (POST, GET, PUT, DELETE)
- Document download operations
- Document history retrieval
- Document merge and move operations
- Document fields operations

These tests verify that document requests and responses can be properly
created and structured for interaction with the SignNow API.
"""

import tempfile
from pathlib import Path

from signnow.api.document.request import (
    DocumentDeleteRequest,
    DocumentDownloadGetRequest,
    DocumentDownloadLinkPostRequest,
    DocumentGetRequest,
    DocumentHistoryGetRequest,
    DocumentMergePostRequest,
    DocumentMovePostRequest,
    DocumentPostRequest,
    DocumentPutRequest,
    FieldExtractPostRequest,
    FieldsGetRequest,
)
from signnow.api.document.response import (
    DocumentDeleteResponse,
    DocumentDownloadGetResponse,
    DocumentDownloadLinkPostResponse,
    DocumentGetResponse,
    DocumentHistoryGetResponse,
    DocumentMergePostResponse,
    DocumentMovePostResponse,
    DocumentPostResponse,
    DocumentPutResponse,
    FieldExtractPostResponse,
    FieldsGetResponse,
)


def test_document_post_request_creation():
    """
    Test DocumentPostRequest creation and structure.

    Verifies that:
    - DocumentPostRequest can be created with file and parameters
    - Request has correct API endpoint annotation
    - File path is properly handled
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as f:
        f.write(b"test content")
        temp_path = f.name

    try:
        request = DocumentPostRequest(
            file=temp_path,
            name="test_document.pdf",
            check_fields=False,
            save_fields=0,
            make_template=0,
        )

        assert hasattr(request, "__api_endpoint__")
        assert request.uri_params() == {}
        # Payload for multipart/form-data is handled differently
    finally:
        Path(temp_path).unlink()


def test_document_get_request_creation():
    """
    Test DocumentGetRequest creation and structure.

    Verifies that:
    - DocumentGetRequest can be created and configured with document ID
    - Document ID is correctly set in URI parameters
    - Request has correct API endpoint annotation
    """
    request = DocumentGetRequest()
    request.with_document_id("test_doc_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["document_id"] == "test_doc_id"
    assert request.payload() == {}


def test_document_put_request_creation():
    """
    Test DocumentPutRequest creation and structure.

    Verifies that:
    - DocumentPutRequest can be created with document ID and update data
    - Document ID is correctly set in URI parameters
    - Request payload contains update data
    """
    request = DocumentPutRequest(document_name="Updated Document Name")
    request.with_document_id("test_doc_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["document_id"] == "test_doc_id"
    payload = request.payload()
    assert "document_name" in payload
    assert payload["document_name"] == "Updated Document Name"


def test_document_delete_request_creation():
    """
    Test DocumentDeleteRequest creation and structure.

    Verifies that:
    - DocumentDeleteRequest can be created and configured with document ID
    - Document ID is correctly set in URI parameters
    - Request has correct API endpoint annotation
    """
    request = DocumentDeleteRequest()
    request.with_document_id("test_doc_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["document_id"] == "test_doc_id"
    assert request.payload() == {}


def test_document_post_response_structure():
    """
    Test DocumentPostResponse data structure.

    Verifies that:
    - DocumentPostResponse can be instantiated with document data
    - Document ID is correctly stored
    """
    response = DocumentPostResponse(id="test_doc_id")

    assert response.id == "test_doc_id"


def test_document_get_response_structure():
    """
    Test DocumentGetResponse data structure.

    Verifies that:
    - DocumentGetResponse can be instantiated with document data
    - All response fields are correctly stored
    """
    response = DocumentGetResponse(
        id="test_doc_id",
        user_id="test_user_id",
        document_name="Test Document",
        page_count="5",
        created=1234567890,
        updated=1234567890,
    )

    assert response.id == "test_doc_id"
    assert response.user_id == "test_user_id"
    assert response.document_name == "Test Document"
    assert response.page_count == "5"
    assert response.created == 1234567890
    assert response.updated == 1234567890


def test_document_put_response_structure():
    """
    Test DocumentPutResponse data structure.

    Verifies that:
    - DocumentPutResponse can be instantiated
    - Response structure is correct
    """
    response = DocumentPutResponse()

    assert response is not None


def test_document_delete_response_structure():
    """
    Test DocumentDeleteResponse data structure.

    Verifies that:
    - DocumentDeleteResponse can be instantiated
    - Response structure is correct
    """
    response = DocumentDeleteResponse()

    assert response is not None


def test_document_download_get_request_creation():
    """
    Test DocumentDownloadGetRequest creation and structure.

    Verifies that:
    - DocumentDownloadGetRequest can be created and configured with document ID
    - Document ID is correctly set in URI parameters
    - Query parameters (type, with_history) can be set
    - Request has correct API endpoint annotation
    """
    request = DocumentDownloadGetRequest()
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


def test_document_download_link_post_request_creation():
    """
    Test DocumentDownloadLinkPostRequest creation and structure.

    Verifies that:
    - DocumentDownloadLinkPostRequest can be created and configured with document ID
    - Document ID is correctly set in URI parameters
    - Request has correct API endpoint annotation
    """
    request = DocumentDownloadLinkPostRequest()
    request.with_document_id("test_doc_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["document_id"] == "test_doc_id"
    assert request.payload() == {}


def test_document_history_get_request_creation():
    """
    Test DocumentHistoryGetRequest creation and structure.

    Verifies that:
    - DocumentHistoryGetRequest can be created and configured with document ID
    - Document ID is correctly set in URI parameters
    - Request has correct API endpoint annotation
    """
    request = DocumentHistoryGetRequest()
    request.with_document_id("test_doc_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["document_id"] == "test_doc_id"
    assert request.payload() == {}


def test_document_merge_post_request_creation():
    """
    Test DocumentMergePostRequest creation and structure.

    Verifies that:
    - DocumentMergePostRequest can be created with merge data
    - Request payload contains document IDs and name
    - Request has correct API endpoint annotation
    """
    request = DocumentMergePostRequest(
        name="Merged Document",
        document_ids=["doc1", "doc2", "doc3"],
        upload_document=False,
    )

    assert hasattr(request, "__api_endpoint__")
    assert request.uri_params() == {}
    payload = request.payload()
    assert payload["name"] == "Merged Document"
    assert payload["document_ids"] == ["doc1", "doc2", "doc3"]
    assert payload["upload_document"] is False


def test_document_move_post_request_creation():
    """
    Test DocumentMovePostRequest creation and structure.

    Verifies that:
    - DocumentMovePostRequest can be created with folder ID
    - Document ID is correctly set in URI parameters
    - Request payload contains folder ID
    - Request has correct API endpoint annotation
    """
    request = DocumentMovePostRequest(folder_id="test_folder_id")
    request.with_document_id("test_doc_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["document_id"] == "test_doc_id"
    payload = request.payload()
    assert payload["folder_id"] == "test_folder_id"


def test_fields_get_request_creation():
    """
    Test FieldsGetRequest creation and structure.

    Verifies that:
    - FieldsGetRequest can be created and configured with document ID
    - Document ID is correctly set in URI parameters
    - Request has correct API endpoint annotation
    """
    request = FieldsGetRequest()
    request.with_document_id("test_doc_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["document_id"] == "test_doc_id"
    assert request.payload() == {}


def test_field_extract_post_request_creation():
    """
    Test FieldExtractPostRequest creation and structure.

    Verifies that:
    - FieldExtractPostRequest can be created with file and tags
    - Request payload contains file and tags
    - Request has correct API endpoint annotation
    """
    import tempfile

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as f:
        f.write(b"test content")
        temp_path = f.name

    try:
        request = FieldExtractPostRequest(
            file=temp_path,
            tags=[{"field_name": "test_field"}],
            parse_type="text",
        )

        assert hasattr(request, "__api_endpoint__")
        assert request.uri_params() == {}
        payload = request.payload()
        assert "file" in payload
        assert "Tags" in payload
    finally:
        import os

        if os.path.exists(temp_path):
            os.unlink(temp_path)


def test_document_download_get_response_structure():
    """
    Test DocumentDownloadGetResponse data structure.

    Verifies that:
    - DocumentDownloadGetResponse can be instantiated
    - Response structure is correct
    """
    response = DocumentDownloadGetResponse()

    assert response is not None


def test_document_download_link_post_response_structure():
    """
    Test DocumentDownloadLinkPostResponse data structure.

    Verifies that:
    - DocumentDownloadLinkPostResponse can be instantiated with link
    - Link is correctly stored
    """
    response = DocumentDownloadLinkPostResponse(
        link="https://signnow.com/download/test"
    )

    assert response.link == "https://signnow.com/download/test"


def test_document_history_get_response_structure():
    """
    Test DocumentHistoryGetResponse data structure.

    Verifies that:
    - DocumentHistoryGetResponse can be instantiated
    - Response structure is correct
    """
    response = DocumentHistoryGetResponse()

    assert response is not None


def test_document_merge_post_response_structure():
    """
    Test DocumentMergePostResponse data structure.

    Verifies that:
    - DocumentMergePostResponse can be instantiated with document ID
    - Document ID is correctly stored
    """
    response = DocumentMergePostResponse(id="merged_doc_id", name="Merged Document")

    assert response.id == "merged_doc_id"
    assert response.name == "Merged Document"


def test_document_move_post_response_structure():
    """
    Test DocumentMovePostResponse data structure.

    Verifies that:
    - DocumentMovePostResponse can be instantiated
    - Response structure is correct
    """
    response = DocumentMovePostResponse()

    assert response is not None


def test_fields_get_response_structure():
    """
    Test FieldsGetResponse data structure.

    Verifies that:
    - FieldsGetResponse can be instantiated
    - Response structure is correct
    """
    response = FieldsGetResponse()

    assert response is not None


def test_field_extract_post_response_structure():
    """
    Test FieldExtractPostResponse data structure.

    Verifies that:
    - FieldExtractPostResponse can be instantiated with document ID
    - Document ID is correctly stored
    """
    response = FieldExtractPostResponse(id="extracted_doc_id")

    assert response.id == "extracted_doc_id"


# ============================================================================
# Real API Call Tests (similar to Java SDK tests)
# ============================================================================


def test_document_get_api_call(mock_api_client):
    """
    Test real API call for getting document.

    Verifies that:
    - ApiClient can send DocumentGetRequest
    - Response is properly parsed
    - Response contains expected fields (similar to Java DocumentTest.testGetDocument)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data matching Java SDK expectation
    mock_response_data = {
        "id": "test_doc_id",
        "user_id": "test_user_id",
        "document_name": "Test Document",
        "page_count": "5",
        "created": "1234567890",
        "updated": "1234567890",
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
        "version_time": "1234567890",
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

    # Configure mock client to return our mock response
    mock_api_client._client.request.return_value = mock_response

    # Execute API call
    request = DocumentGetRequest()
    request.with_document_id("test_doc_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, DocumentGetResponse)
    assert response.id == "test_doc_id"
    assert response.user_id == "test_user_id"
    assert response.document_name == "Test Document"
    assert response.page_count == "5"
    assert response.created == "1234567890"
    assert response.updated == "1234567890"
    assert response.original_filename == "test.pdf"
    assert response.owner == "owner@example.com"
    assert response.owner_name == "Owner Name"
    assert response.template is False

    # Verify API client was called correctly
    mock_api_client._client.request.assert_called_once()


def test_document_post_api_call(mock_api_client):
    """
    Test real API call for creating document.

    Verifies that:
    - ApiClient can send DocumentPostRequest
    - Response is properly parsed
    - Response contains document ID (similar to Java DocumentTest.testPostDocument)
    """
    from unittest.mock import MagicMock
    import httpx
    import json
    import tempfile

    # Mock response data
    mock_response_data = {"id": "new_doc_id"}

    # Create mock httpx.Response
    mock_response = MagicMock(spec=httpx.Response)
    mock_response.status_code = 200
    mock_response.text = json.dumps(mock_response_data)
    mock_response.content = json.dumps(mock_response_data).encode()
    mock_response.headers = {"Content-Type": "application/json"}

    # Configure mock client
    mock_api_client._client.request.return_value = mock_response

    # Create temporary file for upload
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as f:
        f.write(b"test content")
        temp_path = f.name

    try:
        # Execute API call
        request = DocumentPostRequest(
            file=temp_path,
            name="test_document.pdf",
            check_fields=False,
            save_fields=0,
            make_template=0,
        )
        reply = mock_api_client.send(request)
        response = reply.get_response()

        # Assertions
        assert isinstance(response, DocumentPostResponse)
        assert response.id == "new_doc_id"

        # Verify API client was called
        mock_api_client._client.request.assert_called_once()
    finally:
        import os

        if os.path.exists(temp_path):
            os.unlink(temp_path)


def test_document_put_api_call(mock_api_client):
    """
    Test real API call for updating document.

    Verifies that:
    - ApiClient can send DocumentPutRequest
    - Response is properly parsed (similar to Java DocumentTest.testPutDocument)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {"id": "updated_doc_id"}

    # Create mock httpx.Response
    mock_response = MagicMock(spec=httpx.Response)
    mock_response.status_code = 200
    mock_response.text = json.dumps(mock_response_data)
    mock_response.content = json.dumps(mock_response_data).encode()
    mock_response.headers = {"Content-Type": "application/json"}

    # Configure mock client
    mock_api_client._client.request.return_value = mock_response

    # Execute API call
    request = DocumentPutRequest(document_name="Updated Document Name")
    request.with_document_id("test_doc_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, DocumentPutResponse)
    assert response.id == "updated_doc_id"

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_document_delete_api_call(mock_api_client):
    """
    Test real API call for deleting document.

    Verifies that:
    - ApiClient can send DocumentDeleteRequest
    - Response is properly parsed (similar to Java DocumentTest.testDeleteDocument)
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
    request = DocumentDeleteRequest()
    request.with_document_id("test_doc_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, DocumentDeleteResponse)
    assert response.status == "success"

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_document_download_get_api_call(mock_api_client):
    """
    Test real API call for downloading document.

    Verifies that:
    - ApiClient can send DocumentDownloadGetRequest
    - Response is properly handled (similar to Java DocumentDownloadTest.testGetDocumentDownload)
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
    request = DocumentDownloadGetRequest()
    request.with_document_id("test_doc_id")
    request.with_type("collapsed")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, DocumentDownloadGetResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.stream.assert_called_once()


def test_document_download_link_post_api_call(mock_api_client):
    """
    Test real API call for getting document download link.

    Verifies that:
    - ApiClient can send DocumentDownloadLinkPostRequest
    - Response contains download link (similar to Java DocumentDownloadLinkTest.testPostDocumentDownloadLink)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {"link": "https://signnow.com/download/test"}

    # Create mock httpx.Response
    mock_response = MagicMock(spec=httpx.Response)
    mock_response.status_code = 200
    mock_response.text = json.dumps(mock_response_data)
    mock_response.content = json.dumps(mock_response_data).encode()
    mock_response.headers = {"Content-Type": "application/json"}

    # Configure mock client
    mock_api_client._client.request.return_value = mock_response

    # Execute API call
    request = DocumentDownloadLinkPostRequest()
    request.with_document_id("test_doc_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, DocumentDownloadLinkPostResponse)
    assert response.link == "https://signnow.com/download/test"

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_document_history_get_api_call(mock_api_client):
    """
    Test real API call for getting document history.

    Verifies that:
    - ApiClient can send DocumentHistoryGetRequest
    - Response is properly parsed (similar to Java DocumentHistoryTest.testGetDocumentHistory)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {"history": []}

    # Create mock httpx.Response
    mock_response = MagicMock(spec=httpx.Response)
    mock_response.status_code = 200
    mock_response.text = json.dumps(mock_response_data)
    mock_response.content = json.dumps(mock_response_data).encode()
    mock_response.headers = {"Content-Type": "application/json"}

    # Configure mock client
    mock_api_client._client.request.return_value = mock_response

    # Execute API call
    request = DocumentHistoryGetRequest()
    request.with_document_id("test_doc_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, DocumentHistoryGetResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_document_merge_post_api_call(mock_api_client):
    """
    Test real API call for merging documents.

    Verifies that:
    - ApiClient can send DocumentMergePostRequest
    - Response contains merged document ID (similar to Java DocumentMergeTest.testPostDocumentMerge)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {"id": "merged_doc_id", "name": "Merged Document"}

    # Create mock httpx.Response
    mock_response = MagicMock(spec=httpx.Response)
    mock_response.status_code = 200
    mock_response.text = json.dumps(mock_response_data)
    mock_response.content = json.dumps(mock_response_data).encode()
    mock_response.headers = {"Content-Type": "application/json"}

    # Configure mock client
    mock_api_client._client.request.return_value = mock_response

    # Execute API call
    request = DocumentMergePostRequest(
        name="Merged Document",
        document_ids=["doc1", "doc2", "doc3"],
        upload_document=False,
    )
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, DocumentMergePostResponse)
    assert response.id == "merged_doc_id"
    assert response.name == "Merged Document"

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_document_move_post_api_call(mock_api_client):
    """
    Test real API call for moving document.

    Verifies that:
    - ApiClient can send DocumentMovePostRequest
    - Response is properly parsed (similar to Java DocumentMoveTest.testPostDocumentMove)
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
    request = DocumentMovePostRequest(folder_id="test_folder_id")
    request.with_document_id("test_doc_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, DocumentMovePostResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_fields_get_api_call(mock_api_client):
    """
    Test real API call for getting document fields.

    Verifies that:
    - ApiClient can send FieldsGetRequest
    - Response is properly parsed (similar to Java FieldsTest.testGetFields)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {"fields": []}

    # Create mock httpx.Response
    mock_response = MagicMock(spec=httpx.Response)
    mock_response.status_code = 200
    mock_response.text = json.dumps(mock_response_data)
    mock_response.content = json.dumps(mock_response_data).encode()
    mock_response.headers = {"Content-Type": "application/json"}

    # Configure mock client
    mock_api_client._client.request.return_value = mock_response

    # Execute API call
    request = FieldsGetRequest()
    request.with_document_id("test_doc_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, FieldsGetResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_field_extract_post_api_call(mock_api_client):
    """
    Test real API call for extracting fields from document.

    Verifies that:
    - ApiClient can send FieldExtractPostRequest
    - Response contains extracted document ID (similar to Java FieldExtractTest.testPostFieldExtract)
    """
    from unittest.mock import MagicMock
    import httpx
    import json
    import tempfile

    # Mock response data
    mock_response_data = {"id": "extracted_doc_id"}

    # Create mock httpx.Response
    mock_response = MagicMock(spec=httpx.Response)
    mock_response.status_code = 200
    mock_response.text = json.dumps(mock_response_data)
    mock_response.content = json.dumps(mock_response_data).encode()
    mock_response.headers = {"Content-Type": "application/json"}

    # Configure mock client
    mock_api_client._client.request.return_value = mock_response

    # Create temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as f:
        f.write(b"test content")
        temp_path = f.name

    try:
        # Execute API call
        request = FieldExtractPostRequest(
            file=temp_path,
            tags=[{"field_name": "test_field"}],
            parse_type="text",
        )
        reply = mock_api_client.send(request)
        response = reply.get_response()

        # Assertions
        assert isinstance(response, FieldExtractPostResponse)
        assert response.id == "extracted_doc_id"

        # Verify API client was called
        mock_api_client._client.request.assert_called_once()
    finally:
        import os

        if os.path.exists(temp_path):
            os.unlink(temp_path)
