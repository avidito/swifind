from .parser import parse_swipy

def extract_root(component):
    """
    Extracting root information.
    """
    root = component.split(' ', 2)[1]
    return root

def extract_swipy(path):
    """
    Extracting swipy script from path.
    """
    components = parse_swipy(path)
    root = next(components)[2]
    return root, (), {}
