import re
import requests
from bs4 import BeautifulSoup

from .parser import iterate_components
from ..bag import Bag
from ..strategy import Strategy

"""
Validator Functions

Factory function that extract each activity arguments and create activity function. Each function use namespace 'extract_', followed by activity name.
Available activity:
- ORIGIN
- PICK
"""
def extract_origin(args_raw, line_id):
    [url] = re.findall(r"([^'\s]\S*|'.+?')", args_raw)

    def activity(strategy, bag):
        """
        Get origin page and assign it to strategy.
        """
        req = requests.get(url)
        view = BeautifulSoup(req.content, 'html.parser')

        strategy.assign_view(view)
        bag.log_activity('ORIGIN', 1, line_id)
        return req.status_code # Temporary

    return activity

def extract_pick(args_raw, line_id):
    [id, path] = re.findall(r"([^'\s]\S*|'.+?')", args_raw)

    def activity(strategy, bag):
        return True # Temporary
    return activity

"""
Extractor Mapper and Function.
"""
EXTRACTORS = {
    'ORIGIN': extract_origin,
    'PICK': extract_pick
}

@iterate_components
def extract_swipl(components):
    """
    Extracting swipy components and load to strategy.
    """
    line_id, activity, arguments = next(components)
    strategy = EXTRACTORS[activity](arguments, line_id)
    return "OK" # Temporary
