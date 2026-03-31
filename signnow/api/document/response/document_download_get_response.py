"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class DocumentDownloadGetResponse:
    """
    This class represents the response received after a document download request.
    The file is downloaded and saved locally.
    """

    file_path: Optional[str] = None

    def get_file(self) -> Optional[Path]:
        """
        Gets the downloaded file path.

        Returns:
            The Path object representing the downloaded file
        """
        return Path(self.file_path) if self.file_path else None
