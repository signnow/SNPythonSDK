"""Tests for ApiClient — covers error paths and internal helpers."""

import json
from unittest.mock import MagicMock

import httpx
import pytest

from signnow.core.api_client import ApiClient
from signnow.core.exception import SignNowApiException
from signnow.core.request import ApiEndpoint, ApiEndpointResolver
from signnow.core.token import BasicToken, BearerToken

# ---------------------------------------------------------------------------
# fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def config_repo(test_config_repository):
    return test_config_repository


@pytest.fixture
def client(config_repo):
    """ApiClient with a mocked httpx.Client and a bearer token set."""
    mock_http = MagicMock(spec=httpx.Client)
    return ApiClient(
        client=mock_http,
        api_endpoint_resolver=ApiEndpointResolver(),
        config_repository=config_repo,
        basic_token=BasicToken("basic-tok"),
        bearer_token=BearerToken("bearer-tok"),
    )


@pytest.fixture
def client_no_bearer(config_repo):
    """ApiClient without a bearer token."""
    mock_http = MagicMock(spec=httpx.Client)
    return ApiClient(
        client=mock_http,
        api_endpoint_resolver=ApiEndpointResolver(),
        config_repository=config_repo,
        basic_token=BasicToken("basic-tok"),
        bearer_token=None,
    )


# ---------------------------------------------------------------------------
# _build_auth_header
# ---------------------------------------------------------------------------


def test_basic_auth_header(client):
    ep = ApiEndpoint(name="t", url="/t", method="get", auth="basic")
    assert client._build_auth_header(ep) == "Basic basic-tok"


def test_bearer_auth_header(client):
    ep = ApiEndpoint(name="t", url="/t", method="get", auth="bearer")
    assert client._build_auth_header(ep) == "Bearer bearer-tok"


def test_bearer_missing_raises(client_no_bearer):
    ep = ApiEndpoint(name="t", url="/t", method="get", auth="bearer")
    with pytest.raises(SignNowApiException, match="Bearer token is required"):
        client_no_bearer._build_auth_header(ep)


def test_unknown_auth_raises(client):
    ep = ApiEndpoint(name="t", url="/t", method="get", auth="digest")
    with pytest.raises(SignNowApiException, match="Unknown request authentication"):
        client._build_auth_header(ep)


# ---------------------------------------------------------------------------
# _validate_response
# ---------------------------------------------------------------------------


def test_validate_200_ok(client):
    client._validate_response(200)  # should not raise


def test_validate_201_ok(client):
    client._validate_response(201)


def test_validate_4xx_raises(client):
    with pytest.raises(SignNowApiException, match="invalid") as exc_info:
        client._validate_response(
            400,
            endpoint="POST /document",
            payload='{"name": "test"}',
            response_body='{"error": "bad request"}',
        )
    exc = exc_info.value
    assert exc.endpoint == "POST /document"
    assert exc.payload == '{"name": "test"}'
    assert exc.response == '{"error": "bad request"}'
    assert exc.response_code == 400

    with pytest.raises(SignNowApiException) as exc_info:
        client._validate_response(422, endpoint="PUT /document/{id}")
    assert exc_info.value.response_code == 422
    assert exc_info.value.endpoint == "PUT /document/{id}"

    with pytest.raises(SignNowApiException):
        client._validate_response(499)


def test_validate_5xx_raises(client):
    with pytest.raises(SignNowApiException, match="server error") as exc_info:
        client._validate_response(
            500,
            endpoint="GET /user",
            response_body='{"error": "internal"}',
        )
    exc = exc_info.value
    assert exc.endpoint == "GET /user"
    assert exc.response == '{"error": "internal"}'
    assert exc.response_code == 500

    with pytest.raises(SignNowApiException) as exc_info:
        client._validate_response(503)
    assert exc_info.value.response_code == 503


# ---------------------------------------------------------------------------
# _build_url
# ---------------------------------------------------------------------------


def test_build_url_with_uri_params(client):
    ep = ApiEndpoint(name="t", url="/document/{document_id}", method="get")
    request = MagicMock()
    request.uri_params.return_value = {"document_id": "abc123"}
    request.query_params = None
    url = client._build_url(ep, request)
    assert "/document/abc123" in url


# ---------------------------------------------------------------------------
# _build_headers
# ---------------------------------------------------------------------------


def test_build_headers_contains_required_keys(client):
    ep = ApiEndpoint(
        name="t", url="/t", method="get", auth="bearer", type="application/json"
    )
    headers = client._build_headers(ep)
    assert headers["Accept"] == "application/json"
    assert headers["Content-Type"] == "application/json"
    assert "Authorization" in headers
    assert "User-Agent" in headers


# ---------------------------------------------------------------------------
# _build_body
# ---------------------------------------------------------------------------


def test_build_body_get_returns_none(client):
    ep = ApiEndpoint(name="t", url="/t", method="get")
    request = MagicMock()
    assert client._build_body(ep, request) is None


def test_build_body_json_post(client):
    ep = ApiEndpoint(name="t", url="/t", method="post", type="application/json")
    request = MagicMock()
    request.payload.return_value = {"key": "val", "empty": None}
    body = client._build_body(ep, request)
    parsed = json.loads(body)
    assert parsed == {"key": "val"}  # None stripped


def test_build_body_form_urlencoded(client):
    ep = ApiEndpoint(
        name="t", url="/t", method="post", type="application/x-www-form-urlencoded"
    )
    request = MagicMock()
    request.payload.return_value = {"grant_type": "password", "user": "a"}
    body = client._build_body(ep, request)
    assert b"grant_type=password" in body


# ---------------------------------------------------------------------------
# _is_file_download
# ---------------------------------------------------------------------------


def test_is_file_download_pdf():
    ep = ApiEndpoint(
        name="t", url="/doc/{id}/download", method="get", type="application/pdf"
    )
    assert ApiClient._is_file_download(ep) is True


def test_is_file_download_zip():
    ep = ApiEndpoint(
        name="t", url="/group/{id}/downloadall", method="post", type="application/zip"
    )
    assert ApiClient._is_file_download(ep) is True


def test_is_file_download_url_segment():
    ep = ApiEndpoint(
        name="t", url="/doc/{id}/download", method="get", type="application/json"
    )
    assert ApiClient._is_file_download(ep) is True


def test_is_not_file_download_link():
    ep = ApiEndpoint(
        name="t", url="/doc/{id}/download/link", method="post", type="application/json"
    )
    assert ApiClient._is_file_download(ep) is False


def test_is_not_file_download_regular():
    ep = ApiEndpoint(name="t", url="/user", method="get", type="application/json")
    assert ApiClient._is_file_download(ep) is False


# ---------------------------------------------------------------------------
# set/get bearer token
# ---------------------------------------------------------------------------


def test_set_get_bearer_token(client):
    new_token = BearerToken("new-tok")
    client.set_bearer_token(new_token)
    assert client.get_bearer_token() is new_token


# ---------------------------------------------------------------------------
# _get_payload helper
# ---------------------------------------------------------------------------


def test_get_payload_none(client):
    assert client._get_payload(None) is None


def test_get_payload_utf8(client):
    assert client._get_payload(b'{"k":"v"}') == '{"k":"v"}'


def test_get_payload_binary(client):
    assert client._get_payload(b"\x80\x81") == "<binary data>"


# ---------------------------------------------------------------------------
# send — HTTP error wrapping
# ---------------------------------------------------------------------------


def test_send_http_error_wraps_exception(client):
    """httpx.HTTPError during request is wrapped in SignNowApiException."""
    from signnow.api.user.request import UserGetRequest

    client._client.request.side_effect = httpx.ConnectError("connection refused")
    with pytest.raises(SignNowApiException, match="Failed processing"):
        client.send(UserGetRequest())
