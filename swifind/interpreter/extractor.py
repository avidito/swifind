import re

from .parser import iterate_components
from ..bucket import Bucket
from ..strategy import Strategy

"""
Validator Functions

Function to extract each activity arguments. Each function use namespace 'extract_', followed by activity name.
Available activity:
- ORIGIN
- PICK
"""
def extract_origin(strategy, args_raw, line_id):
    [url] = re.findall(r"([^'\s]\S*|'.+?')", args_raw)
    strategy.add_origin_plan(url)
    return strategy

def extract_pick(strategy, args_raw, line_id):
    [id, path] = re.findall(r"([^'\s]\S*|'.+?')", args_raw)
    strategy.add_pick_plan(id, path)
    return strategy

"""
Extractor Mapper and Function.
"""
EXTRACTORS = {
    'ORIGIN': extract_origin,
    'PICK': extract_pick
}

@iterate_components
def extract_swipl(components, strategy=Strategy()):
    """
    Extracting swipy components and load to strategy.
    """
    line_id, activity, arguments = next(components)
    strategy = EXTRACTORS[activity](strategy, arguments, line_id)
    return strategy
