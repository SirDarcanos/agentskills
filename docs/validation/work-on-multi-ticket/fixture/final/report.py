from names import normalize_name


def render_names(values):
    return ', '.join(normalize_name(value) for value in values)
