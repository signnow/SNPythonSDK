"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

import json
from typing import Any, Callable, Generic, Iterator, List, TypeVar

T = TypeVar("T")


class TypedCollection(Generic[T]):
    """
    A typed collection class that provides methods for managing collections of a specific type.

    Args:
        T: The type of elements in this collection
    """

    def __init__(self):
        """Default constructor that initializes an empty list of elements."""
        self._elements: List[T] = []
        self._current_index: int = 0

    def current(self) -> T:
        """
        Returns the current element in the collection.

        Returns:
            The current element

        Raises:
            IndexError: If the current index is out of bounds
        """
        if 0 <= self._current_index < len(self._elements):
            return self._elements[self._current_index]
        raise IndexError("Current index is out of bounds")

    def key(self) -> int:
        """
        Returns the current index of the collection.

        Returns:
            The current index
        """
        return self._current_index

    def next(self) -> None:
        """Moves the current index to the next element if it exists."""
        if self._current_index < len(self._elements) - 1:
            self._current_index += 1

    def rewind(self) -> None:
        """Resets the current index to the start of the collection."""
        self._current_index = 0

    def contains(self, element: Any) -> bool:
        """
        Checks if the collection contains the specified element.

        Args:
            element: The element to be checked

        Returns:
            True if the collection contains the element, False otherwise
        """
        return element in self._elements

    def index_of(self, element: T) -> int:
        """
        Returns the index of the specified element in the collection.

        Args:
            element: The element to find

        Returns:
            The index of the element, or -1 if the collection does not contain the element
        """
        try:
            return self._elements.index(element)
        except ValueError:
            return -1

    def get(self, key: int) -> T:
        """
        Returns the element at the specified position in the collection.

        Args:
            key: Index of the element to return

        Returns:
            The element at the specified position

        Raises:
            IndexError: If the index is out of range
        """
        if 0 <= key < len(self._elements):
            return self._elements[key]
        raise IndexError("Index is out of bounds.")

    def set(self, key: int, value: T) -> None:
        """
        Replaces the element at the specified position in the collection with the specified element.

        Args:
            key: Index of the element to replace
            value: Element to be stored at the specified position

        Raises:
            IndexError: If the index is out of range
        """
        if 0 <= key < len(self._elements):
            self._elements[key] = value
        elif key == len(self._elements):
            self._elements.append(value)
        else:
            raise IndexError("Index is out of bounds.")

    def first(self) -> T:
        """
        Returns the first element in the collection.

        Returns:
            The first element

        Raises:
            ValueError: If the collection is empty
        """
        if not self._elements:
            raise ValueError("Collection is empty.")
        return self._elements[0]

    def last(self) -> T:
        """
        Returns the last element in the collection.

        Returns:
            The last element

        Raises:
            ValueError: If the collection is empty
        """
        if not self._elements:
            raise ValueError("Collection is empty.")
        return self._elements[-1]

    def merge(self, other: "TypedCollection[T]") -> None:
        """
        Merges the specified collection into the current collection.

        Args:
            other: The collection to be merged
        """
        if other is not None:
            self._elements.extend(other._elements)

    def keys(self) -> List[int]:
        """
        Returns a list of all keys in the collection.

        Returns:
            A list of all keys (indices)
        """
        return list(range(len(self._elements)))

    def values(self) -> List[T]:
        """
        Returns a list of all values in the collection.

        Returns:
            A list of all values
        """
        return list(self._elements)

    def to_array(self) -> List[T]:
        """
        Returns a list containing all the elements in the collection.

        Returns:
            A list containing all the elements
        """
        return list(self._elements)

    def to_json(self) -> str:
        """
        Converts the collection to a JSON string.

        Returns:
            A JSON string representation of the collection
        """
        try:
            return json.dumps(self._elements)
        except (TypeError, ValueError):
            return "[]"

    def map(self, mapper: Callable[[T], T]) -> "TypedCollection[T]":
        """
        Applies the specified function to each element in the collection and returns a new collection.

        Args:
            mapper: A function to apply to each element

        Returns:
            A new collection with the transformed elements
        """
        result = TypedCollection[T]()
        for element in self._elements:
            result.add(mapper(element))
        return result

    def reduce(self, identity: T, accumulator: Callable[[T, T], T]) -> T:
        """
        Accumulates value starting with the initial value and applying the specified function.

        Args:
            identity: The initial value
            accumulator: A function for combining two values

        Returns:
            The result of the accumulation
        """
        result = identity
        for element in self._elements:
            result = accumulator(result, element)
        return result

    def slice(self, from_index: int, to_index: int) -> "TypedCollection[T]":
        """
        Returns a new collection containing elements from the specified range.

        Args:
            from_index: Low endpoint (inclusive) of the slice
            to_index: High endpoint (exclusive) of the slice

        Returns:
            A new collection containing the specified range

        Raises:
            IndexError: If an endpoint index value is out of range
        """
        if from_index < 0 or to_index > len(self._elements) or from_index > to_index:
            raise IndexError("Invalid slice indices")
        sliced_collection = TypedCollection[T]()
        sliced_collection._elements = self._elements[from_index:to_index]
        return sliced_collection

    def filter(self, predicate: Callable[[T], bool]) -> "TypedCollection[T]":
        """
        Returns a new collection containing elements that match the given predicate.

        Args:
            predicate: A predicate to apply to each element

        Returns:
            A new collection containing the matched elements
        """
        filtered_collection = TypedCollection[T]()
        for element in self._elements:
            if predicate(element):
                filtered_collection.add(element)
        return filtered_collection

    def size(self) -> int:
        """
        Returns the number of elements in the collection.

        Returns:
            The number of elements
        """
        return len(self._elements)

    def is_empty(self) -> bool:
        """
        Checks if the collection is empty.

        Returns:
            True if the collection is empty, False otherwise
        """
        return len(self._elements) == 0

    def contains_all(self, other_collection: "TypedCollection[T]") -> bool:
        """
        Checks if the collection contains all the elements in the specified collection.

        Args:
            other_collection: Collection to be checked for containment

        Returns:
            True if this collection contains all the elements in the specified collection
        """
        if other_collection is None:
            return False
        return all(item in self._elements for item in other_collection._elements)

    def add(self, value: T) -> bool:
        """
        Adds the specified element to the collection.

        Args:
            value: Element to be added to the collection

        Returns:
            True (always, as list.append always succeeds)
        """
        self._elements.append(value)
        return True

    def remove(self, value: Any) -> bool:
        """
        Removes a single instance of the specified element from the collection, if it is present.

        Args:
            value: Element to be removed from the collection, if present

        Returns:
            True if an element was removed as a result of this call
        """
        try:
            self._elements.remove(value)
            return True
        except ValueError:
            return False

    def add_all(self, other_collection: "TypedCollection[T]") -> bool:
        """
        Adds all the elements in the specified collection to the collection.

        Args:
            other_collection: Collection containing elements to be added

        Returns:
            True if this collection changed as a result of the call
        """
        if other_collection is None:
            return False
        old_size = len(self._elements)
        self._elements.extend(other_collection._elements)
        return len(self._elements) > old_size

    def remove_all(self, other_collection: "TypedCollection[T]") -> bool:
        """
        Removes all the collection's elements that are also contained in the specified collection.

        Args:
            other_collection: Collection containing elements to be removed

        Returns:
            True if this collection changed as a result of the call
        """
        if other_collection is None:
            return False
        old_size = len(self._elements)
        self._elements = [
            item for item in self._elements if item not in other_collection._elements
        ]
        return len(self._elements) < old_size

    def retain_all(self, other_collection: "TypedCollection[T]") -> bool:
        """
        Retains only the elements in the collection that are contained in the specified collection.

        Args:
            other_collection: Collection containing elements to be retained

        Returns:
            True if this collection changed as a result of the call
        """
        if other_collection is None:
            return False
        old_size = len(self._elements)
        self._elements = [
            item for item in self._elements if item in other_collection._elements
        ]
        return len(self._elements) < old_size

    def clear(self) -> None:
        """Removes all the elements from the collection."""
        self._elements.clear()
        self._current_index = 0

    def __iter__(self) -> Iterator[T]:
        """Returns an iterator over the elements in the collection."""
        return iter(self._elements)

    def __len__(self) -> int:
        """Returns the number of elements in the collection."""
        return len(self._elements)

    def __getitem__(self, index: int) -> T:
        """Returns the element at the specified index."""
        return self.get(index)

    def __contains__(self, element: Any) -> bool:
        """Checks if the collection contains the specified element."""
        return self.contains(element)
