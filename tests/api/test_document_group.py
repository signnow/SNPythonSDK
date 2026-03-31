"""
Tests for DocumentGroup API.

This module contains tests for document group API including:
- Document group CRUD operations
- Document group recipients operations
- Document group download operations

These tests verify that document group requests and responses can be properly
created and structured for interaction with the SignNow API.
"""

from signnow.api.documentgroup.request import (
    DocumentGroupDeleteRequest,
    DocumentGroupGetRequest,
    DocumentGroupPostRequest,
    DocumentGroupRecipientsGetRequest,
    DocumentGroupRecipientsPutRequest,
    DownloadDocumentGroupPostRequest,
)
from signnow.api.documentgroup.response import (
    DocumentGroupDeleteResponse,
    DocumentGroupGetResponse,
    DocumentGroupPostResponse,
    DocumentGroupRecipientsGetResponse,
    DocumentGroupRecipientsPutResponse,
    DownloadDocumentGroupPostResponse,
)


def test_document_group_post_request_creation():
    """
    Test DocumentGroupPostRequest creation and structure.

    Verifies that:
    - DocumentGroupPostRequest can be created with document IDs and group name
    - Request payload contains document IDs and group name
    - Request has correct API endpoint annotation
    """
    request = DocumentGroupPostRequest(
        document_ids=["doc1", "doc2", "doc3"],
        group_name="Test Group",
    )

    assert hasattr(request, "__api_endpoint__")
    assert request.uri_params() == {}
    payload = request.payload()
    assert payload["document_ids"] == ["doc1", "doc2", "doc3"]
    assert payload["group_name"] == "Test Group"


def test_document_group_get_request_creation():
    """
    Test DocumentGroupGetRequest creation and structure.

    Verifies that:
    - DocumentGroupGetRequest can be created and configured with document group ID
    - Document group ID is correctly set in URI parameters
    - Request has correct API endpoint annotation
    """
    request = DocumentGroupGetRequest()
    request.with_document_group_id("test_group_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["document_group_id"] == "test_group_id"
    assert request.payload() == {}


def test_document_group_delete_request_creation():
    """
    Test DocumentGroupDeleteRequest creation and structure.

    Verifies that:
    - DocumentGroupDeleteRequest can be created and configured with document group ID
    - Document group ID is correctly set in URI parameters
    - Request has correct API endpoint annotation
    """
    request = DocumentGroupDeleteRequest()
    request.with_document_group_id("test_group_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["document_group_id"] == "test_group_id"
    assert request.payload() == {}


def test_document_group_recipients_get_request_creation():
    """
    Test DocumentGroupRecipientsGetRequest creation and structure.

    Verifies that:
    - DocumentGroupRecipientsGetRequest can be created and configured with document group ID
    - Document group ID is correctly set in URI parameters
    - Request has correct API endpoint annotation
    """
    request = DocumentGroupRecipientsGetRequest()
    request.with_document_group_id("test_group_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["document_group_id"] == "test_group_id"
    assert request.payload() == {}


def test_document_group_recipients_put_request_creation():
    """
    Test DocumentGroupRecipientsPutRequest creation and structure.

    Verifies that:
    - DocumentGroupRecipientsPutRequest can be created with recipients data
    - Document group ID is correctly set in URI parameters
    - Request payload contains recipients information
    - Request has correct API endpoint annotation
    """
    request = DocumentGroupRecipientsPutRequest(
        recipients=[{"email": "test@example.com"}]
    )
    request.with_document_group_id("test_group_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["document_group_id"] == "test_group_id"
    payload = request.payload()
    assert "recipients" in payload


def test_document_group_recipients_put_request_with_order_type():
    """
    Test DocumentGroupRecipientsPutRequest with order_type, expiration, and reminder.
    """
    request = DocumentGroupRecipientsPutRequest(
        recipients=[{"email": "test@example.com"}],
        general_expiration_days=30,
        general_reminder={
            "remind_before": 5,
            "remind_repeat": 3,
            "remind_after": 7,
        },
        order_type="recipient_order",
    )
    request.with_document_group_id("test_group_id")

    payload = request.payload()
    assert payload["order_type"] == "recipient_order"
    assert payload["general_expiration_days"] == 30
    assert payload["general_reminder"]["remind_before"] == 5


def test_document_group_recipients_put_request_order_type_omitted():
    """
    Test that order_type is not in payload when not specified.
    """
    request = DocumentGroupRecipientsPutRequest(
        recipients=[{"email": "test@example.com"}],
    )
    payload = request.payload()
    assert "order_type" not in payload


def test_download_document_group_post_request_creation():
    """
    Test DownloadDocumentGroupPostRequest creation and structure.

    Verifies that:
    - DownloadDocumentGroupPostRequest can be created and configured with document group ID
    - Document group ID is correctly set in URI parameters
    - Request has correct API endpoint annotation
    """
    request = DownloadDocumentGroupPostRequest()
    request.with_document_group_id("test_group_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["document_group_id"] == "test_group_id"
    assert request.payload() == {}


def test_document_group_post_response_structure():
    """
    Test DocumentGroupPostResponse data structure.

    Verifies that:
    - DocumentGroupPostResponse can be instantiated with document group data
    - Document group ID is correctly stored
    """
    response = DocumentGroupPostResponse(id="test_group_id")

    assert response.id == "test_group_id"


def test_document_group_get_response_structure():
    """
    Test DocumentGroupGetResponse data structure.

    Verifies that:
    - DocumentGroupGetResponse can be instantiated with document group data
    - All response fields are correctly stored
    """
    response = DocumentGroupGetResponse(
        id="test_group_id",
        group_name="Test Group",
    )

    assert response.id == "test_group_id"
    assert response.group_name == "Test Group"
    assert response.order_type is None


def test_document_group_get_response_with_order_type():
    """
    Test DocumentGroupGetResponse with order_type field.
    """
    response = DocumentGroupGetResponse(
        id="test_group_id",
        group_name="Test Group",
        order_type="recipient_order",
    )

    assert response.order_type == "recipient_order"


def test_document_group_delete_response_structure():
    """
    Test DocumentGroupDeleteResponse data structure.

    Verifies that:
    - DocumentGroupDeleteResponse can be instantiated
    - Response structure is correct
    """
    response = DocumentGroupDeleteResponse(status="success")

    assert response is not None


def test_document_group_recipients_get_response_structure():
    """
    Test DocumentGroupRecipientsGetResponse data structure.

    Verifies that:
    - DocumentGroupRecipientsGetResponse can be instantiated
    - Response structure is correct
    """
    response = DocumentGroupRecipientsGetResponse()

    assert response is not None


def test_document_group_recipients_get_response_with_expiration_and_reminder():
    """
    Test DocumentGroupRecipientsGetResponse with general_expiration_days and general_reminder
    inside the data dict, matching the actual API response structure.
    """
    response = DocumentGroupRecipientsGetResponse(
        data={
            "recipients": [],
            "general_expiration_days": 30,
            "general_reminder": {
                "remind_before": 5,
                "remind_repeat": 3,
                "remind_after": 7,
            },
            "order_type": "at_the_same_time",
        }
    )

    assert response.data is not None
    assert response.data["general_expiration_days"] == 30
    assert response.data["general_reminder"]["remind_before"] == 5
    assert response.data["general_reminder"]["remind_repeat"] == 3
    assert response.data["general_reminder"]["remind_after"] == 7
    assert response.data["order_type"] == "at_the_same_time"


def test_document_group_recipients_get_response_defaults_none():
    """
    Test that data defaults to None when not provided.
    """
    response = DocumentGroupRecipientsGetResponse()
    assert response.data is None


def test_document_group_recipients_get_response_full_structure():
    """
    Test the full response structure matching the actual API response.
    """
    response = DocumentGroupRecipientsGetResponse(
        data={
            "recipients": [
                {
                    "name": "Contract Preparer",
                    "email": None,
                    "phone_invite": None,
                    "email_group": {"id": None},
                    "order": 1,
                    "attributes": {},
                    "documents": [
                        {
                            "id": "a4a64df3f20f4962bc4308513cc50bb802f06ccb",
                            "role": "Contract Preparer",
                            "action": "sign",
                        }
                    ],
                }
            ],
            "unmapped_documents": [],
            "allowed_unmapped_sign_documents": [],
            "cc": [],
            "order_type": None,
            "general_expiration_days": None,
            "general_reminder": None,
        }
    )

    assert response.data is not None
    assert len(response.data["recipients"]) == 1
    assert response.data["recipients"][0]["name"] == "Contract Preparer"
    assert response.data["recipients"][0]["order"] == 1
    assert response.data["recipients"][0]["documents"][0]["role"] == "Contract Preparer"
    assert response.data["recipients"][0]["documents"][0]["action"] == "sign"
    assert response.data["recipients"][0]["email_group"]["id"] is None
    assert response.data["unmapped_documents"] == []
    assert response.data["cc"] == []
    assert response.data["general_expiration_days"] is None
    assert response.data["general_reminder"] is None


def test_document_group_recipients_put_response_structure():
    """
    Test DocumentGroupRecipientsPutResponse data structure.

    Verifies that:
    - DocumentGroupRecipientsPutResponse can be instantiated
    - Response structure is correct
    """
    response = DocumentGroupRecipientsPutResponse()

    assert response is not None


def test_download_document_group_post_response_structure():
    """
    Test DownloadDocumentGroupPostResponse data structure.

    Verifies that:
    - DownloadDocumentGroupPostResponse can be instantiated
    - Response structure is correct
    """
    response = DownloadDocumentGroupPostResponse()

    assert response is not None


# ============================================================================
# Real API Call Tests (similar to Java SDK tests)
# ============================================================================


def test_document_group_post_api_call(mock_api_client):
    """
    Test real API call for creating document group.

    Verifies that:
    - ApiClient can send DocumentGroupPostRequest
    - Response is properly parsed (similar to Java DocumentGroupTest.testPostDocumentGroup)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {"id": "group_id"}

    # Create mock httpx.Response
    mock_response = MagicMock(spec=httpx.Response)
    mock_response.status_code = 200
    mock_response.text = json.dumps(mock_response_data)
    mock_response.content = json.dumps(mock_response_data).encode()
    mock_response.headers = {"Content-Type": "application/json"}

    # Configure mock client
    mock_api_client._client.request.return_value = mock_response

    # Execute API call
    request = DocumentGroupPostRequest(
        document_ids=["doc1", "doc2", "doc3"],
        group_name="Test Group",
    )
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, DocumentGroupPostResponse)
    assert response.id == "group_id"

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_document_group_get_api_call(mock_api_client):
    """
    Test real API call for getting document group.

    Verifies that:
    - ApiClient can send DocumentGroupGetRequest
    - Response is properly parsed (similar to Java DocumentGroupTest.testGetDocumentGroup)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {
        "id": "group_id",
        "group_name": "Test Group",
        "invite_id": "invite_id",
        "documents": [],
        "originator_organization_settings": None,
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
    request = DocumentGroupGetRequest()
    request.with_document_group_id("group_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, DocumentGroupGetResponse)
    assert response.id == "group_id"
    assert response.group_name == "Test Group"
    assert response.invite_id == "invite_id"

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_document_group_delete_api_call(mock_api_client):
    """
    Test real API call for deleting document group.

    Verifies that:
    - ApiClient can send DocumentGroupDeleteRequest
    - Response is properly parsed (similar to Java DocumentGroupTest.testDeleteDocumentGroup)
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
    request = DocumentGroupDeleteRequest()
    request.with_document_group_id("group_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, DocumentGroupDeleteResponse)
    assert response.status == "success"

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_document_group_recipients_get_api_call(mock_api_client):
    """
    Test API call for getting document group recipients.

    Verifies that:
    - ApiClient can send DocumentGroupRecipientsGetRequest
    - Response is properly parsed with the full structure including
      general_expiration_days and general_reminder inside data
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data matching the actual API response
    mock_response_data = {
        "data": {
            "recipients": [
                {
                    "name": "Contract Preparer",
                    "email": None,
                    "phone_invite": None,
                    "email_group": {"id": None},
                    "order": 1,
                    "attributes": {},
                    "documents": [
                        {
                            "id": "a4a64df3f20f4962bc4308513cc50bb802f06ccb",
                            "role": "Contract Preparer",
                            "action": "sign",
                        }
                    ],
                },
                {
                    "name": "Professor",
                    "email": None,
                    "phone_invite": None,
                    "email_group": {"id": None},
                    "order": 1,
                    "attributes": {},
                    "documents": [
                        {
                            "id": "a4a64df3f20f4962bc4308513cc50bb802f06ccb",
                            "role": "Professor",
                            "action": "sign",
                        }
                    ],
                },
            ],
            "unmapped_documents": [],
            "allowed_unmapped_sign_documents": [],
            "cc": [],
            "order_type": None,
            "general_expiration_days": None,
            "general_reminder": None,
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
    request = DocumentGroupRecipientsGetRequest()
    request.with_document_group_id("group_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, DocumentGroupRecipientsGetResponse)
    assert response.data is not None
    assert len(response.data["recipients"]) == 2
    assert response.data["recipients"][0]["name"] == "Contract Preparer"
    assert response.data["recipients"][0]["order"] == 1
    assert response.data["recipients"][0]["documents"][0]["action"] == "sign"
    assert response.data["recipients"][1]["name"] == "Professor"
    assert response.data["unmapped_documents"] == []
    assert response.data["cc"] == []
    assert response.data["general_expiration_days"] is None
    assert response.data["general_reminder"] is None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_document_group_recipients_get_api_call_with_reminder(mock_api_client):
    """
    Test API call for getting document group recipients with expiration and reminder set.
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    mock_response_data = {
        "data": {
            "recipients": [
                {
                    "name": "Signer",
                    "email": "signer@example.com",
                    "phone_invite": None,
                    "email_group": {"id": None},
                    "order": 1,
                    "attributes": {},
                    "documents": [{"id": "doc123", "role": "Signer", "action": "sign"}],
                }
            ],
            "unmapped_documents": [],
            "allowed_unmapped_sign_documents": [],
            "cc": [],
            "order_type": None,
            "general_expiration_days": 30,
            "general_reminder": {
                "remind_before": 5,
                "remind_repeat": 3,
                "remind_after": 7,
            },
        }
    }

    mock_response = MagicMock(spec=httpx.Response)
    mock_response.status_code = 200
    mock_response.text = json.dumps(mock_response_data)
    mock_response.content = json.dumps(mock_response_data).encode()
    mock_response.headers = {"Content-Type": "application/json"}

    mock_api_client._client.request.return_value = mock_response

    request = DocumentGroupRecipientsGetRequest()
    request.with_document_group_id("group_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    assert isinstance(response, DocumentGroupRecipientsGetResponse)
    assert response.data["general_expiration_days"] == 30
    assert response.data["general_reminder"]["remind_before"] == 5
    assert response.data["general_reminder"]["remind_repeat"] == 3
    assert response.data["general_reminder"]["remind_after"] == 7
    assert response.data["recipients"][0]["email"] == "signer@example.com"

    mock_api_client._client.request.assert_called_once()


def test_document_group_recipients_put_api_call(mock_api_client):
    """
    Test real API call for updating document group recipients.

    Verifies that:
    - ApiClient can send DocumentGroupRecipientsPutRequest
    - Response is properly parsed
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
    request = DocumentGroupRecipientsPutRequest(recipients=[])
    request.with_document_group_id("group_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, DocumentGroupRecipientsPutResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_download_document_group_post_api_call(mock_api_client):
    """
    Test real API call for downloading document group.

    Verifies that:
    - ApiClient can send DownloadDocumentGroupPostRequest
    - Response is properly parsed (similar to Java DownloadDocumentGroupTest.testPostDownloadDocumentGroup)
    """
    from unittest.mock import MagicMock

    # Create mock streaming response
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.headers = {
        "Content-Type": "application/zip",
        "Content-Disposition": 'attachment; filename="document_group.zip"',
    }
    mock_response.iter_bytes.return_value = [b"PK\x03\x04test zip content"]

    # Configure mock client stream context manager
    mock_api_client._client.stream.return_value.__enter__ = MagicMock(
        return_value=mock_response
    )
    mock_api_client._client.stream.return_value.__exit__ = MagicMock(return_value=False)

    # Execute API call
    request = DownloadDocumentGroupPostRequest(
        type="collapsed",
        with_history="yes",
        document_order=[],
    )
    request.with_document_group_id("group_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, DownloadDocumentGroupPostResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.stream.assert_called_once()
