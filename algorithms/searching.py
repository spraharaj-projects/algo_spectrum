from typing import List, Optional, Any


def linear_search(target: Any, items: List[Any]) -> Optional[int]:
    """
    Linear search sequentially scans through a collection, comparing each
    element with the target value until a match is found or the end of the
    collection is reached, making it suitable for small or unsorted datasets.

    :param Any target: The value to search for.
    :param Any items: The list of items to search.
    :return: The index of the target if found, or None if not present.
    :rtype: int
    """
    for index, item in enumerate(items):
        if item == target:
            return index

    # Target value not found
    return None


def sentinel_linear_search(target: Any, items: List[Any]) -> Optional[int]:
    """
    Sentinel linear search optimizes the standard linear search algorithm by
    reducing comparisons within the loop, enhancing its efficiency for
    searching unsorted collections.

    :param Any target: The value to search for.
    :param Any items: The list of items to search.
    :return: The index of the target if found, or None if not present.
    :rtype: int
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
    Binary search quickly finds a target value within a sorted collection by
    repeatedly dividing the search space in half, resulting in logarithmic
    time complexity.

    :param Any target: The value to search for.
    :param Any items: The list of items to search.
    :return: The index of the target if found, or None if not present.
    :rtype: int
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
