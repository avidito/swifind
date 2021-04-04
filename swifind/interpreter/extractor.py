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
    raw = read_script(path)[:-1].split('\n')
    root = extract_root(raw[0])
    return root, (), {}
