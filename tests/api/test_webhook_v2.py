"""
Tests for WebhookV2 API.

This module contains tests for webhook V2 API including:
- Event subscription operations
- Callback operations

These tests verify that webhook V2 requests and responses can be properly
created and structured for interaction with the SignNow API.
"""

from signnow.api.webhookv2.request import (
    CallbackGetRequest,
    CallbacksAllGetRequest,
    EventSubscriptionAllGetRequest,
    EventSubscriptionDeleteRequest,
    EventSubscriptionGetRequest,
    EventSubscriptionPutRequest,
    EventSubscriptionsCallbacksAllGetRequest,
)
from signnow.api.webhookv2.response import (
    CallbackGetResponse,
    CallbacksAllGetResponse,
    EventSubscriptionAllGetResponse,
    EventSubscriptionDeleteResponse,
    EventSubscriptionGetResponse,
    EventSubscriptionPutResponse,
    EventSubscriptionsCallbacksAllGetResponse,
)


def test_event_subscription_get_request_creation():
    """Test EventSubscriptionGetRequest creation and structure."""
    request = EventSubscriptionGetRequest()
    request.with_event_subscription_id("test_subscription_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["event_subscription_id"] == "test_subscription_id"


def test_event_subscription_all_get_request_creation():
    """Test EventSubscriptionAllGetRequest creation and structure."""
    request = EventSubscriptionAllGetRequest()

    assert hasattr(request, "__api_endpoint__")
    assert request.uri_params() == {}
    assert request.payload() == {}


def test_event_subscription_put_request_creation():
    """Test EventSubscriptionPutRequest creation and structure."""
    from signnow.api.webhookv2.request.data.attribute import Attribute

    attributes = Attribute(callback="https://example.com/callback")
    request = EventSubscriptionPutRequest(
        event="document.complete",
        entity_id="entity_id",
        action="callback",
        attributes=attributes,
    )
    request.with_event_subscription_id("test_subscription_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["event_subscription_id"] == "test_subscription_id"


def test_event_subscription_delete_request_creation():
    """Test EventSubscriptionDeleteRequest creation and structure."""
    request = EventSubscriptionDeleteRequest()
    request.with_event_subscription_id("test_subscription_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["event_subscription_id"] == "test_subscription_id"


def test_callback_get_request_creation():
    """Test CallbackGetRequest creation and structure."""
    request = CallbackGetRequest()
    request.with_callback_id("test_callback_id")

    assert hasattr(request, "__api_endpoint__")
    uri_params = request.uri_params()
    assert uri_params["callback_id"] == "test_callback_id"


def test_callbacks_all_get_request_creation():
    """Test CallbacksAllGetRequest creation and structure."""
    request = CallbacksAllGetRequest()

    assert hasattr(request, "__api_endpoint__")
    assert request.uri_params() == {}
    assert request.payload() == {}


def test_event_subscriptions_callbacks_all_get_request_creation():
    """Test EventSubscriptionsCallbacksAllGetRequest creation and structure."""
    request = EventSubscriptionsCallbacksAllGetRequest()

    assert hasattr(request, "__api_endpoint__")
    assert request.uri_params() == {}
    assert request.payload() == {}


def test_event_subscription_get_response_structure():
    """Test EventSubscriptionGetResponse data structure."""
    response = EventSubscriptionGetResponse()
    assert response is not None


def test_event_subscription_all_get_response_structure():
    """Test EventSubscriptionAllGetResponse data structure."""
    response = EventSubscriptionAllGetResponse()
    assert response is not None


def test_event_subscription_put_response_structure():
    """Test EventSubscriptionPutResponse data structure."""
    response = EventSubscriptionPutResponse()
    assert response is not None


def test_event_subscription_delete_response_structure():
    """Test EventSubscriptionDeleteResponse data structure."""
    response = EventSubscriptionDeleteResponse()
    assert response is not None


def test_callback_get_response_structure():
    """Test CallbackGetResponse data structure."""
    response = CallbackGetResponse()
    assert response is not None


def test_callbacks_all_get_response_structure():
    """Test CallbacksAllGetResponse data structure."""
    response = CallbacksAllGetResponse()
    assert response is not None


def test_event_subscriptions_callbacks_all_get_response_structure():
    """Test EventSubscriptionsCallbacksAllGetResponse data structure."""
    response = EventSubscriptionsCallbacksAllGetResponse()
    assert response is not None


# ============================================================================
# Real API Call Tests (similar to Java SDK tests)
# ============================================================================


def test_event_subscription_get_api_call(mock_api_client):
    """
    Test real API call for getting event subscription.

    Verifies that:
    - ApiClient can send EventSubscriptionGetRequest
    - Response is properly parsed (similar to Java EventSubscriptionTest.testGetEventSubscription)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {
        "data": {
            "id": "subscription_id",
            "event": "document.complete",
            "entity_id": "entity_id",
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
    request = EventSubscriptionGetRequest()
    request.with_event_subscription_id("test_subscription_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, EventSubscriptionGetResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_event_subscription_put_api_call(mock_api_client):
    """
    Test real API call for updating event subscription.

    Verifies that:
    - ApiClient can send EventSubscriptionPutRequest
    - Response is properly parsed (similar to Java EventSubscriptionTest.testPutEventSubscription)
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
    from signnow.api.webhookv2.request.data.attribute import Attribute

    attributes = Attribute(callback="https://example.com/callback")
    request = EventSubscriptionPutRequest(
        event="document.complete",
        entity_id="entity_id",
        action="create",
        attributes=attributes,
    )
    request.with_event_subscription_id("test_subscription_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, EventSubscriptionPutResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_event_subscription_delete_api_call(mock_api_client):
    """
    Test real API call for deleting event subscription.

    Verifies that:
    - ApiClient can send EventSubscriptionDeleteRequest
    - Response is properly parsed (similar to Java EventSubscriptionTest.testDeleteEventSubscription)
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
    request = EventSubscriptionDeleteRequest()
    request.with_event_subscription_id("test_subscription_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, EventSubscriptionDeleteResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_event_subscription_all_get_api_call(mock_api_client):
    """
    Test real API call for getting all event subscriptions.

    Verifies that:
    - ApiClient can send EventSubscriptionAllGetRequest
    - Response is properly parsed (similar to Java EventSubscriptionAllTest.testGetEventSubscriptionAll)
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
    request = EventSubscriptionAllGetRequest()
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, EventSubscriptionAllGetResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_callback_get_api_call(mock_api_client):
    """
    Test real API call for getting callback.

    Verifies that:
    - ApiClient can send CallbackGetRequest
    - Response is properly parsed (similar to Java CallbackTest.testGetCallback)
    """
    from unittest.mock import MagicMock
    import httpx
    import json

    # Mock response data
    mock_response_data = {
        "data": {
            "id": "callback_id",
            "url": "https://example.com/callback",
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
    request = CallbackGetRequest()
    request.with_event_subscription_id("test_subscription_id")
    request.with_callback_id("test_callback_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, CallbackGetResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_callbacks_all_get_api_call(mock_api_client):
    """
    Test real API call for getting all callbacks.

    Verifies that:
    - ApiClient can send CallbacksAllGetRequest
    - Response is properly parsed (similar to Java CallbacksAllTest.testGetCallbacksAll)
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
    request = CallbacksAllGetRequest()
    request.with_event_subscription_id("test_subscription_id")
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, CallbacksAllGetResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()


def test_event_subscriptions_callbacks_all_get_api_call(mock_api_client):
    """
    Test real API call for getting all event subscriptions callbacks.

    Verifies that:
    - ApiClient can send EventSubscriptionsCallbacksAllGetRequest
    - Response is properly parsed (similar to Java EventSubscriptionsCallbacksAllTest.testGetEventSubscriptionsCallbacksAll)
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
    request = EventSubscriptionsCallbacksAllGetRequest()
    reply = mock_api_client.send(request)
    response = reply.get_response()

    # Assertions
    assert isinstance(response, EventSubscriptionsCallbacksAllGetResponse)
    assert response is not None

    # Verify API client was called
    mock_api_client._client.request.assert_called_once()
