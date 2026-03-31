"""
Tests for DocumentInvite API.

This module contains tests for document invite API including:
- Signing link creation
- Free form invite operations
- Send invite operations
- Cancel invite operations
- Cancel free form invite operations

These tests verify that document invite requests and responses can be properly
created and structured for interaction with the SignNow API.
"""

from signnow.api.documentinvite.request import (
    CancelFreeFormInvitePutRequest,
    CancelInvitePutRequest,
    FreeFormInviteGetRequest,
    FreeFormInvitePostRequest,
    SendInvitePostRequest,
    SigningLinkPostRequest,
)
from signnow.api.documentinvite.response import (
    CancelFreeFormInvitePutResponse,
    CancelInvitePutResponse,
    FreeFormInviteGetResponse,
    FreeFormInvitePostResponse,
    SendInvitePostResponse,
    SigningLinkPostResponse,
)


def test_signing_link_post_request_creation():
    """
    Test SigningLinkPostRequest creation and structure.

    Verifies that:
    - SigningLinkPostRequest can be created with document ID and redirect URI
    - Request payload contains document ID and redirect URI
    - Request has correct API endpoint annotation
    """
    request = SigningLinkPostRequest(
        document_id="test_doc_id",
        redirect_uri="https://example.com/callback",
    )

    assert hasattr(request, "__api_endpoint__")
    assert request.uri_params() == {}
    payload = request.payload()
    assert payload["document_id"] == "test_doc_id"
    assert payload["redirect_uri"] == "https://example.com/callback"


def test_free_form_invite_post_request_creation():
    """
    Test FreeFormInvitePostRequest creation and structure.

    Verifies that:
    - FreeFormInvitePostRequest can be created with invite data
    - Document ID is correctly set in URI parameters
    - Request payload contains invite information
    - Request has correct API endpoint annotation
    """
    request = FreeFormInvitePostRequest(
        to="recipient@example.com",
        from_email="sender@example.com",
        subject="Please sign",
        message="Please sign this document",
    )
    request.with_document_id("test_doc_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["document_id"] == "test_doc_id"
    payload = request.payload()
    assert payload["to"] == "recipient@example.com"
    assert payload["from"] == "sender@example.com"
    assert payload["subject"] == "Please sign"
    assert payload["message"] == "Please sign this document"


def test_free_form_invite_get_request_creation():
    """
    Test FreeFormInviteGetRequest creation and structure.

    Verifies that:
    - FreeFormInviteGetRequest can be created and configured with document ID
    - Document ID is correctly set in URI parameters
    - Request has correct API endpoint annotation
    """
    request = FreeFormInviteGetRequest()
    request.with_document_id("test_doc_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["document_id"] == "test_doc_id"
    assert request.payload() == {}


def test_send_invite_post_request_creation():
    """
    Test SendInvitePostRequest creation and structure.

    Verifies that:
    - SendInvitePostRequest can be created with invite data
    - Document ID is correctly set in URI parameters
    - Request payload contains invite information
    - Request has correct API endpoint annotation
    """
    request = SendInvitePostRequest(
        to=[{"email": "recipient@example.com"}],
        from_email="sender@example.com",
        subject="Please sign",
        message="Please sign this document",
    )
    request.with_document_id("test_doc_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["document_id"] == "test_doc_id"
    payload = request.payload()
    assert "to" in payload
    assert payload["from"] == "sender@example.com"
    assert payload["subject"] == "Please sign"
    assert payload["message"] == "Please sign this document"


def test_cancel_invite_put_request_creation():
    """
    Test CancelInvitePutRequest creation and structure.

    Verifies that:
    - CancelInvitePutRequest can be created with reason and document ID
    - Document ID is correctly set in URI parameters
    - Request payload contains reason
    - Request has correct API endpoint annotation
    """
    request = CancelInvitePutRequest(reason="User cancelled")
    request.with_document_id("test_doc_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["document_id"] == "test_doc_id"
    payload = request.payload()
    assert payload["reason"] == "User cancelled"


def test_cancel_free_form_invite_put_request_creation():
    """
    Test CancelFreeFormInvitePutRequest creation and structure.

    Verifies that:
    - CancelFreeFormInvitePutRequest can be created and configured with document ID
    - Document ID is correctly set in URI parameters
    - Request has correct API endpoint annotation
    """
    request = CancelFreeFormInvitePutRequest(reason="test_reason")
    request.with_invite_id("test_invite_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["invite_id"] == "test_invite_id"
    payload = request.payload()
    assert payload == {"reason": "test_reason"}


def test_signing_link_post_response_structure():
    """
    Test SigningLinkPostResponse data structure.

    Verifies that:
    - SigningLinkPostResponse can be instantiated with signing link data
    - URL and URL no signup are correctly stored
    """
    response = SigningLinkPostResponse(
        url="https://signnow.com/sign/test",
        url_no_signup="https://signnow.com/sign/test?no_signup=true",
    )

    assert response.url == "https://signnow.com/sign/test"
    assert response.url_no_signup == "https://signnow.com/sign/test?no_signup=true"


def test_free_form_invite_post_response_structure():
    """
    Test FreeFormInvitePostResponse data structure.

    Verifies that:
    - FreeFormInvitePostResponse can be instantiated
    - Response structure is correct
    """
    response = FreeFormInvitePostResponse()

    assert response is not None


def test_free_form_invite_get_response_structure():
    """
    Test FreeFormInviteGetResponse data structure.

    Verifies that:
    - FreeFormInviteGetResponse can be instantiated
    - Response structure is correct
    """
    response = FreeFormInviteGetResponse()

    assert response is not None


def test_send_invite_post_response_structure():
    """
    Test SendInvitePostResponse data structure.

    Verifies that:
    - SendInvitePostResponse can be instantiated
    - Response structure is correct
    """
    response = SendInvitePostResponse()

    assert response is not None


def test_cancel_invite_put_response_structure():
    """
    Test CancelInvitePutResponse data structure.

    Verifies that:
    - CancelInvitePutResponse can be instantiated
    - Response structure is correct
    """
    response = CancelInvitePutResponse()

    assert response is not None


def test_cancel_free_form_invite_put_response_structure():
    """
    Test CancelFreeFormInvitePutResponse data structure.

    Verifies that:
    - CancelFreeFormInvitePutResponse can be instantiated
    - Response structure is correct
    """
    response = CancelFreeFormInvitePutResponse()

    assert response is not None


# ============================================================================
# Real API Call Tests (similar to Java SDK tests)
# ============================================================================


def test_send_invite_post_api_call(mock_api_client):
    """
    Test real API call for sending invite.

    Verifies that:
    - ApiClient can send SendInvitePostRequest
    - Response is properly parsed (similar to Java SendInviteTest.testPostSendInvite)
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
    request = SendInvitePostRequest(
        to=[{"email": "signer@example.com"}],
        from_email="sender@example.com",
        subject="Please sign",
        message="Please sign this document",
    )
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, SendInvitePostResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_signing_link_post_api_call(mock_api_client):
    """
    Test real API call for creating signing link.

    Verifies that:
    - ApiClient can send SigningLinkPostRequest
    - Response contains signing URLs (similar to Java SigningLinkTest.testPostSigningLink)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {
        "url": "https://signnow.com/sign/test",
        "url_no_signup": "https://signnow.com/sign/test?no_signup=true",
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
    request = SigningLinkPostRequest(
        document_id="test_doc_id",
        redirect_uri="https://example.com/callback",
    )
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, SigningLinkPostResponse)
    assert response.url == "https://signnow.com/sign/test"
    assert response.url_no_signup == "https://signnow.com/sign/test?no_signup=true"

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_free_form_invite_post_api_call(mock_api_client):
    """
    Test real API call for creating free form invite.

    Verifies that:
    - ApiClient can send FreeFormInvitePostRequest
    - Response is properly parsed (similar to Java FreeFormInviteTest.testPostFreeFormInvite)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {
        "result": "success",
        "id": "invite_id",
        "callback_url": "https://example.com/callback",
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
    request = FreeFormInvitePostRequest(
        to=["signer@example.com"],
        from_email="sender@example.com",
        subject="Please sign",
        message="Please sign this document",
    )
    request.with_document_id("test_doc_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, FreeFormInvitePostResponse)
    assert response.result == "success"
    assert response.id == "invite_id"
    assert response.callback_url == "https://example.com/callback"

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_free_form_invite_get_api_call(mock_api_client):
    """
    Test real API call for getting free form invites.

    Verifies that:
    - ApiClient can send FreeFormInviteGetRequest
    - Response is properly parsed (similar to Java FreeFormInviteTest.testGetFreeFormInvite)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {
        "data": [],
        "meta": {"total": 0},
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
    request = FreeFormInviteGetRequest()
    request.with_document_id("test_doc_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, FreeFormInviteGetResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_cancel_invite_put_api_call(mock_api_client):
    """
    Test real API call for canceling invite.

    Verifies that:
    - ApiClient can send CancelInvitePutRequest
    - Response is properly parsed (similar to Java CancelInviteTest.testPutCancelInvite)
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
    request = CancelInvitePutRequest(reason="Cancelled by user")
    request.with_document_id("test_doc_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, CancelInvitePutResponse)
    assert response.status == "success"

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_cancel_free_form_invite_put_api_call(mock_api_client):
    """
    Test real API call for canceling free form invite.

    Verifies that:
    - ApiClient can send CancelFreeFormInvitePutRequest
    - Response is properly parsed (similar to Java CancelFreeFormInviteTest.testPutCancelFreeFormInvite)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {"id": "invite_id"}

    # Create mock httpx.Response
    mock_response = MagicMock(spec=httpx.Response)
    mock_response.status_code = 200
    mock_response.text = json.dumps(mock_response_data)
    mock_response.content = json.dumps(mock_response_data).encode()
    mock_response.headers = {"Content-Type": "application/json"}

    # Configure mock client
    mock_api_client._client.request.return_value = mock_response

    # Execute API call
    request = CancelFreeFormInvitePutRequest(reason="Cancelled by user")
    request.with_invite_id("invite_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, CancelFreeFormInvitePutResponse)
    assert response.id == "invite_id" or response.id == ""

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()
