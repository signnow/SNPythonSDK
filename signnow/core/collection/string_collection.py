"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from signnow.core.collection.typed_collection import TypedCollection


class StringCollection(TypedCollection[str]):
    """
    This class represents a collection of Strings.
    It extends the TypedCollection class with a type parameter of String.

    See Also:
        signnow.core.collection.TypedCollection
    """

    def __init__(self):
        """Default constructor for StringCollection."""
        super().__init__()
