import re

def to_constant_case(input_string):
    """
    Convert a string to CONSTANT_CASE.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to CONSTANT_CASE.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not input_string:
        return ""
    
    # Use regex to split camelCase and MixedCase into words
    # Replace non-alphanumeric characters with underscores
    # Convert to uppercase
    # Remove leading/trailing underscores
    words = re.findall(r'[A-Z]?[a-z]+|[A-Z]+(?=[A-Z][a-z]|\d|\W|$)|\d+', input_string)
    constant_case = '_'.join(word.upper() for word in words).strip('_')
    
    return constant_case