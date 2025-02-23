import pytest
from src.unique_even_sum import unique_even_sum

def test_unique_even_sum_basic():
    """Test basic functionality with mixed numbers"""
    assert unique_even_sum([2, 3, 4, 5, 6]) == 2
    
def test_unique_even_sum_duplicates():
    """Test handling of duplicate even numbers"""
    assert unique_even_sum([2, 2, 3, 4, 4, 5, 6]) == 0
    
def test_unique_even_sum_empty_array():
    """Test with an empty array"""
    assert unique_even_sum([]) == 0
    
def test_unique_even_sum_no_even_numbers():
    """Test array with no even numbers"""
    assert unique_even_sum([1, 3, 5, 7]) == 0
    
def test_unique_even_sum_large_numbers():
    """Test with large numbers, including negative and positive even numbers"""
    assert unique_even_sum([-2, 2, 4, 4, -4, 6, 8, 8]) == -2
    
def test_unique_even_sum_single_number():
    """Test with a single unique even number"""
    assert unique_even_sum([2]) == 2