def read_script(path):
    """
    Reading script from path and remove empty string.
    """
    with open(path, 'r') as f:
        raw = f.read()
    raw_components = ((line_id+1, line.strip()) for line_id, line in enumerate(raw.split('\n')) if (line != ''))
    return raw_components

def parse_swipl(path):
    """
    Parse swipl script to list of component.
    """
    raw_components = read_script(path)
    components = ((line_id, *line.split(' ', 1)) if (line.count(' ')) else (line_id, line.strip(), None) for line_id, line in raw_components)
    return components

def iterate_components(func):
    """
    Decorator to apply function accross all components.
    """
    def wrapper(components):
        try:
            while(1): obj = func(components)
        except StopIteration:
            pass
        return obj
    return wrapper
