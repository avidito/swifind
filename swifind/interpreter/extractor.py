import re

from .parser import iterate_components
from ..bucket import Bucket
from ..strategy import Strategy

def extract_root(strategy, args_raw, line_id):
    """
    Extracting root information.
    """
    [url] = re.findall(r"([^'\s]\S*|'.+?')", args_raw)
    strategy.add_root_plan(url)
    return strategy

def extract_collect(strategy, args_raw, line_id):
    """
    Extracting collect information.
    """
    [id, path] = re.findall(r"([^'\s]\S*|'.+?')", args_raw)
    strategy.add_collect_plan(id, path)
    return strategy

EXTRACTORS = {
    'ROOT': extract_root,
    'COLLECT': extract_collect
}

# Extractor Functions
@iterate_components
def extract_swipy(components, strategy=Strategy()):
    """
    Extracting swipy components and load to strategy.
    """
    line_id, activity, arguments = next(components)
    strategy = EXTRACTORS[activity](strategy, arguments, line_id)
    return strategy
