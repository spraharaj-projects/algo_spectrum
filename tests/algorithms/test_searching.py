"""
Test cases for various searching algorithms using pytest.
"""

from algorithms import (
    linear_search,
    sentinel_linear_search,
    binary_search,
    jump_search,
    interpolation_search,
)


def test_linear_search_found_int():
    """
    Test linear_search when the int target value is found.
    """
    result = linear_search(42, [1, 2, 42, 4, 5])
    assert result == 2


def test_linear_search_not_found_int():
    """
    Test linear_search when the int target value is not found.
    """
    result = linear_search(10, [1, 2, 3, 4, 5])
    assert result is None


def test_linear_search_found_string():
    """
    Test linear_search when the string target value is found.
    """
    result = linear_search(
        'apple',
        ['orange', 'banana', 'apple', 'pineapple', 'grapes']
    )
    assert result == 2


def test_linear_search_not_found_string():
    """
    Test linear_search when the string target value is not found.
    """
    result = linear_search(
        'strawberry',
        ['orange', 'banana', 'apple', 'pineapple', 'grapes']
    )
    assert result is None


def test_sentinel_linear_search_found_int():
    """
    Test sentinel_linear_search when the int target value is found.
    """
    result = sentinel_linear_search(42, [1, 2, 42, 4, 5])
    assert result == 2


def test_sentinel_linear_search_not_found_int():
    """
    Test sentinel_linear_search when the int target value is not found.
    """
    result = sentinel_linear_search(10, [1, 2, 3, 4, 5])
    assert result is None


def test_sentinel_linear_search_found_string():
    """
    Test sentinel_linear_search when the string target value is found.
    """
    result = sentinel_linear_search(
        'apple',
        ['orange', 'banana', 'apple', 'pineapple', 'grapes']
    )
    assert result == 2


def test_sentinel_linear_search_not_found_string():
    """
    Test sentinel_linear_search when the string target value is not found.
    """
    result = sentinel_linear_search(
        'strawberry',
        ['orange', 'banana', 'apple', 'pineapple', 'grapes']
    )
    assert result is None


def test_binary_search_found_int():
    """
    Test binary_search when the int target value is found.
    """
    result = binary_search(2, [1, 2, 3, 4, 5])
    assert result == 1


def test_binary_search_not_found_int():
    """
    Test binary_search when the int target value is not found.
    """
    result = binary_search(10, [1, 2, 3, 4, 5])
    assert result is None


def test_binary_search_found_string():
    """
    Test binary_search when the string target value is found.
    """
    result = binary_search(
        'grapes',
        ['apple', 'banana', 'grapes', 'orange', 'pineapple']
    )
    assert result == 2


def test_binary_search_not_found_string():
    """
    Test binary_search when the string target value is not found.
    """
    result = binary_search(
        'strawberry',
        ['orange', 'banana', 'apple', 'pineapple', 'grapes']
    )
    assert result is None


def test_jump_search_found_int():
    """
    Test jump_search when the int target value is found.
    """
    result = jump_search(2, [1, 2, 3, 4, 5])
    assert result == 1


def test_jump_search_not_found_int():
    """
    Test jump_search when the int target value is not found.
    """
    result = jump_search(10, [1, 2, 3, 4, 5])
    assert result is None


def test_jump_search_found_string():
    """
    Test jump_search when the string target value is found.
    """
    result = jump_search(
        'grapes',
        ['apple', 'banana', 'grapes', 'orange', 'pineapple']
    )
    assert result == 2


def test_jump_search_not_found_string():
    """
    Test jump_search when the string target value is not found.
    """
    result = jump_search(
        'strawberry',
        ['orange', 'banana', 'apple', 'pineapple', 'grapes']
    )
    assert result is None


def test_interpolation_search_found_int():
    """
    Test interpolation_search when the int target value is found.
    """
    result = interpolation_search(2, [1, 2, 3, 4, 5])
    assert result == 1


def test_interpolation_search_not_found_int():
    """
    Test interpolation_search when the int target value is not found.
    """
    result = interpolation_search(10, [1, 2, 3, 4, 5])
    assert result is None
