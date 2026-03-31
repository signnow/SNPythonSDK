"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass
class ProxyFileResponse:
    """
    This class represents the response received after a request to proxy any unimplemented endpoint
    that returns a file.
    """

    file_path: str
    """The file path of the downloaded file."""

    def get_file(self) -> Path:
        """
        Gets the downloaded file.

        Returns:
            The Path object representing the downloaded file
        """
        return Path(self.file_path)
