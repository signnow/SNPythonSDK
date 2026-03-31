"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass


@dataclass
class DocumentDownloadLinkPostResponse:
    """
    Represents the response from the Document Download Link Post API.
    """

    link: str = ""
    """The link to download the document."""
