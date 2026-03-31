"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from signnow.core.collection.typed_collection import TypedCollection


class FloatCollection(TypedCollection[float]):
    """
    This class represents a collection of Float objects.
    It extends the TypedCollection class by specifying the type of objects it can contain.

    See Also:
        signnow.core.collection.TypedCollection
    """

    def __init__(self):
        """Default constructor for FloatCollection."""
        super().__init__()
