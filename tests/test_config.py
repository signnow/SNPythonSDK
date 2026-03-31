"""
Tests for configuration classes.

This module contains tests for configuration management including:
- Configuration defaults and default values
- Configuration loading from files (.env format)
- Configuration repository for accessing configuration values
- Environment variable handling and parsing

These tests verify that the SDK can properly load and manage configuration
from various sources including environment variables and configuration files.
"""

import os
import tempfile

from signnow.core.config import (
    ConfigDefaults,
    ConfigLoader,
    ConfigRepository,
)


def test_config_defaults():
    """
    Test ConfigDefaults class for default configuration values.

    Verifies that:
    - Default configuration values are properly defined
    - Default host is set to SignNow API host
    - All required environment variable names are present in defaults
    """
    defaults = ConfigDefaults.get_defaults()
    assert ConfigDefaults.ENV_VAR_HOST in defaults
    assert defaults[ConfigDefaults.ENV_VAR_HOST] == ConfigDefaults.SIGNNOW_API_HOST


def test_config_loader_from_file():
    """
    Test ConfigLoader loading configuration from file.

    Verifies that:
    - Configuration can be loaded from .env file format
    - Environment variables are properly parsed
    - Comments in configuration files are ignored
    - Multiple configuration values are correctly loaded
    """
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".env") as f:
        f.write("SIGNNOW_API_HOST=https://test.api.com\n")
        f.write("SIGNNOW_API_BASIC_TOKEN=test_token\n")
        f.write("# This is a comment\n")
        f.write("SIGNNOW_API_USERNAME=test_user\n")
        temp_path = f.name

    try:
        loader = ConfigLoader()
        config = loader.load(temp_path)
        assert config["SIGNNOW_API_HOST"] == "https://test.api.com"
        assert config["SIGNNOW_API_BASIC_TOKEN"] == "test_token"
        assert config["SIGNNOW_API_USERNAME"] == "test_user"
        assert "# This is a comment" not in config
    finally:
        os.unlink(temp_path)


def test_config_repository():
    """
    Test ConfigRepository for accessing configuration values.

    Verifies that:
    - Configuration repository can be created from configuration map
    - All configuration values are accessible through repository methods
    - Host, user, password, and token are correctly retrieved
    - Client name and timeout values are properly set
    """
    config_map = {
        ConfigDefaults.ENV_VAR_HOST: "https://test.api.com",
        ConfigDefaults.ENV_VAR_BASIC_TOKEN: "test_token",
        ConfigDefaults.ENV_VAR_USERNAME: "test_user",
        ConfigDefaults.ENV_VAR_PASSWORD: "test_password",
    }
    repo = ConfigRepository(config_map)
    assert repo.host() == "https://test.api.com"
    assert repo.user() == "test_user"
    assert repo.password() == "test_password"
    assert repo.basic_token().token() == "test_token"
    assert repo.client_name() == "SignNowApiClient/v3.0.0 (Python)"
    assert repo.read_timeout() == 15
