"""
Tests for token classes.

This module contains tests for authentication tokens including:
- BasicToken for basic authentication
- BearerToken for OAuth2 bearer token authentication
- Token type, value, and expiration handling
- Empty token validation

These tests verify that tokens can be properly created, validated, and used
for API authentication.
"""

from signnow.core.token import BasicToken, BearerToken


def test_basic_token():
    """
    Test BasicToken creation and methods.

    Verifies that:
    - BasicToken can be created with a token string
    - Token type is correctly set to "Basic"
    - Token value is correctly stored and retrieved
    - String representation returns the token value
    """
    token = BasicToken("test_token")
    assert token.type() == "Basic"
    assert token.token() == "test_token"
    assert str(token) == "test_token"


def test_bearer_token():
    """
    Test BearerToken creation and methods with full parameters.

    Verifies that:
    - BearerToken can be created with access token, refresh token, and expiration
    - Token type is correctly set to "Bearer"
    - Access token, refresh token, and expiration are correctly stored
    - Empty token check works correctly for non-empty tokens
    - String representation returns the access token
    """
    token = BearerToken("access_token", "refresh_token", 3600)
    assert token.type() == "Bearer"
    assert token.token() == "access_token"
    assert token.refresh_token() == "refresh_token"
    assert token.expires() == 3600
    assert not token.is_empty()
    assert str(token) == "access_token"


def test_bearer_token_empty():
    """
    Test BearerToken with empty token string.

    Verifies that:
    - BearerToken can be created with empty string
    - Empty token check correctly identifies empty tokens
    """
    token = BearerToken("")
    assert token.is_empty()


def test_bearer_token_simple():
    """
    Test BearerToken with only access token (minimal parameters).

    Verifies that:
    - BearerToken can be created with only access token
    - Refresh token defaults to None when not provided
    - Expiration defaults to 0 when not provided
    - Access token is correctly stored and retrieved
    """
    token = BearerToken("access_token")
    assert token.token() == "access_token"
    assert token.refresh_token() is None
    assert token.expires() == 0
