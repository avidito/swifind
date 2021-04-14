def read_script(path):
    """
    Reading script from path and remove empty string.
    """
    with open(path, 'r') as f:
        raw = f.read().strip()
    raw_components = ((id+1, line.strip()) for id, line in enumerate(raw.split('\n')) if (line.strip()))
    return raw_components

def parse_swipl(path):
    """
    Parse swipl script to list of component.
    """
    raw_components = read_script(path)
    components = ((line_id, *line.split(' ', 1)) for line_id, line in raw_components)
    components_padded_args = ((line, *activity) if (len(activity) == 2) else (line, *activity, '') for line, *activity in components)
    return components_padded_args
