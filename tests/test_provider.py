"""
Tests for service provider functionality.

This module contains tests for service provider functionality including:
- Configuration loading with defaults
- Configuration loading from file
- Service registration

These tests verify that the SDK can properly initialize services
and configuration, similar to ApiServiceProvider in Java SDK.
"""

import os
import tempfile
from pathlib import Path

from signnow.core.config import ConfigDefaults
from signnow.core.token import BasicToken
from signnow.sdk import Sdk


def test_build_config_with_defaults_loading():
    """
    Test SDK build with defaults loading when config file doesn't exist.

    Verifies that:
    - SDK can be built with non-existing config file
    - Default configuration values are applied
    - ConfigRepository is properly initialized with defaults
    """
    sdk = Sdk(".not_existing_config")
    built_sdk = sdk.build()
    config_repository = built_sdk._config_repository

    assert config_repository is not None
    assert config_repository.host() == ConfigDefaults.SIGNNOW_API_HOST
    assert config_repository.user() == ""
    assert config_repository.password() == ""
    assert config_repository.basic_token().token() == ""
    assert config_repository.project_directory() == str(Path.cwd())
    assert config_repository.downloads_directory() == str(Path.cwd() / "downloads")


def test_build_config_with_actual_config_file():
    """
    Test SDK build with actual config file.

    Verifies that:
    - SDK can be built with existing config file
    - Configuration values from file are loaded correctly
    - ConfigRepository is properly initialized with file values
    """
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".env") as f:
        f.write("SIGNNOW_API_HOST=https://api.test.not.exist.signnow.com\n")
        f.write("SIGNNOW_API_BASIC_TOKEN=test_basic_token\n")
        f.write("SIGNNOW_API_USERNAME=user-test@signnow.com\n")
        f.write("SIGNNOW_API_PASSWORD=test!PAZZW\n")
        temp_path = f.name

    try:
        sdk = Sdk(temp_path)
        built_sdk = sdk.build()
        config_repository = built_sdk._config_repository

        assert config_repository is not None
        assert config_repository.host() == "https://api.test.not.exist.signnow.com"
        assert config_repository.user() == "user-test@signnow.com"
        assert config_repository.password() == "test!PAZZW"
        assert isinstance(config_repository.basic_token(), BasicToken)
        assert config_repository.basic_token().token() == "test_basic_token"
        assert config_repository.project_directory() == str(Path.cwd())
        assert config_repository.downloads_directory() == str(Path.cwd() / "downloads")
    finally:
        if os.path.exists(temp_path):
            os.unlink(temp_path)
