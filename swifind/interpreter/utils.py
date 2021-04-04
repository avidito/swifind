def read_script(path):
    """
    Reading script from path.
    """
    with open(path, 'r') as f:
        raw = f.read()
    fltr = filter(lambda x: x != '', raw.split('\n'))
    return fltr
