import os

def get_bool_env(var_name, default=False):
    """
    Reads an environment variable and converts it to a boolean.
    Returns the default value if the variable is unset.
    """
    value = os.getenv(var_name)
    if value is None:
        return default
    # Convert to lowercase and check against common true values
    return value.lower() in ('true', '1', 'yes', 'on')