"""
Tests for collection classes.

This module contains tests for collection classes including:
- TypedCollection for generic typed collections
- StringCollection for string collections
- FloatCollection for float collections

These tests verify that collections can be properly created, manipulated,
and converted to various formats.
"""

from signnow.core.collection import FloatCollection, StringCollection, TypedCollection


def test_typed_collection_create_update_remove():
    """
    Test TypedCollection create, update, and remove operations.

    Verifies that:
    - TypedCollection can be created and elements can be added
    - Elements can be retrieved, updated, and removed
    - Collection size and emptiness checks work correctly
    """
    fruits = TypedCollection[str]()

    assert fruits.is_empty()

    fruits.add("Apple")
    fruits.add("Pineapple")

    assert not fruits.is_empty()
    assert fruits.size() == 2
    assert fruits.contains("Apple")
    assert not fruits.contains("not_found")
    assert fruits.get(0) == "Apple"
    assert fruits.get(1) == "Pineapple"
    assert fruits.index_of("Apple") == 0
    assert fruits.index_of("Pineapple") == 1

    fruits.remove("Pineapple")
    assert not fruits.contains("Pineapple")
    assert fruits.size() == 1

    fruits.set(0, "Banana")
    assert fruits.size() == 1
    assert fruits.get(0) == "Banana"

    fruits.clear()
    assert fruits.size() == 0
    assert fruits.is_empty()


def test_typed_collection_to_array_and_to_json():
    """
    Test TypedCollection toArray and toJson methods.

    Verifies that:
    - Collection can be converted to array
    - Collection can be converted to JSON string
    """
    items = TypedCollection[str]()

    items.add("item1")
    items.add("item2")

    array = items.to_array()
    assert array[0] == "item1"
    assert array[1] == "item2"

    json_str = items.to_json()
    assert "item1" in json_str
    assert "item2" in json_str


def test_typed_collection_navigation():
    """
    Test TypedCollection navigation methods (first, last, current, next, rewind).

    Verifies that:
    - Navigation methods work correctly
    - Current index tracking works
    """
    items = TypedCollection[str]()

    items.add("first")
    items.add("second")
    items.add("third")

    first = items.first()
    last = items.last()
    assert first == "first"
    assert last == "third"

    items.next()
    middle = items.current()
    middle_key = items.key()
    assert middle == "second"
    assert middle_key == 1

    items.next()
    last_item = items.current()
    assert last_item == "third"

    items.rewind()
    first_item = items.current()
    assert first_item == "first"


def test_typed_collection_search():
    """
    Test TypedCollection search operations.

    Verifies that:
    - Contains method works correctly
    - IndexOf method works correctly
    """
    subjects = TypedCollection[str]()

    subjects.add("table")
    subjects.add("chair")
    subjects.add("cup")

    assert subjects.contains("table")
    assert subjects.contains("chair")
    assert subjects.contains("cup")
    assert not subjects.contains("draw")

    assert subjects.index_of("table") == 0
    assert subjects.index_of("chair") == 1
    assert subjects.index_of("cup") == 2


def test_typed_collection_merge():
    """
    Test TypedCollection merge operations.

    Verifies that:
    - Merge method combines collections
    - RetainAll method keeps only common elements
    - RemoveAll method removes common elements
    """
    items1 = TypedCollection[str]()
    items2 = TypedCollection[str]()

    items1.add("item1")
    items2.add("item2")
    items1.merge(items2)
    assert items1.size() == 2
    assert items2.size() == 1

    items1.retain_all(items2)
    item = items1.first()
    assert items1.size() == 1
    assert item == "item2"

    items1.remove_all(items2)
    assert items1.is_empty()


def test_typed_collection_map():
    """
    Test TypedCollection map method.

    Verifies that:
    - Map method applies function to each element
    - Returns new collection with transformed elements
    """
    numbers = TypedCollection[int]()
    numbers.add(1)
    numbers.add(2)
    numbers.add(3)

    doubled_numbers = numbers.map(lambda x: x * 2)
    assert doubled_numbers.get(0) == 2
    assert doubled_numbers.get(1) == 4
    assert doubled_numbers.get(2) == 6


def test_typed_collection_reduce():
    """
    Test TypedCollection reduce method.

    Verifies that:
    - Reduce method accumulates values correctly
    """
    numbers = TypedCollection[int]()
    numbers.add(15)
    numbers.add(25)
    numbers.add(35)

    result = numbers.reduce(0, lambda acc, x: acc + x)
    assert result == 75


def test_typed_collection_slice():
    """
    Test TypedCollection slice method.

    Verifies that:
    - Slice method returns elements from specified range
    """
    cities = TypedCollection[str]()
    cities.add("Sidney")
    cities.add("Kyiv")
    cities.add("Warsaw")
    cities.add("Berlin")
    cities.add("New York")
    cities.add("Tokyo")

    european_cities = cities.slice(1, 4)
    assert european_cities.size() == 3
    assert european_cities.get(0) == "Kyiv"
    assert european_cities.get(1) == "Warsaw"
    assert european_cities.get(2) == "Berlin"


def test_typed_collection_filter():
    """
    Test TypedCollection filter method.

    Verifies that:
    - Filter method returns elements matching predicate
    """
    numbers = TypedCollection[int]()
    numbers.add(1)
    numbers.add(2)
    numbers.add(3)
    numbers.add(4)
    numbers.add(5)
    numbers.add(6)
    numbers.add(7)

    filtered_numbers = numbers.filter(lambda x: x % 2 == 0)
    assert filtered_numbers.size() == 3
    assert filtered_numbers.get(0) == 2
    assert filtered_numbers.get(1) == 4
    assert filtered_numbers.get(2) == 6


def test_typed_collection_keys_values():
    """
    Test TypedCollection keys and values methods.

    Verifies that:
    - Keys method returns list of indices
    - Values method returns list of elements
    """
    drinks = TypedCollection[str]()
    drinks.add("Juice")
    drinks.add("Tea")
    drinks.add("Coffee")
    drinks.add("Soda")

    keys = drinks.keys()
    assert keys[0] == 0
    assert keys[1] == 1
    assert keys[2] == 2
    assert keys[3] == 3

    values = drinks.values()
    assert values[0] == "Juice"
    assert values[1] == "Tea"
    assert values[2] == "Coffee"
    assert values[3] == "Soda"


def test_string_collection():
    """
    Test StringCollection operations.

    Verifies that:
    - StringCollection can be created and used
    - Elements can be added and converted to array
    """
    roles = StringCollection()

    roles.add("Product Manager")
    roles.add("Java Developer")
    roles.add("Software Engineer")

    array = roles.to_array()
    expected = ["Product Manager", "Java Developer", "Software Engineer"]
    assert array == expected


def test_float_collection():
    """
    Test FloatCollection operations.

    Verifies that:
    - FloatCollection can be created and used
    - Float elements can be added and converted to array
    """
    floats = FloatCollection()
    floats.add(1.0)
    floats.add(15.5)

    array = floats.to_array()
    expected = [1.0, 15.5]
    assert array == expected
