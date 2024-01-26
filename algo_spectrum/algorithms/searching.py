from typing import List, Optional, Any


def linear_search(target: Any, items: List[Any]) -> Optional[int]:
    """
    Perform linear search to find the target value in a list

    :param target: The value to search for.
    :param items: The list of items to search.
    :return: The index of the target if found, or None if not present.
    """
    for index, item in enumerate(items):
        if item == target:
            return index

    # Target value not found
    return None


def binary_search(target: Any, items: List[Any]) -> Optional[int]:
    """
    Perform binary search to find the target value in a list

    :param target: The value to search for.
    :param items: The list of items to search.
    :return: The index of the target if found, or None if not present.

    Algorithm:
    1. Initialize low and high pointers to the start and end of the list.
    2. While the low pointer is less than or equal to the high pointer:
    - Calculate the middle index.
    - Compare the value at the middle index with the target value:
    - If they are equal, return the middle index.
    - If the mid_value is less than the target,
    adjust the low pointer to mid + 1.
    - If the mid_value is greater than the target,
    adjust the high pointer to mid - 1.
    - If the target value is not found after the loop, return None.

    Time Complexity:
    - O(log n), where n is the number of elements in the list.

    Space Complexity:
    - O(1), as the algorithm uses a constant amount of extra space.

    Note:
    - The list must be sorted for binary search to work correctly.
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
