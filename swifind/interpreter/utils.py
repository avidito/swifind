def read_script(path):
    """
    Reading script from path.
    """
    with open(path, 'r') as f:
        raw = f.read()
    return raw
