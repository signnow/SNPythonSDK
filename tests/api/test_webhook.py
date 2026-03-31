"""
Tests for Webhook API.

This module contains tests for webhook API including:
- Webhook subscription operations

These tests verify that webhook requests and responses can be properly
created and structured for interaction with the SignNow API.
"""

from signnow.api.webhook.request import (
    SubscriptionDeleteRequest,
    SubscriptionGetRequest,
    SubscriptionPostRequest,
    SubscriptionPutRequest,
)
from signnow.api.webhook.response import (
    SubscriptionDeleteResponse,
    SubscriptionGetResponse,
    SubscriptionPostResponse,
    SubscriptionPutResponse,
)


def test_subscription_post_request_creation():
    """Test SubscriptionPostRequest creation and structure."""
    request = SubscriptionPostRequest(
        event="document.complete",
        entity_id="test_entity_id",
        action="callback",
    )

    assert hasattr(request, "__api_endpoint__")
    assert request.uri_params() == {}
    payload = request.payload()
    assert "event" in payload
    assert "entity_id" in payload
    assert "action" in payload


def test_subscription_get_request_creation():
    """Test SubscriptionGetRequest creation and structure."""
    request = SubscriptionGetRequest()

    assert hasattr(request, "__api_endpoint__")
    assert request.uri_params() == {}
    assert request.payload() == {}


def test_subscription_put_request_creation():
    """Test SubscriptionPutRequest creation and structure."""
    request = SubscriptionPutRequest(
        event="document.complete", entity_id="entity_id", action="action"
    )
    request.with_event_subscription_id("test_subscription_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["event_subscription_id"] == "test_subscription_id"


def test_subscription_delete_request_creation():
    """Test SubscriptionDeleteRequest creation and structure."""
    request = SubscriptionDeleteRequest()
    request.with_event_subscription_id("test_subscription_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["event_subscription_id"] == "test_subscription_id"


def test_subscription_post_response_structure():
    """Test SubscriptionPostResponse data structure."""
    response = SubscriptionPostResponse()
    assert response is not None


def test_subscription_get_response_structure():
    """Test SubscriptionGetResponse data structure."""
    response = SubscriptionGetResponse()
    assert response is not None


def test_subscription_put_response_structure():
    """Test SubscriptionPutResponse data structure."""
    response = SubscriptionPutResponse()
    assert response is not None


def test_subscription_delete_response_structure():
    """Test SubscriptionDeleteResponse data structure."""
    response = SubscriptionDeleteResponse()
    assert response is not None


# ============================================================================
# Real API Call Tests (similar to Java SDK tests)
# ============================================================================


def test_subscription_post_api_call(mock_api_client):
    """
    Test real API call for creating subscription.

    Verifies that:
    - ApiClient can send SubscriptionPostRequest
    - Response is properly parsed (similar to Java SubscriptionTest.testPostSubscription)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {"id": "subscription_id"}

    # Create mock httpx.Response
    mock_response = MagicMock(spec=httpx.Response)
    mock_response.status_code = 200
    mock_response.text = json.dumps(mock_response_data)
    mock_response.content = json.dumps(mock_response_data).encode()
    mock_response.headers = {"Content-Type": "application/json"}

    # Configure mock client
    mock_api_client._client.request.return_value = mock_response

    # Execute API call
    request = SubscriptionPostRequest(
        event="document.complete",
        entity_id="test_entity_id",
        action="callback",
    )
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, SubscriptionPostResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_subscription_get_api_call(mock_api_client):
    """
    Test real API call for getting subscriptions.

    Verifies that:
    - ApiClient can send SubscriptionGetRequest
    - Response is properly parsed (similar to Java SubscriptionTest.testGetSubscription)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {"data": []}

    # Create mock httpx.Response
    mock_response = MagicMock(spec=httpx.Response)
    mock_response.status_code = 200
    mock_response.text = json.dumps(mock_response_data)
    mock_response.content = json.dumps(mock_response_data).encode()
    mock_response.headers = {"Content-Type": "application/json"}

    # Configure mock client
    mock_api_client._client.request.return_value = mock_response

    # Execute API call
    request = SubscriptionGetRequest()
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, SubscriptionGetResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_subscription_put_api_call(mock_api_client):
    """
    Test real API call for updating subscription.

    Verifies that:
    - ApiClient can send SubscriptionPutRequest
    - Response is properly parsed (similar to Java SubscriptionTest.testPutSubscription)
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
    request = SubscriptionPutRequest(
        event="document.complete",
        entity_id="test_entity_id",
        action="callback",
    )
    request.with_event_subscription_id("test_subscription_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, SubscriptionPutResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_subscription_delete_api_call(mock_api_client):
    """
    Test real API call for deleting subscription.

    Verifies that:
    - ApiClient can send SubscriptionDeleteRequest
    - Response is properly parsed (similar to Java SubscriptionTest.testDeleteSubscription)
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
    request = SubscriptionDeleteRequest()
    request.with_event_subscription_id("test_subscription_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, SubscriptionDeleteResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()
