"""
Tests for response classes.

This module contains tests for response handling including:
- ResponseParser for parsing JSON and file responses
- ResponseData for handling HTTP response data
- Reply for representing server replies

These tests verify that responses can be properly parsed, deserialized,
and handled from the SignNow API.
"""

from signnow.api.auth.request import TokenPostRequest
from signnow.api.webhookv2.request import EventSubscriptionDeleteRequest
from signnow.core.exception import SignNowApiException
from signnow.core.request import ApiEndpointResolver
from signnow.core.response import ResponseData, ResponseParser


def test_json_response_mapped_successfully():
    """
    Test ResponseParser parsing JSON response successfully.

    Verifies that:
    - ResponseParser can parse JSON response and map it to response class
    - Reply object contains correct status code, JSON, and deserialized response
    - All response fields are correctly mapped from JSON
    """
    api_endpoint_resolver = ApiEndpointResolver()
    request = TokenPostRequest(
        user="test_user",
        password="test#paZZw0rd",
        scope="*",
        grant_type="password",
        code="some code",
    )

    json_response = (
        "{"
        '"expires_in": 1754143108, '
        '"token_type":"bearer", '
        '"access_token":"f9b20",'
        '"refresh_token":"2c9737",'
        '"scope":"*",'
        '"last_login":590918188'
        "}"
    )
    endpoint = api_endpoint_resolver.resolve(request)
    response_data = ResponseData(
        code=200,
        content_type="application/json",
        content_disposition="",
        download_directory="",
        content=json_response.encode("utf-8"),
    )
    reply = ResponseParser.parse(response_data, endpoint)
    response = reply.get_response()

    assert reply.get_status_code() == 200
    assert reply.is_ok()
    assert not reply.is_empty()
    assert reply.to_json() == json_response
    assert response.expires_in == 1754143108
    assert response.token_type == "bearer"
    assert response.access_token == "f9b20"
    assert response.refresh_token == "2c9737"
    assert response.scope == "*"
    assert response.last_login == 590918188


def test_map_empty_response():
    """
    Test ResponseParser mapping empty response.

    Verifies that:
    - ResponseParser can handle empty response (204 status)
    - Reply object correctly identifies empty responses
    - Empty JSON is properly handled
    """
    api_endpoint_resolver = ApiEndpointResolver()
    request = EventSubscriptionDeleteRequest()
    request.with_event_subscription_id("123")

    endpoint = api_endpoint_resolver.resolve(request)
    empty_bytes = b""
    response_data = ResponseData(
        code=204,
        content_type="application/json",
        content_disposition="",
        download_directory="",
        content=empty_bytes,
    )
    reply = ResponseParser.parse(response_data, endpoint)

    assert reply.get_status_code() == 204
    assert reply.is_ok()
    assert reply.is_empty()
    assert reply.to_json() == "{}"


def test_map_empty_json_response():
    """
    Test ResponseParser mapping empty JSON response.

    Verifies that:
    - ResponseParser can handle empty JSON object response
    - Reply correctly identifies empty JSON responses
    - Status code 204 with empty JSON is handled properly
    """
    api_endpoint_resolver = ApiEndpointResolver()
    request = EventSubscriptionDeleteRequest()
    request.with_event_subscription_id("123")

    endpoint = api_endpoint_resolver.resolve(request)
    json_bytes = "{}".encode("utf-8")
    response_data = ResponseData(
        code=204,
        content_type="application/json",
        content_disposition="",
        download_directory="",
        content=json_bytes,
    )
    reply = ResponseParser.parse(response_data, endpoint)

    assert reply.get_status_code() == 204
    assert reply.is_ok()
    assert reply.is_empty()
    assert reply.to_json() == "{}"


def test_response_containing_pdf_file_with_name():
    """
    Test ResponseData with PDF file containing filename.

    Verifies that:
    - ResponseData correctly identifies file responses
    - Content disposition with filename is properly handled
    - File content and metadata are correctly stored
    """
    content = b"text"
    data = ResponseData(
        code=200,
        content_type="application/pdf",
        content_disposition='attachment; filename="demo_document.pdf"',
        download_directory="/tmp",
        content=content,
    )

    assert data.code == 200
    assert data.download_directory == "/tmp"
    assert data.get_content_as_string() == "text"
    assert data.content == content
    assert data.has_file()


def test_response_containing_zip_file_without_name():
    """
    Test ResponseData with ZIP file without filename.

    Verifies that:
    - ResponseData correctly identifies ZIP file responses
    - File responses without explicit filename are handled
    - Binary content is correctly stored
    """
    bytes_content = bytes([0x41, 0x42, 0x43])
    data = ResponseData(
        code=201,
        content_type="application/zip",
        content_disposition="attachment;",
        download_directory="/downloads",
        content=bytes_content,
    )

    assert data.code == 201
    assert data.download_directory == "/downloads"
    assert data.get_content_as_string() == "ABC"
    assert data.content == bytes_content
    assert data.has_file()


def test_response_not_containing_file():
    """
    Test ResponseData with non-file response.

    Verifies that:
    - ResponseData correctly identifies non-file responses
    - Text responses are properly handled
    - has_file() returns False for non-file responses
    """
    empty_array = b""
    data = ResponseData(
        code=204,
        content_type="text/plain",
        content_disposition="",
        download_directory="/downloads",
        content=empty_array,
    )

    assert data.code == 204
    assert not data.has_file()


def test_response_parser_capitalize_first_letter():
    """
    Test ResponseParser capitalize_first_letter method.

    Verifies that:
    - First letter is correctly capitalized
    - Empty strings are handled
    - Single character strings are handled
    """
    assert ResponseParser.capitalize_first_letter("test") == "Test"
    assert ResponseParser.capitalize_first_letter("") == ""
    assert ResponseParser.capitalize_first_letter("a") == "A"
    assert (
        ResponseParser.capitalize_first_letter("TEST") == "TEST"
    )  # Java SDK keeps rest as-is
    assert (
        ResponseParser.capitalize_first_letter("cloneTemplate") == "CloneTemplate"
    )  # Preserves camelCase


def test_json_deserialization_error_includes_response_code():
    """
    Verifies that SignNowApiException raised on JSON deserialization failure
    includes the HTTP response_code from the original response.
    """
    import pytest

    api_endpoint_resolver = ApiEndpointResolver()
    request = TokenPostRequest(
        user="u", password="p", scope="*", grant_type="password", code=""
    )
    endpoint = api_endpoint_resolver.resolve(request)

    # Provide invalid JSON that will cause a deserialization error
    response_data = ResponseData(
        code=200,
        content_type="application/json",
        content_disposition="",
        download_directory="",
        content=b"not valid json",
    )

    with pytest.raises(SignNowApiException) as exc_info:
        ResponseParser.parse(response_data, endpoint)

    exc = exc_info.value
    assert exc.response_code == 200
    assert exc.endpoint is not None
    assert exc.cause is not None
