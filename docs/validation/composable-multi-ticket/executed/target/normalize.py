def normalize(name, *, upper=False):
    if not isinstance(name, str):
        raise ValueError("name must be a string")
    name = name.strip()
    if not name:
        raise ValueError("name must not be blank")
    return name.upper() if upper else name
