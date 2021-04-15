import re
import requests
from bs4 import BeautifulSoup

from ..bag import Bag
from ..strategy import Strategy

"""
Validator Functions

Factory function that extract each activity arguments and create activity function. Each function use namespace 'extract_', followed by activity name.
Available activity:
- ORIGIN
- PICK
"""
def extract_origin(args_raw, line):
    [url] = re.findall(r"([^'\s]\S*|'.+?')", args_raw)

    def activity(catfish):
        """
        Get origin page and assign it to strategy.
        """
        req = requests.get(url)
        view = BeautifulSoup(req.content, 'html.parser')

        catfish._assign_view(view)
        catfish.bag.log_activity('ORIGIN', 1, line)
        return req.status_code # Temporary

    return activity

def extract_pick(args_raw, line):
    [id, path] = re.findall(r"([^'\s]\S*|'.+?')", args_raw)

    def activity(catfish):
        return True # Temporary
    return activity

"""
Extractor Mapper and Function.
"""
EXTRACTORS = {
    'ORIGIN': extract_origin,
    'PICK': extract_pick
}

def extract_swipl(strategy, components):
    """
    Extracting swipl components and load to strategy.
    """
    for component in components:
        line, plan, args_raw = component
        activity = EXTRACTORS[plan](args_raw, line)
        strategy.add_activity(plan, activity)
    return strategy
