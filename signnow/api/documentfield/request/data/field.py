"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass
from typing import Dict


@dataclass
class Field:
    """
    Represents a Field with a name and prefilled text.
    """

    field_name: str
    """The name of the field."""

    prefilled_text: str
    """The prefilled text of the field."""

    def to_dict(self) -> Dict[str, str]:
        """
        Converts this Field to a dictionary with keys "field_name" and "prefilled_text".

        Returns:
            A dictionary representation of this Field.
        """
        return {
            "field_name": self.field_name,
            "prefilled_text": self.prefilled_text,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, str]) -> "Field":
        """
        Constructs a new Field from the specified dictionary.
        The dictionary must contain keys "field_name" and "prefilled_text".

        Args:
            data: The dictionary to convert to a Field.

        Returns:
            A new Field constructed from the specified dictionary.
        """
        return cls(
            field_name=data.get("field_name", ""),
            prefilled_text=data.get("prefilled_text", ""),
        )
