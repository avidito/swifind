from .utils import read_script

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
    components = tuple(read_script(path))
    root = extract_root(components[0])
    return root, (), {}
