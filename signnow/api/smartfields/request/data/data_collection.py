"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from typing import List

from signnow.api.smartfields.request.data.data import Data


class DataCollection:
    """
    Represents a collection of Data objects.
    """

    def __init__(self):
        """Default constructor for DataCollection."""
        self._data: List[Data] = []

    def add(self, data: Data) -> None:
        """
        Adds a Data object to the collection.

        Args:
            data: The Data object to add.
        """
        self._data.append(data)

    def to_list(self) -> List[dict]:
        """
        Converts this DataCollection to a list of dictionaries.

        Returns:
            A list of dictionaries representing the data.
        """
        return [item.to_dict() for item in self._data]

    def __iter__(self):
        """Returns an iterator over the data."""
        return iter(self._data)

    def __len__(self) -> int:
        """Returns the number of data items in the collection."""
        return len(self._data)

    def __getitem__(self, index: int) -> Data:
        """Returns the data item at the specified index."""
        return self._data[index]
