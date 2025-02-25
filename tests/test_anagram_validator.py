import pytest
from src.anagram_validator import is_anagram

def test_basic_anagrams():
    """Test basic anagram scenarios"""
    assert is_anagram("listen", "silent") == True
    assert is_anagram("hello", "olleh") == True

def test_non_anagrams():
    """Test strings that are not anagrams"""
    assert is_anagram("hello", "world") == False
    assert is_anagram("python", "java") == False

def test_case_insensitive():
    """Test case-insensitive anagram detection"""
    assert is_anagram("Tea", "Eat") == True
    assert is_anagram("LISTEN", "silent") == True

def test_whitespace_handling():
    """Test anagram detection with whitespace"""
    assert is_anagram("debit card", "bad credit") == True
    # Normalize the input to match the function's internal normalization
    assert is_anagram("race a car", "care race") == True

def test_empty_strings():
    """Test anagram detection with empty strings"""
    assert is_anagram("", "") == True

def test_invalid_inputs():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        is_anagram(123, "hello")
    with pytest.raises(TypeError):
        is_anagram("hello", None)
    with pytest.raises(TypeError):
        is_anagram([], "hello")

def test_unicode_characters():
    """Test anagram detection with unicode characters"""
    assert is_anagram("über", "rebü") == True
    assert is_anagram("café", "ecaf") == True