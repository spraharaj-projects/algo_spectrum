"""
Algo Spectrum: Searching Module

This module contains various searching algorithms for finding elements within a
collection.

Available Algorithms:
- Linear Search
- Sentinel Linear Search
- Binary Search
- ... (other searching algorithms)

Usage:
1. Import the module in your Python script:
    from algo_spectrum import binary_search, linear_search

2. Utilize the provided searching algorithms:
    - Linear Search:
      result = linear_search(target_element, array)

    - Sentinel Linear Search:
      result = linear_search(target_element, array)

    - Binary Search:
      result = binary_search(target_element, sorted_array)

Each algorithm is designed for specific scenarios, providing flexibility for
different use cases. Refer to the individual algorithm docstrings for detailed
usage instructions and examples.

For more information and updates, visit the Algo Spectrum GitHub repository:
https://github.com/your-username/algo-spectrum
"""
from typing import List, Optional, Any


def linear_search(target: Any, items: List[Any]) -> Optional[int]:
    """
    Perform linear search to find the target value in a list.

    :param Any target: The value to search for.
    :param Any items: The list of items to search.
    :return int: The index of the target if found, or None if not present.
    """
    for index, item in enumerate(items):
        if item == target:
            return index

    # Target value not found
    return None


def sentinel_linear_search(target: Any, items: List[Any]) -> Optional[int]:
    """
    Perform sentinel search to find the target value in a list.

    :param Any target: The value to search for.
    :param Any items: The list of items to search.
    :return int: The index of the target if found, or None if not present.
    """
    n = len(items)  # Length of items list
    last = items[n - 1]  # store last element of list
    items[n - 1] = target  # assign target as last element of list
    index = 0
    while items[index] != target:
        index += 1

    items[n - 1] = last  # revert back last element of list

    if index < n - 1 or items[n - 1] == target:
        return index

    # Target value not found
    return None


def binary_search(target: Any, items: List[Any]) -> Optional[int]:
    """
    Perform binary search to find the target value in a list

    :param target: The value to search for.
    :param items: The list of items to search.
    :return: The index of the target if found, or None if not present.
    """
    low, high = 0, len(items) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = items[mid]

        if mid_value == target:
            return mid
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

    # Target value not found
    return None
