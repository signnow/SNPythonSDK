"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import List

from signnow.api.document.request.data.field import Field


class FieldCollection:
    """
    Represents a collection of Field objects.
    """

    def __init__(self):
        """Constructs an empty FieldCollection."""
        self._fields: List[Field] = []

    def add(self, field: Field) -> None:
        """
        Adds a Field to the collection.

        Args:
            field: The Field to add.
        """
        self._fields.append(field)

    def to_list(self) -> List[dict]:
        """
        Converts this FieldCollection to a list of dictionaries.

        Returns:
            A list of dictionaries representing the fields.
        """
        return [field.to_dict() for field in self._fields]

    def __iter__(self):
        """Returns an iterator over the fields."""
        return iter(self._fields)

    def __len__(self) -> int:
        """Returns the number of fields in the collection."""
        return len(self._fields)

    def __getitem__(self, index: int) -> Field:
        """Returns the field at the specified index."""
        return self._fields[index]
