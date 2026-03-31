"""
Tests for the main SDK class.

This module contains tests for the core SDK functionality including:
- SDK initialization with default and custom configuration
- SDK building and API client creation
- SDK version retrieval
- Bearer token management

These tests verify that the SDK can be properly instantiated and configured
to interact with the SignNow API.
"""

from signnow.sdk import Sdk


def test_sdk_initialization():
    """
    Test SDK initialization with default configuration.

    Verifies that:
    - SDK can be instantiated without parameters
    - SDK version is correctly set
    - SDK instance is not None
    """
    sdk = Sdk()
    assert sdk is not None
    assert sdk.version() == "2024-08-30"


def test_sdk_with_config_path():
    """
    Test SDK initialization with custom configuration file path.

    Verifies that:
    - SDK can be instantiated with a path to configuration file
    - SDK instance is properly created
    """
    sdk = Sdk(".env")
    assert sdk is not None


def test_sdk_build():
    """
    Test SDK build method to create configured SDK instance.

    Verifies that:
    - SDK build() method returns a configured SDK instance
    - Built SDK has a valid API client
    - API client is not None
    """
    sdk = Sdk()
    built_sdk = sdk.build()
    assert built_sdk is not None
    assert built_sdk.get_api_client() is not None


def test_sdk_version():
    """
    Test SDK version method to retrieve API version.

    Verifies that:
    - SDK version() method returns the correct API version string
    - Version format is correct (YYYY-MM-DD)
    """
    sdk = Sdk()
    version = sdk.version()
    assert version == "2024-08-30"
