def validate(data):
    if not isinstance(data, list):
        raise TypeError("The loaded json is not in the correct format")