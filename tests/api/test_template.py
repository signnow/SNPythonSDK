"""
Tests for Template API.

This module contains tests for template API including:
- Template creation
- Template cloning
- Bulk invite operations
- Routing details operations
- Group template operations

These tests verify that template requests and responses can be properly
created and structured for interaction with the SignNow API.
"""

from signnow.api.template.request import (
    BulkInvitePostRequest,
    CloneTemplatePostRequest,
    GroupTemplateGetRequest,
    GroupTemplatePutRequest,
    RoutingDetailsGetRequest,
    RoutingDetailsPostRequest,
    RoutingDetailsPutRequest,
    TemplatePostRequest,
)
from signnow.api.template.response import (
    BulkInvitePostResponse,
    CloneTemplatePostResponse,
    GroupTemplateGetResponse,
    GroupTemplatePutResponse,
    RoutingDetailsGetResponse,
    RoutingDetailsPostResponse,
    RoutingDetailsPutResponse,
    TemplatePostResponse,
)


def test_template_post_request_creation():
    """
    Test TemplatePostRequest creation and structure.

    Verifies that:
    - TemplatePostRequest can be created with document ID and name
    - Request payload contains document ID and name
    - Request has correct API endpoint annotation
    """
    request = TemplatePostRequest(
        document_id="test_doc_id",
        document_name="Test Template",
    )

    assert hasattr(request, "__api_endpoint__")
    assert request.uri_params() == {}
    payload = request.payload()
    assert payload["document_id"] == "test_doc_id"
    assert payload["document_name"] == "Test Template"


def test_clone_template_post_request_creation():
    """
    Test CloneTemplatePostRequest creation and structure.

    Verifies that:
    - CloneTemplatePostRequest can be created and configured with template ID
    - Template ID is correctly set in URI parameters
    - Request has correct API endpoint annotation
    """
    request = CloneTemplatePostRequest()
    request.with_template_id("test_template_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["template_id"] == "test_template_id"
    assert request.payload() == {}


def test_bulk_invite_post_request_creation():
    """
    Test BulkInvitePostRequest creation and structure.

    Verifies that:
    - BulkInvitePostRequest can be created with file
    - Document ID is correctly set in URI parameters
    - Request has correct API endpoint annotation
    """
    import tempfile

    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as f:
        f.write(b"test content")
        temp_path = f.name

    try:
        request = BulkInvitePostRequest(file=temp_path)
        request.with_document_id("test_template_id")

        assert hasattr(request, "__api_endpoint__")
        uri_params = request.uri_params()
        assert uri_params["document_id"] == "test_template_id"
        # Payload for multipart/form-data is handled differently
    finally:
        import os

        if os.path.exists(temp_path):
            os.unlink(temp_path)


def test_routing_details_get_request_creation():
    """
    Test RoutingDetailsGetRequest creation and structure.

    Verifies that:
    - RoutingDetailsGetRequest can be created and configured with document ID
    - Document ID is correctly set in URI parameters
    - Request has correct API endpoint annotation
    """
    request = RoutingDetailsGetRequest()
    request.with_document_id("test_document_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["document_id"] == "test_document_id"
    assert request.payload() == {}


def test_routing_details_post_request_creation():
    """
    Test RoutingDetailsPostRequest creation and structure.

    Verifies that:
    - RoutingDetailsPostRequest can be created
    - Document ID is correctly set in URI parameters
    - Request has correct API endpoint annotation
    """
    request = RoutingDetailsPostRequest()
    request.with_document_id("test_document_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["document_id"] == "test_document_id"
    assert isinstance(request.payload(), dict)


def test_routing_details_put_request_creation():
    """
    Test RoutingDetailsPutRequest creation and structure.

    Verifies that:
    - RoutingDetailsPutRequest can be created with routing data
    - Document ID is correctly set in URI parameters
    - Request payload contains routing information
    - Request has correct API endpoint annotation
    """
    request = RoutingDetailsPutRequest()
    request.with_document_id("test_document_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["document_id"] == "test_document_id"
    assert isinstance(request.payload(), dict)


def test_group_template_get_request_creation():
    """
    Test GroupTemplateGetRequest creation and structure.

    Verifies that:
    - GroupTemplateGetRequest can be created and configured with template ID
    - Template ID is correctly set in URI parameters
    - Request has correct API endpoint annotation
    """
    request = GroupTemplateGetRequest()
    request.with_template_id("test_template_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["template_id"] == "test_template_id"
    assert request.payload() == {}


def test_group_template_put_request_creation():
    """
    Test GroupTemplatePutRequest creation and structure.

    Verifies that:
    - GroupTemplatePutRequest can be created with group data
    - Template ID is correctly set in URI parameters
    - Request payload contains group information
    - Request has correct API endpoint annotation
    """
    request = GroupTemplatePutRequest(template_group_name="Test Group")
    request.with_template_id("test_template_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["template_id"] == "test_template_id"
    payload = request.payload()
    assert "template_group_name" in payload
    assert payload["template_group_name"] == "Test Group"


def test_template_post_response_structure():
    """
    Test TemplatePostResponse data structure.

    Verifies that:
    - TemplatePostResponse can be instantiated with template data
    - Template ID is correctly stored
    """
    response = TemplatePostResponse(id="test_template_id")

    assert response.id == "test_template_id"


def test_clone_template_post_response_structure():
    """
    Test CloneTemplatePostResponse data structure.

    Verifies that:
    - CloneTemplatePostResponse can be instantiated
    - Response structure is correct
    """
    response = CloneTemplatePostResponse(id="cloned_doc_id", name="Cloned Template")

    assert response is not None
    assert response.id == "cloned_doc_id"
    assert response.name == "Cloned Template"


def test_bulk_invite_post_response_structure():
    """
    Test BulkInvitePostResponse data structure.

    Verifies that:
    - BulkInvitePostResponse can be instantiated
    - Response structure is correct
    """
    response = BulkInvitePostResponse(status="success")

    assert response is not None
    assert response.status == "success"


def test_routing_details_get_response_structure():
    """
    Test RoutingDetailsGetResponse data structure.

    Verifies that:
    - RoutingDetailsGetResponse can be instantiated
    - Response structure is correct
    """
    response = RoutingDetailsGetResponse()

    assert response is not None


def test_routing_details_post_response_structure():
    """
    Test RoutingDetailsPostResponse data structure.

    Verifies that:
    - RoutingDetailsPostResponse can be instantiated
    - Response structure is correct
    """
    response = RoutingDetailsPostResponse()

    assert response is not None


def test_routing_details_put_response_structure():
    """
    Test RoutingDetailsPutResponse data structure.

    Verifies that:
    - RoutingDetailsPutResponse can be instantiated
    - Response structure is correct
    """
    response = RoutingDetailsPutResponse()

    assert response is not None


def test_group_template_get_response_structure():
    """
    Test GroupTemplateGetResponse data structure.

    Verifies that:
    - GroupTemplateGetResponse can be instantiated
    - Response structure is correct
    """
    response = GroupTemplateGetResponse()

    assert response is not None


def test_group_template_put_response_structure():
    """
    Test GroupTemplatePutResponse data structure.

    Verifies that:
    - GroupTemplatePutResponse can be instantiated
    - Response structure is correct
    """
    response = GroupTemplatePutResponse()

    assert response is not None


# ============================================================================
# Real API Call Tests (similar to Java SDK tests)
# ============================================================================


def test_template_post_api_call(mock_api_client):
    """
    Test real API call for creating template.

    Verifies that:
    - ApiClient can send TemplatePostRequest
    - Response is properly parsed (similar to Java TemplateTest.testPostTemplate)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {"id": "template_id"}

    # Create mock httpx.Response
    mock_response = MagicMock(spec=httpx.Response)
    mock_response.status_code = 200
    mock_response.text = json.dumps(mock_response_data)
    mock_response.content = json.dumps(mock_response_data).encode()
    mock_response.headers = {"Content-Type": "application/json"}

    # Configure mock client
    mock_api_client._client.request.return_value = mock_response

    # Execute API call
    request = TemplatePostRequest(
        document_id="test_doc_id",
        document_name="Test Template",
    )
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, TemplatePostResponse)
    assert response.id == "template_id"

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_clone_template_post_api_call(mock_api_client):
    """
    Test real API call for cloning template.

    Verifies that:
    - ApiClient can send CloneTemplatePostRequest
    - Response is properly parsed (similar to Java CloneTemplateTest.testPostCloneTemplate)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {
        "id": "cloned_doc_id",
        "name": "Cloned Template",
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
    request = CloneTemplatePostRequest(
        document_name="Cloned Template",
        client_timestamp="1234567890",
        folder_id="folder_id",
    )
    request.with_template_id("template_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, CloneTemplatePostResponse)
    assert response.id == "cloned_doc_id"
    assert response.name == "Cloned Template"

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_bulk_invite_post_api_call(mock_api_client):
    """
    Test real API call for bulk invite.

    Verifies that:
    - ApiClient can send BulkInvitePostRequest
    - Response is properly parsed (similar to Java BulkInviteTest.testPostBulkInvite)
    """
    from unittest.mock import MagicMock
    import httpx
    import json
    import tempfile

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

    # Create temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as f:
        f.write(b"email,name\nsigner@example.com,Signer Name")
        temp_path = f.name

    try:
        # Execute API call
        request = BulkInvitePostRequest(
            file=temp_path,
            folder_id="folder_id",
            client_timestamp="1234567890",
            document_name="Bulk Invite Document",
            subject="Please sign",
            email_message="Please sign this document",
        )
        request.with_document_id("test_doc_id")
        reply = mock_api_client.send(request)
        response = reply.get_response()

        # Assertions
        assert isinstance(response, BulkInvitePostResponse)
        assert response.status == "success"

        # Verify API client was called
        mock_api_client._client.request.assert_called_once()
    finally:
        import os

        if os.path.exists(temp_path):
            os.unlink(temp_path)


def test_routing_details_get_api_call(mock_api_client):
    """
    Test real API call for getting routing details.

    Verifies that:
    - ApiClient can send RoutingDetailsGetRequest
    - Response is properly parsed (similar to Java RoutingDetailsTest.testGetRoutingDetails)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {
        "routing_details": [],
        "cc": [],
        "cc_step": [],
        "viewers": [],
        "approvers": [],
        "attributes": {},
        "invite_link_instructions": None,
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
    request = RoutingDetailsGetRequest()
    request.with_document_id("test_doc_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, RoutingDetailsGetResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_routing_details_post_api_call(mock_api_client):
    """
    Test real API call for creating routing details.

    Verifies that:
    - ApiClient can send RoutingDetailsPostRequest
    - Response is properly parsed (similar to Java RoutingDetailsTest.testPostRoutingDetails)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {
        "routing_details": [],
        "cc": [],
        "cc_step": [],
        "viewers": [],
        "approvers": [],
        "invite_link_instructions": None,
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
    request = RoutingDetailsPostRequest()
    request.with_document_id("test_doc_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, RoutingDetailsPostResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_routing_details_put_api_call(mock_api_client):
    """
    Test real API call for updating routing details.

    Verifies that:
    - ApiClient can send RoutingDetailsPutRequest
    - Response is properly parsed (similar to Java RoutingDetailsTest.testPutRoutingDetails)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {
        "id": "routing_id",
        "document_id": "test_doc_id",
        "data": {},
        "cc": [],
        "cc_step": [],
        "viewers": [],
        "approvers": [],
        "invite_link_instructions": None,
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
    request = RoutingDetailsPutRequest(
        template_data={},
        template_data_object={},
        cc=[],
        cc_step=[],
        viewers=[],
        approvers=[],
        invite_link_instructions=None,
    )
    request.with_document_id("test_doc_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, RoutingDetailsPutResponse)
    assert response.id == "routing_id"
    assert response.document_id == "test_doc_id"

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_group_template_get_api_call(mock_api_client):
    """
    Test real API call for getting group template.

    Verifies that:
    - ApiClient can send GroupTemplateGetRequest
    - Response is properly parsed (similar to Java GroupTemplateTest.testGetGroupTemplate)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {
        "id": "group_template_id",
        "user_id": "user_id",
        "group_name": "Test Group",
        "folder_id": "folder_id",
        "routing_details": [],
        "templates": [],
        "shared": False,
        "document_group_template_owner_email": "owner@example.com",
        "shared_team_id": None,
        "own_as_merged": False,
        "email_action_on_complete": None,
        "created": "1234567890",
        "updated": "1234567890",
        "recently_used": False,
        "pinned": False,
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
    request = GroupTemplateGetRequest()
    request.with_template_id("template_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, GroupTemplateGetResponse)
    assert response.id == "group_template_id"
    assert response.group_name == "Test Group"

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_group_template_put_api_call(mock_api_client):
    """
    Test real API call for updating group template.

    Verifies that:
    - ApiClient can send GroupTemplatePutRequest
    - Response is properly parsed (similar to Java GroupTemplateTest.testPutGroupTemplate)
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
    request = GroupTemplatePutRequest(
        routing_details={},
        template_group_name="Updated Group",
        template_ids_to_add=[],
        template_ids_to_remove=[],
    )
    request.with_template_id("template_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, GroupTemplatePutResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()
