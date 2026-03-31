"""
Pytest configuration and fixtures.

This module provides shared fixtures and test utilities (analog of BaseTest in Java SDK).
It includes:
- Test configuration setup
- Mock data generators
- Common test utilities
- Fixtures for API client and tokens
"""

import os
import tempfile

import pytest

from signnow.core.config import ConfigLoader, ConfigRepository
from signnow.core.token import BasicToken, BearerToken


@pytest.fixture
def test_config_file():
    """
    Creates a temporary test configuration file.

    Returns:
        Path to the temporary configuration file
    """
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".env") as f:
        f.write("SIGNNOW_API_HOST=https://api.test.not.exist.signnow.com\n")
        f.write("SIGNNOW_API_BASIC_TOKEN=test_basic_token\n")
        f.write("SIGNNOW_API_USERNAME=user-test@signnow.com\n")
        f.write("SIGNNOW_API_PASSWORD=test!PAZZW\n")
        temp_path = f.name

    yield temp_path

    # Cleanup
    if os.path.exists(temp_path):
        os.unlink(temp_path)


@pytest.fixture
def test_config_repository(test_config_file):
    """
    Creates a ConfigRepository from test configuration file.

    Args:
        test_config_file: Path to test configuration file

    Returns:
        ConfigRepository instance
    """
    loader = ConfigLoader()
    config_map = loader.load(test_config_file)
    return ConfigRepository(config_map)


@pytest.fixture
def test_basic_token():
    """
    Creates a test BasicToken.

    Returns:
        BasicToken instance with test token
    """
    return BasicToken("test-basic")


@pytest.fixture
def test_bearer_token():
    """
    Creates a test BearerToken.

    Returns:
        BearerToken instance with test tokens
    """
    return BearerToken(
        access_token="test-bearer",
        refresh_token="test-refresh",
        expires=25920,
    )


@pytest.fixture
def test_bearer_token_empty():
    """
    Creates an empty BearerToken.

    Returns:
        Empty BearerToken instance
    """
    return BearerToken("")


@pytest.fixture
def test_download_directory():
    """
    Creates a temporary download directory.

    Returns:
        Path to the temporary download directory
    """
    temp_dir = tempfile.mkdtemp()
    yield temp_dir

    # Cleanup
    import shutil

    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)


@pytest.fixture
def mock_api_client(test_config_repository, test_basic_token, test_bearer_token):
    """
    Creates a mock API client for testing real API calls.

    This fixture provides an ApiClient with a mocked httpx.Client that can be
    configured to return specific responses for testing.

    Returns:
        ApiClient instance with mocked HTTP client
    """
    from unittest.mock import MagicMock
    import httpx
    from signnow.core.api_client import ApiClient
    from signnow.core.request import ApiEndpointResolver

    mock_client = MagicMock(spec=httpx.Client)
    resolver = ApiEndpointResolver()
    return ApiClient(
        client=mock_client,
        api_endpoint_resolver=resolver,
        config_repository=test_config_repository,
        basic_token=test_basic_token,
        bearer_token=test_bearer_token,
    )
