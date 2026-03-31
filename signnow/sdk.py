"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Optional

import httpx

from signnow.api.auth.request import TokenPostRequest
from signnow.api.auth.response import TokenPostResponse
from signnow.core.api_client import ApiClient
from signnow.core.config import (
    ConfigDefaults,
    ConfigLoader,
    ConfigRepository,
)
from signnow.core.request import ApiEndpointResolver
from signnow.core.token import BearerToken


class Sdk:
    """Main class for the signNow SDK."""

    API_VERSION = "2024-08-30"
    DEFAULT_CONFIG = ".env"
    FULL_SCOPE = "*"
    EMPTY_CODE = ""
    GRANT_TYPE_BY_PASSWORD = "password"

    def __init__(self, config_path: Optional[str] = None):
        """
        Constructor that initializes the SDK with the provided or default configuration path.

        Args:
            config_path: The path to the configuration file (optional)
        """
        if config_path is None or config_path == "":
            config_path = self.DEFAULT_CONFIG

        self._config_path = config_path
        self._api_client: Optional[ApiClient] = None
        self._config_repository: Optional[ConfigRepository] = None

    def build(self) -> "Sdk":
        """
        Builds the SDK by initializing the configuration and API client.

        Returns:
            The built SDK

        Raises:
            SignNowApiException: If an error occurs during the initialization
        """
        # Load configuration
        config_loader = ConfigLoader()
        defaults = ConfigDefaults.get_defaults()
        config = {}

        # Try to load from file
        from pathlib import Path

        config_file = Path(self._config_path)
        if config_file.exists() and config_file.is_file():
            file_config = config_loader.load(self._config_path)
            config.update(file_config)
        else:
            # Try to load from environment variables
            env_config = config_loader.load_config_from_environment_variables()
            config.update(env_config)

        # Apply defaults for missing values
        for key, default_val in defaults.items():
            if key not in config or not config[key]:
                config[key] = default_val

        self._config_repository = ConfigRepository(config)

        # Create API client
        http_client = httpx.Client(
            timeout=self._config_repository.read_timeout(),
            follow_redirects=False,
        )

        self._api_client = ApiClient(
            client=http_client,
            api_endpoint_resolver=ApiEndpointResolver(),
            config_repository=self._config_repository,
            basic_token=self._config_repository.basic_token(),
            bearer_token=None,
        )

        return self

    def get_api_client(self) -> ApiClient:
        """
        Retrieves the ApiClient.

        Returns:
            The ApiClient

        Raises:
            SignNowApiException: If an error occurs during the retrieval of the ApiClient
        """
        if self._api_client is None:
            self.build()
        assert self._api_client is not None
        return self._api_client

    def authenticate(self) -> "Sdk":
        """
        Authenticates the SDK by sending a TokenPostRequest and setting the BearerToken.

        Returns:
            The authenticated SDK

        Raises:
            SignNowApiException: If an error occurs during the authentication
        """
        if self._api_client is None:
            self.build()

        assert self._config_repository is not None
        assert self._api_client is not None

        request = TokenPostRequest(
            user=self._config_repository.user(),
            password=self._config_repository.password(),
            scope=self.FULL_SCOPE,
            grant_type=self.GRANT_TYPE_BY_PASSWORD,
            code=self.EMPTY_CODE,
        )

        reply = self._api_client.send(request)
        response: TokenPostResponse = reply.get_response()

        bearer_token = BearerToken(
            access_token=response.access_token or "",
            refresh_token=response.refresh_token,
            expires=response.expires_in,
        )

        self._api_client.set_bearer_token(bearer_token)

        return self

    def with_bearer_token(self, bearer_token: BearerToken) -> "Sdk":
        """
        Sets the BearerToken for the ApiClient.

        Args:
            bearer_token: The BearerToken to be set

        Returns:
            The SDK with the set BearerToken
        """
        if self._api_client is None:
            self.build()

        assert self._api_client is not None
        self._api_client.set_bearer_token(bearer_token)
        return self

    def get_actual_bearer_token(self) -> Optional[BearerToken]:
        """
        Retrieves the actual BearerToken of the ApiClient.

        Returns:
            The actual BearerToken

        Raises:
            SignNowApiException: If an error occurs during the retrieval of the BearerToken
        """
        return self.get_api_client().get_bearer_token()

    def version(self) -> str:
        """Retrieves the version of the API."""
        return self.API_VERSION
