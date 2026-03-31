"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import Optional

from signnow.core.api_client import ApiClient
from signnow.sdk import Sdk


class SdkFactory:
    """Factory class for creating instances of ApiClient."""

    @staticmethod
    def create_api_client(config_path: Optional[str] = None) -> ApiClient:
        """
        Creates an instance of ApiClient using default or provided configuration.

        Args:
            config_path: The path to the configuration file (optional)

        Returns:
            ApiClient instance

        Raises:
            SignNowApiException: If there is an error during ApiClient creation
        """
        sdk = Sdk(config_path) if config_path else Sdk()
        return sdk.build().authenticate().get_api_client()

    @staticmethod
    def create_api_client_with_bearer_token(
        bearer_token: Optional[str] = None,
    ) -> ApiClient:
        """
        Creates an instance of ApiClient using the provided bearer token.

        Args:
            bearer_token: The bearer token to be used for authentication (optional)

        Returns:
            ApiClient instance

        Raises:
            SignNowApiException: If there is an error during ApiClient creation
        """
        from signnow.core.token import BearerToken

        if not bearer_token:
            return SdkFactory.create_api_client()

        sdk = Sdk()
        token = BearerToken(bearer_token)
        return sdk.build().with_bearer_token(token).get_api_client()
