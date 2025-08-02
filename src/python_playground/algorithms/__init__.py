"""Algorithms module containing sorting and other algorithmic implementations."""

from .sorting import merge_sort, quick_sort, partition, QsPivot, Comparable
from .inversion import inversions_fast, inversion_slow

__all__ = [
    'merge_sort',
    'quick_sort',
    'partition',
    'QsPivot',
    'Comparable',
    'inversions_fast',
    'inversion_slow',
]
