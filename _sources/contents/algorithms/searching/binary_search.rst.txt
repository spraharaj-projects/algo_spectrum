Binary Search
=============

:func:`algorithms.binary_search`

The Binary Search algorithm is a highly efficient searching algorithm used to
find a target element in a sorted collection by repeatedly dividing the search
interval in half.

Algorithm Overview
------------------

.. image:: ../../../_static/binary_search.jpg
   :width: 600px
   :alt: Linear Search Flow Diagram
   :align: center

|

1. Initialize two pointers, left and `right`, representing the leftmost and
   rightmost indices of the collection, respectively.
2. While the `left` pointer is less than or equal to the `right` pointer:

   - Calculate the middle index as `(left + right) // 2`.
   - If the middle element is equal to the target element, return its index.
   - If the middle element is greater than the target element, update the
     `right` pointer to `mid - 1`.
   - If the middle element is less than the target element, update the `left`
     pointer to `mid + 1`.
3. If the target element is not found after the loop, return None.

.. note::
   Binary Search requires the collection to be sorted and has a time complexity of O(log n), where 'n' is the number of elements in the collection.

Implementation in Python
------------------------

Here's a Python implementation of the Binary Search algorithm:

.. code-block:: python
   :linenos:

    def binary_search(target: Any, items: List[Any]) -> Optional[int]:
        left, right = 0, len(items) - 1
        while left <= right:
            mid = (left + right) // 2
            if items[mid] == target:
                return mid
            elif items[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return None

Usage
-----

To use the binary_search function:

.. code-block:: python
   :linenos:
   :emphasize-lines: 6

    from algorithms import binary_search


    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 5
    index = binary_search(target, arr)
    if index is not None:
        print(f"Element {target} found at index {index}")
    else:
        print(f"Element {target} not found")
