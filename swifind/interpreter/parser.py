def read_script(path):
    """
    Reading script from path and remove empty string.
    """
    with open(path, 'r') as f:
        raw = f.read()
    raw_components = ((line_id, line) for line_id, line in enumerate(raw.split('\n')) if (line != ''))
    return raw_components

def parse_swipy(path):
    """
    Parse swipy script to list of component.
    """
    raw_components = read_script(path)
    components = ((line_id, *line.split(' ', 1)) for line_id, line in raw_components)
    return components
