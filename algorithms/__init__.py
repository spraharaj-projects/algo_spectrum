"""
Algorithms
==========

Doc on algo.
"""
from algorithms.searching import linear_search
from algorithms.searching import sentinel_linear_search
from algorithms.searching import binary_search
from algorithms.searching import jump_search
from algorithms.searching import interpolation_search
from algorithms.searching import exponential_search
from algorithms.searching import fibonacci_search
from algorithms.searching import ternary_search
from algorithms.sorting import bubble_sort


__all__ = [
    # searching
    'linear_search',
    'sentinel_linear_search',
    'binary_search',
    'jump_search',
    'interpolation_search',
    'exponential_search',
    'fibonacci_search',
    'ternary_search',

    # sorting
    'bubble_sort',
]