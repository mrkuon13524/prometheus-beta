import unicodedata

def is_anagram(str1: str, str2: str) -> bool:
    """
    Determine if two strings are anagrams.
    
    An anagram is a word or phrase formed by rearranging the letters of another,
    using all the original letters exactly once.
    
    Args:
        str1 (str): The first string to compare
        str2 (str): The second string to compare
    
    Returns:
        bool: True if the strings are anagrams, False otherwise
    
    Raises:
        TypeError: If input is not a string
    """
    # Check input types
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Both inputs must be strings")
    
    # Normalize and clean string
    def clean_string(s: str) -> str:
        # Convert to lowercase and remove all non-letter characters
        return ''.join(
            char.lower() for char in s 
            if char.isalpha()
        )
    
    # Clean and compare sorted characters
    cleaned1 = clean_string(str1)
    cleaned2 = clean_string(str2)
    
    # Check if cleaned strings have same length and characters
    return sorted(cleaned1) == sorted(cleaned2)