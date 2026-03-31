"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

import os
from typing import Dict

from signnow.core.token import BasicToken


class ConfigDefaults:
    """This class provides default values for signNow SDK configuration."""

    SIGNNOW_API_HOST = "https://api.signnow.com"
    BASIC_TOKEN = ""
    USERNAME = ""
    PASSWORD = ""
    DOWNLOADS_DIR = "./downloads"

    # Environment variables
    ENV_VAR_HOST = "SIGNNOW_API_HOST"
    ENV_VAR_BASIC_TOKEN = "SIGNNOW_API_BASIC_TOKEN"
    ENV_VAR_USERNAME = "SIGNNOW_API_USERNAME"
    ENV_VAR_PASSWORD = "SIGNNOW_API_PASSWORD"
    ENV_DOWNLOADS_DIR = "SIGNNOW_DOWNLOADS_DIR"

    @staticmethod
    def get_environment_variable_names() -> list:
        """Returns list of environment variables that keep API secrets."""
        return [
            ConfigDefaults.ENV_VAR_HOST,
            ConfigDefaults.ENV_VAR_BASIC_TOKEN,
            ConfigDefaults.ENV_VAR_USERNAME,
            ConfigDefaults.ENV_VAR_PASSWORD,
            ConfigDefaults.ENV_DOWNLOADS_DIR,
        ]

    @staticmethod
    def get_defaults() -> Dict[str, str]:
        """Returns default values for SDK configuration."""
        return {
            ConfigDefaults.ENV_VAR_HOST: ConfigDefaults.SIGNNOW_API_HOST,
            ConfigDefaults.ENV_VAR_BASIC_TOKEN: ConfigDefaults.BASIC_TOKEN,
            ConfigDefaults.ENV_VAR_USERNAME: ConfigDefaults.USERNAME,
            ConfigDefaults.ENV_VAR_PASSWORD: ConfigDefaults.PASSWORD,
            ConfigDefaults.ENV_DOWNLOADS_DIR: ConfigDefaults.DOWNLOADS_DIR,
        }


class ConfigLoader:
    """This class reads and parses signNow SDK configuration file."""

    @staticmethod
    def load(file_path: str) -> Dict[str, str]:
        """
        Loads the configuration file from the provided file path and parses it into a dict.
        Each line in the file should represent a key-value pair, separated by an equals sign.
        Lines starting with a hash sign are considered comments and are ignored. Empty lines are also ignored.

        Args:
            file_path: The path to the configuration file

        Returns:
            A dict containing the key-value pairs from the configuration file

        Raises:
            SignNowApiException: If an error occurs while reading the file
        """
        from signnow.core.exception import SignNowApiException

        config_map = {}
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("#") or not line:
                        continue
                    if "=" in line:
                        key, value = line.split("=", 1)
                        config_map[key.strip()] = value.strip()
        except IOError as e:
            raise SignNowApiException(
                f"An error occurred while reading the signNow SDK configuration file: {file_path}. "
                f"Please ensure the file exists, is accessible, and is correctly formatted.",
                cause=e,
            )
        return config_map

    @staticmethod
    def load_config_from_environment_variables() -> Dict[str, str]:
        """
        Load API credentials from environment variables if they exist.

        Returns:
            A dict of SDK configuration parsed from environment variables
        """
        config = {}
        env_vars = ConfigDefaults.get_environment_variable_names()
        for env_var in env_vars:
            value = os.getenv(env_var)
            if value:
                config[env_var] = value
        return config


class ConfigRepository:
    """This class represents all the signNow SDK API configuration file entries as a repository."""

    READ_TIMEOUT = 15
    CLIENT_NAME = "SignNowApiClient/v3.0.0 (Python)"

    def __init__(self, config_map: Dict[str, str]):
        """
        Constructor for ConfigRepository.

        Args:
            config_map: A dict of configuration entries
        """
        self._config_map = config_map

    def host(self) -> str:
        """Returns the host from the configuration map."""
        return self._config_map.get(
            ConfigDefaults.ENV_VAR_HOST, ConfigDefaults.SIGNNOW_API_HOST
        )

    def basic_token(self) -> BasicToken:
        """Returns the basic token from the configuration map."""
        token = self._config_map.get(
            ConfigDefaults.ENV_VAR_BASIC_TOKEN, ConfigDefaults.BASIC_TOKEN
        )
        return BasicToken(token)

    def user(self) -> str:
        """Returns the user from the configuration map."""
        return self._config_map.get(
            ConfigDefaults.ENV_VAR_USERNAME, ConfigDefaults.USERNAME
        )

    def password(self) -> str:
        """Returns the password from the configuration map."""
        return self._config_map.get(
            ConfigDefaults.ENV_VAR_PASSWORD, ConfigDefaults.PASSWORD
        )

    def project_directory(self) -> str:
        """Returns the project directory."""
        return os.getcwd()

    def downloads_directory(self) -> str:
        """Returns the path to save downloaded files from the configuration map."""
        downloads_dir = self._config_map.get(
            ConfigDefaults.ENV_DOWNLOADS_DIR, ConfigDefaults.DOWNLOADS_DIR
        )

        if downloads_dir.startswith("."):
            downloads_dir = downloads_dir.replace(".", self.project_directory(), 1)

        return downloads_dir

    def client_name(self) -> str:
        """Returns the client name."""
        return self.CLIENT_NAME

    def read_timeout(self) -> int:
        """Returns the read timeout."""
        return self.READ_TIMEOUT
