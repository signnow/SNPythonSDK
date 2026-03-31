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
class DownloadDocumentGroupPostResponse:
    """
    Represents the response received after a request to download a document group.
    """

    file_path: Optional[Path] = None
    """The file path of the downloaded document group."""
