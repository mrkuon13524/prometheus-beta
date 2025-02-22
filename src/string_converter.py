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
    
    # Remove non-alphanumeric characters and replace with underscore
    # Convert to uppercase
    # Remove leading/trailing underscores
    constant_case = re.sub(r'[^a-zA-Z0-9]+', '_', input_string).upper().strip('_')
    
    return constant_case