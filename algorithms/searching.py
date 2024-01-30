"""
Searching Module
================

The Searching Module in Algo Spectrum provides implementations of various
searching algorithms, each designed to efficiently locate elements within an
array or other collection.

Algorithms Included
-------------------

1. **Linear Search** [:func:`algorithms.searching.linear_search`]
2. **Sentinel Search:** [:func:`algorithms.searching.sentinel_linear_search`]
3. **Binary Search:** [:func:`algorithms.searching.binary_search`]
4. **Jump Search:** [:func:`algorithms.searching.jump_search`]
5. **Interpolation Search:** [:func:`algorithms.searching.interpolation_search`]
6. **Exponential Search:** [:func:`algorithms.searching.exponential_search`]
7. **Fibonacci Search:** [:func:`algorithms.searching.fibonacci_search`]
8. **Ternary Search:** [:func:`algorithms.searching.ternary_search`]
"""
from typing import List, Optional, Any, Union


def linear_search(target: Any, items: List[Any]) -> Optional[int]:
    """
    Linear search sequentially scans through a collection, comparing each
    element with the target value until a match is found or the end of the
    collection is reached, making it suitable for small or unsorted datasets.

    :param Any target: The value to search for.
    :param Any items: The list of items to search.
    :return: The index of the target if found, or None if not present.
    :rtype: Optional[int]
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
    :rtype: Optional[int]
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
    :param List[Any] items: The list of items to search.
    :return: The index of the target if found, or None if not present.
    :rtype: Optional[int]
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


def jump_search(target: Any, items: List[Any]) -> Optional[int]:
    """
    Perform Jump Search to find the index of the target element in the given
    sorted array.

    It works on the principle of linear search but improves the efficiency by
    jumping a fixed number of steps ahead in each iteration, thus reducing the
    number of comparisons. This algorithm requires the array to be sorted
    beforehand.

    :param Any target: The target element to search for.
    :param List[Any] items: The sorted list or array to search in.
    :return: The index of the target element if found, else None.
    :rtype: Optional[int]
    """
    n = len(items)
    step = int(n**0.5)  # Determine the step size for jumping

    prev = 0
    while items[min(step, n) - 1] < target:
        prev = step
        step += int(n**0.5)
        if prev >= n:
            return None

    while items[prev] < target:
        prev += 1
        if prev == min(step, n):
            return None

    if items[prev] == target:
        return prev

    return None


def interpolation_search(
        target: Union[int, float, complex],
        items: List[Union[int, float, complex]]
) -> Optional[int]:
    """
    Perform Interpolation Search to find the index of the target element in the
    given sorted array.

    Interpolation search is an algorithm for finding a specific value within an
    array that is sorted in ascending order. It works by making a linear
    interpolation to estimate the position of the target value within the array,
    then performs binary search in the estimated range. This algorithm is most
    effective when the elements in the array are uniformly distributed.

    :param int | float | complex target: The value to search for.
    :param List[int | float | complex] items: The list of items to search.
    :return: The index of the target if found, or None if not present.
    :rtype: Optional[int]
    """
    low = 0
    high = len(items) - 1

    while low <= high and items[low] <= target <= items[high]:
        if low == high:
            if items[low] == target:
                return low
            return None

        pos = low + int(
            (high - low) /
            (items[high] - items[low]) *
            (target - items[low])
        )

        if items[pos] == target:
            return pos
        elif items[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return None


def exponential_search(target: Any, items: List[Any]) -> Optional[int]:
    """
    Perform exponential search to find the index of the target element in the
    given sorted array.

    :param Any target: The value to search for.
    :param List[Any] items: The list of items to search.
    :return: The index of the target if found, or None if not present.
    :rtype: Optional[int]
    """
    if not items:
        return None

    # If the target is smaller than the first element or larger than the last
    # element, it cannot be in the array
    if target < items[0] or target > items[-1]:
        return None

    i = 1

    while i < len(items) and items[i] <= target:
        i *= 2

    # Perform binary search within the range found by exponential search
    left, right = i // 2, min(i, len(items))
    while left <= right:
        mid = left + (right - left) // 2
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None


def fibonacci_search(target: int, items: List[int]) -> Optional[int]:
    """
    Perform fibonacci search to find the index of the target element in the
    given sorted array.

    :param int target: The value to search for.
    :param List[int] items: The list of items to search.
    :return: The index of the target if found, or None if not present.
    :rtype: Optional[int]
    """
    if not items:
        return None

        # Define Fibonacci numbers
    fib_m2, fib_m1 = 0, 1
    fib = fib_m1 + fib_m2

    # Find the smallest Fibonacci number greater than or equal to the length
    # of the array
    while fib < len(items):
        fib_m2, fib_m1 = fib_m1, fib
        fib = fib_m1 + fib_m2

    # Initialize variables
    offset = -1

    # Perform search
    while fib > 1:
        # Calculate the next Fibonacci number to the left of fib
        i = min(offset + fib_m2, len(items) - 1)

        # If the target element is greater than the current element, move the
        # offset and Fibonacci numbers to the right
        if items[i] < target:
            fib, fib_m1, fib_m2 = fib_m1, fib_m2, fib - fib_m1
            offset = i

        # If the target element is less than the current element, move the
        # offset and Fibonacci numbers to the left
        elif items[i] > target:
            fib, fib_m1, fib_m2 = fib_m2, fib_m1 - fib_m2, fib_m2 - fib_m1
        else:
            return i

    # If the target element is not found, return None
    if fib_m1 and items[offset + 1] == target:
        return offset + 1
    return None


def ternary_search(target: Any, items: List[Any]) -> Optional[int]:
    """
    Perform ternary search to find the index of the target element in the
    given sorted array.

    :param Any target: The value to search for.
    :param List[Any] items: The list of items to search.
    :return: The index of the target if found, or None if not present.
    :rtype: Optional[int]
    """
    if not items:
        return None

    left, right = 0, len(items) - 1

    while left <= right:
        # Divide the array into three parts
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if items[mid1] == target:
            return mid1
        elif items[mid2] == target:
            return mid2

        # If the target is in the first third
        elif items[mid1] > target:
            right = mid1 - 1
        # If the target is in the last third
        elif items[mid2] < target:
            left = mid2 + 1

        # If the target is in the middle third
        else:
            left = mid1 + 1
            right = mid2 - 1

    return None
