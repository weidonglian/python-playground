"""Sample test file for algorithms module."""

from python_playground.algorithms import sorting


def test_sorting_module_exists():
    """Test that the sorting module can be imported."""
    assert sorting is not None
    assert hasattr(sorting, 'merge_sort')
    assert hasattr(sorting, 'quick_sort')
    assert hasattr(sorting, 'partition')
    assert hasattr(sorting, 'QsPivot')


# Add more tests as needed for your algorithms
