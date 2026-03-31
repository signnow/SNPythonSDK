"""
Tests for DocumentGroupTemplate API.

This module contains tests for document group template API including:
- Document group template creation
- Document group template recipients operations (GET, PUT)
- Reminder and expiration fields

These tests verify that document group template requests and responses can be
properly created and structured for interaction with the SignNow API.
"""

from signnow.api.documentgrouptemplate.request import (
    DocumentGroupTemplateRecipientsGetRequest,
    DocumentGroupTemplateRecipientsPutRequest,
)
from signnow.api.documentgrouptemplate.response import (
    DocumentGroupTemplateRecipientsGetResponse,
    DocumentGroupTemplateRecipientsPutResponse,
)

# ============================================================================
# Request Tests
# ============================================================================


def test_document_group_template_recipients_get_request_creation():
    """
    Test DocumentGroupTemplateRecipientsGetRequest creation and structure.
    """
    request = DocumentGroupTemplateRecipientsGetRequest()
    request.with_template_group_id("tpl_group_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["template_group_id"] == "tpl_group_id"
    assert request.payload() == {}


def test_document_group_template_recipients_get_request_endpoint():
    """
    Test that the GET request has the correct API endpoint configuration.
    """
    request = DocumentGroupTemplateRecipientsGetRequest()
    endpoint = request.__api_endpoint__

    assert endpoint.url == "/v2/document-group-templates/{template_group_id}/recipients"
    assert endpoint.method == "get"
    assert endpoint.auth == "bearer"
    assert endpoint.namespace == "documentGroupTemplate"
    assert endpoint.entity == "documentGroupTemplateRecipients"


def test_document_group_template_recipients_put_request_creation():
    """
    Test DocumentGroupTemplateRecipientsPutRequest creation with recipients.
    """
    request = DocumentGroupTemplateRecipientsPutRequest(
        recipients=[{"email": "signer@example.com"}],
    )
    request.with_template_group_id("tpl_group_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["template_group_id"] == "tpl_group_id"
    payload = request.payload()
    assert "recipients" in payload
    assert payload["recipients"] == [{"email": "signer@example.com"}]


def test_document_group_template_recipients_put_request_with_reminder():
    """
    Test DocumentGroupTemplateRecipientsPutRequest with expiration, reminder, and order_type.
    """
    request = DocumentGroupTemplateRecipientsPutRequest(
        recipients=[{"email": "signer@example.com"}],
        general_expiration_days=30,
        general_reminder={
            "remind_before": 5,
            "remind_repeat": 3,
            "remind_after": 7,
        },
        order_type="recipient_order",
    )
    request.with_template_group_id("tpl_group_id")

    payload = request.payload()
    assert payload["general_expiration_days"] == 30
    assert payload["general_reminder"]["remind_before"] == 5
    assert payload["general_reminder"]["remind_repeat"] == 3
    assert payload["general_reminder"]["remind_after"] == 7
    assert payload["order_type"] == "recipient_order"


def test_document_group_template_recipients_put_request_without_optional_fields():
    """
    Test that optional fields are not included in payload when not set.
    """
    request = DocumentGroupTemplateRecipientsPutRequest(
        recipients=[{"email": "signer@example.com"}],
    )

    payload = request.payload()
    assert "general_expiration_days" not in payload
    assert "general_reminder" not in payload
    assert "order_type" not in payload


def test_document_group_template_recipients_put_request_endpoint():
    """
    Test that the PUT request has the correct API endpoint configuration.
    """
    request = DocumentGroupTemplateRecipientsPutRequest()
    endpoint = request.__api_endpoint__

    assert endpoint.url == "/v2/document-group-templates/{template_group_id}/recipients"
    assert endpoint.method == "put"
    assert endpoint.auth == "bearer"
    assert endpoint.namespace == "documentGroupTemplate"
    assert endpoint.entity == "documentGroupTemplateRecipients"


# ============================================================================
# Response Tests
# ============================================================================


def test_document_group_template_recipients_get_response_structure():
    """
    Test DocumentGroupTemplateRecipientsGetResponse data structure.
    """
    response = DocumentGroupTemplateRecipientsGetResponse()
    assert response.data is None


def test_document_group_template_recipients_get_response_with_data():
    """
    Test DocumentGroupTemplateRecipientsGetResponse with full data.
    """
    response = DocumentGroupTemplateRecipientsGetResponse(
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
                            "id": "abc123",
                            "role": "Contract Preparer",
                            "action": "sign",
                        }
                    ],
                }
            ],
            "unmapped_documents": [],
            "allowed_unmapped_sign_documents": [],
            "cc": [],
            "order_type": "recipient_order",
            "general_expiration_days": 30,
            "general_reminder": {
                "remind_before": 5,
                "remind_repeat": 3,
                "remind_after": 7,
            },
        }
    )

    assert response.data is not None
    assert len(response.data["recipients"]) == 1
    assert response.data["general_expiration_days"] == 30
    assert response.data["general_reminder"]["remind_before"] == 5
    assert response.data["general_reminder"]["remind_repeat"] == 3
    assert response.data["general_reminder"]["remind_after"] == 7
    assert response.data["order_type"] == "recipient_order"


def test_document_group_template_recipients_put_response_structure():
    """
    Test DocumentGroupTemplateRecipientsPutResponse data structure.
    """
    response = DocumentGroupTemplateRecipientsPutResponse()
    assert response.data is None


def test_document_group_template_recipients_put_response_with_data():
    """
    Test DocumentGroupTemplateRecipientsPutResponse with data.
    """
    response = DocumentGroupTemplateRecipientsPutResponse(
        data={
            "recipients": [{"email": "signer@example.com"}],
            "general_expiration_days": 15,
            "general_reminder": {
                "remind_before": 2,
                "remind_repeat": 1,
                "remind_after": 3,
            },
        }
    )

    assert response.data is not None
    assert response.data["general_expiration_days"] == 15


# ============================================================================
# Mock API Call Tests
# ============================================================================


def test_document_group_template_recipients_get_api_call(mock_api_client):
    """
    Test API call for getting document group template recipients.
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
            "order_type": "advanced_order",
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

    request = DocumentGroupTemplateRecipientsGetRequest()
    request.with_template_group_id("tpl_group_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    assert isinstance(response, DocumentGroupTemplateRecipientsGetResponse)
    assert response.data is not None
    assert response.data["general_expiration_days"] == 30
    assert response.data["general_reminder"]["remind_before"] == 5
    assert len(response.data["recipients"]) == 1
    assert response.data["order_type"] == "advanced_order"

    mock_api_client._client.request.assert_called_once()


def test_document_group_template_recipients_put_api_call(mock_api_client):
    """
    Test API call for updating document group template recipients with reminder fields.
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    mock_response_data = {
        "data": {
            "recipients": [{"email": "signer@example.com"}],
            "general_expiration_days": 30,
            "general_reminder": {
                "remind_before": 5,
                "remind_repeat": 3,
                "remind_after": 7,
            },
            "order_type": "at_the_same_time",
        }
    }

    mock_response = MagicMock(spec=httpx.Response)
    mock_response.status_code = 200
    mock_response.text = json.dumps(mock_response_data)
    mock_response.content = json.dumps(mock_response_data).encode()
    mock_response.headers = {"Content-Type": "application/json"}

    mock_api_client._client.request.return_value = mock_response

    request = DocumentGroupTemplateRecipientsPutRequest(
        recipients=[{"email": "signer@example.com"}],
        general_expiration_days=30,
        general_reminder={
            "remind_before": 5,
            "remind_repeat": 3,
            "remind_after": 7,
        },
    )
    request.with_template_group_id("tpl_group_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    assert isinstance(response, DocumentGroupTemplateRecipientsPutResponse)
    assert response.data is not None
    assert response.data["general_expiration_days"] == 30
    assert response.data["order_type"] == "at_the_same_time"

    mock_api_client._client.request.assert_called_once()
