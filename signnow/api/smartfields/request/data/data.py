"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass
from typing import Dict


@dataclass
class Data:
    """
    Represents the Data object in the signNow API.
    """

    field_name: str
    """The name of the field."""

    def to_dict(self) -> Dict[str, str]:
        """
        Converts the Data object to a dictionary.

        Returns:
            A dictionary representation of the Data object.
        """
        return {
            "field_name": self.field_name,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, str]) -> "Data":
        """
        Creates a new Data object from a dictionary.

        Args:
            data: The dictionary to convert to a Data object.

        Returns:
            A new Data object.
        """
        return cls(
            field_name=data.get("field_name", ""),
        )
