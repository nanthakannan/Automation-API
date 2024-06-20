import json

def get_int_value(value):
    try:
        return int(value)
    except ValueError:
        raise ValueError(f"Invalid integer value: {value}")

def load_response(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def append_response(context, response):
    """
    Append the response to the context.

    Args:
        context: The context object.
        response: The response object to append.
    """
    context.responses.append(response)
    
    
def convert_to_int(value):
    """
    Convert a string value to an integer.

    Args:
        value (str): The string value to convert.

    Returns:
        int: The integer value.
    """
    try:
        return int(value)
    except ValueError:
        raise ValueError(f"Invalid integer value: {value}")
