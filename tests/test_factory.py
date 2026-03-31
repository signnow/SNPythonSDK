"""Tests for SdkFactory."""

from unittest.mock import MagicMock, patch

from signnow.core.factory import SdkFactory


def test_create_api_client_with_bearer_token_returns_client(test_config_file):
    """Factory creates a usable client when given a bearer token."""
    with patch("signnow.core.factory.Sdk") as MockSdk:
        mock_sdk = MockSdk.return_value
        mock_sdk.build.return_value = mock_sdk
        mock_sdk.with_bearer_token.return_value = mock_sdk

        mock_client = MagicMock()
        mock_sdk.get_api_client.return_value = mock_client

        result = SdkFactory.create_api_client_with_bearer_token("tok123")
        assert result is mock_client
        mock_sdk.build.assert_called_once()
        mock_sdk.with_bearer_token.assert_called_once()


def test_create_api_client_with_bearer_token_empty_falls_back(test_config_file):
    """Empty bearer token falls back to full authentication flow."""
    with patch("signnow.core.factory.SdkFactory.create_api_client") as mock_create:
        mock_create.return_value = MagicMock()
        SdkFactory.create_api_client_with_bearer_token("")
        mock_create.assert_called_once()


def test_create_api_client_with_bearer_token_none_falls_back(test_config_file):
    """None bearer token falls back to full authentication flow."""
    with patch("signnow.core.factory.SdkFactory.create_api_client") as mock_create:
        mock_create.return_value = MagicMock()
        SdkFactory.create_api_client_with_bearer_token(None)
        mock_create.assert_called_once()


def test_create_api_client_calls_authenticate():
    """create_api_client calls build → authenticate → get_api_client."""
    with patch("signnow.core.factory.Sdk") as MockSdk:
        mock_sdk = MockSdk.return_value
        mock_sdk.build.return_value = mock_sdk
        mock_sdk.authenticate.return_value = mock_sdk

        mock_client = MagicMock()
        mock_sdk.get_api_client.return_value = mock_client

        client = SdkFactory.create_api_client()
        assert client is mock_client
        mock_sdk.build.assert_called_once()
        mock_sdk.authenticate.assert_called_once()
        mock_sdk.get_api_client.assert_called_once()


def test_create_api_client_with_config_path():
    """create_api_client forwards config_path to Sdk constructor."""
    with patch("signnow.core.factory.Sdk") as MockSdk:
        mock_sdk = MockSdk.return_value
        mock_sdk.build.return_value = mock_sdk
        mock_sdk.authenticate.return_value = mock_sdk
        mock_sdk.get_api_client.return_value = MagicMock()

        SdkFactory.create_api_client("/custom/.env")
        MockSdk.assert_called_once_with("/custom/.env")
