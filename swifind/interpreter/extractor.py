from .parser import parse_swipy
from ..bucket import Bucket
from ..strategy import Strategy

def extract_root(component):
    """
    Extracting root information.
    """
    root = next(component)[2]
    return root


# Extractor Functions
def extract_swipy(path):
    """
    Extracting swipy script from path and load to strategy.
    """
    components = parse_swipy(path)
    strategy = Strategy(extract_root(components))
    return Bucket(), strategy
