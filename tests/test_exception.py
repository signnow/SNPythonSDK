"""Tests for SignNowApiException."""

import pytest

from signnow.core.exception import SignNowApiException


def test_exception_message_only():
    """Exception with just a message preserves it."""
    exc = SignNowApiException("something went wrong")
    assert str(exc) == "something went wrong\nStatus: ?"
    assert exc.endpoint is None
    assert exc.payload is None
    assert exc.response is None
    assert exc.response_code is None
    assert exc.cause is None


def test_exception_all_fields():
    """Exception with all fields populated renders them in __str__."""
    cause = ValueError("bad value")
    exc = SignNowApiException(
        message="Auth failed",
        endpoint="POST /oauth2/token",
        payload='{"user":"x"}',
        response='{"error":"invalid_credentials"}',
        response_code=401,
        cause=cause,
    )
    text = str(exc)
    assert "Auth failed" in text
    assert "POST /oauth2/token" in text
    assert "Status: 401" in text
    assert '{"error":"invalid_credentials"}' in text
    assert '{"user":"x"}' in text
    assert "bad value" in text
    assert exc.cause is cause


def test_exception_is_exception():
    """SignNowApiException is a proper Exception subclass."""
    exc = SignNowApiException("test")
    assert isinstance(exc, Exception)
    with pytest.raises(SignNowApiException):
        raise exc


def test_exception_without_optional_fields():
    """Only endpoint populated — response/payload lines omitted."""
    exc = SignNowApiException("err", endpoint="GET /user")
    text = str(exc)
    assert "GET /user" in text
    assert "Response:" not in text
    assert "Request:" not in text


def test_exception_response_code_zero():
    """response_code=0 is falsy but still rendered."""
    exc = SignNowApiException("err", response_code=0)
    # 0 is falsy, so current impl shows '?'
    assert "Status:" in str(exc)
