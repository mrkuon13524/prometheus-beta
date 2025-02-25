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
    
    # Normalize function to remove spaces, convert to lowercase, 
    # and optionally handle basic accents
    def normalize(s: str) -> str:
        # Remove all whitespace and convert to lowercase
        normalized = ''.join(s.replace(' ', '').lower())
        
        # Optional: simple accent removal
        accent_map = {
            'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
            'ä': 'a', 'ë': 'e', 'ï': 'i', 'ö': 'o', 'ü': 'u',
            'à': 'a', 'è': 'e', 'ì': 'i', 'ò': 'o', 'ù': 'u'
        }
        
        # Replace accented characters
        return ''.join(accent_map.get(char, char) for char in normalized)
    
    # Normalize both strings
    norm1 = normalize(str1)
    norm2 = normalize(str2)
    
    # Quick length check to rule out non-anagrams quickly
    if len(norm1) != len(norm2):
        return False
    
    # Use character counting approach
    return sorted(norm1) == sorted(norm2)