def validate_name(name: str, min_length: int, max_length: int):
    """
    Validates that a name is a string and within a specified length range.

    Args:
        name (str): The name to validate.
        min_length (int): The minimum length of the name.
        max_length (int): The maximum length of the name.

    Returns:
        bool: True if the name is valid.

    Raises:
        ValueError: If the name is not a string or not within the specified length range.
    """
    if isinstance(name, str) and min_length <= len(name) <= max_length:
        return True
    else:
        raise ValueError(f"Name must be a string between {min_length} and {max_length} characters.")
