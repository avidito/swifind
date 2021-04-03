def read_script(path):
    """
    Reading script from path.
    """
    with open(path, 'r') as f:
        raw = f.read()
    return raw

def root_extract(path):
    """
    Extracting root information.
    """
    raw = read_script(path).split('\n')[0]
    root = raw.split(' = ')[1][1:-1]
    return root
