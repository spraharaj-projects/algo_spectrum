"""
Searching Module
================

The Searching Module in Algo Spectrum provides implementations of various
searching algorithms, each designed to efficiently locate elements within an
array or other collection.

Algorithms Included
-------------------

1. **Linear Search** [:func:`algorithms.searching.linear_search`]

   - **Description:** A simple algorithm that sequentially searches through each
     element of the array until it finds the target value or reaches the end.
   - **Usage:** Suitable for unsorted arrays.

2. **Sentinel Search:** [:func:`algorithms.searching.sentinel_linear_search`]

   - **Description:** Similar to linear search, but with a sentinel element
     placed at the end of the array to avoid repeated boundary checks.
   - **Use Case:** Improves the efficiency of linear search in some scenarios.

3. **Binary Search:** [:func:`algorithms.searching.binary_search`]

   - **Description:** Requires a sorted array. Divides the array in half
     repeatedly until it finds the target value or determines that it's not
     present.
   - **Use Case:** Efficient for searching in sorted arrays.

4. **Jump Search:** [:func:`algorithms.searching.jump_search`]

   - **Description:** Requires a sorted array. Jumps forward by a fixed step
     size and performs linear search in the block until the target value is
     found or exceeded.
   - **Use Case:** Combines advantages of linear and binary search.

5. **Interpolation Search:** [:func:`algorithms.searching.interpolation_search`]

   - **Description:** Requires a sorted array with uniformly distributed values.
     Estimates the position of the target value based on its value and the
     array's range, then performs binary search.
   - **Use Case:** Effective when values are uniformly distributed.

6. **Exponential Search:**

   - **Description:** Requires a sorted array. Finds a range where the target
     value may exist by exponentially increasing the search range, then performs
     binary search within that range.
   - **Use Case:** Optimized for unbounded search spaces.

7. **Fibonacci Search:**

   - **Description:** Requires a sorted array. Uses Fibonacci numbers to divide
     the array into smaller parts, then performs binary search on the
     appropriate part.
   - **Use Case:** Useful when array sizes are unknown.

8. **Ternary Search:**

   - **Description:** Requires a sorted array. Divides the array into three
     parts using two midpoints, then recursively searches in one of the three
     parts.
   - **Use Case:** Useful for ternary searchable spaces.
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

    :param SupportsComplex target: The value to search for.
    :param List[SupportsComplex] items: The list of items to search.
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
