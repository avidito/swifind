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
    [url] = args_raw

    def activity(catfish):
        """
        Get origin page and assign it to strategy.
        """
        req = requests.get(url)
        catfish.view = BeautifulSoup(req.content, 'lxml')
        catfish.bag.log_activity('ORIGIN', line)
        return req.status_code # Temporary

    return activity

def extract_pick(args_raw, line):
    [id, path] = args_raw
    path = path.strip("'")

    def activity(catfish):
        content = catfish.view
        for tag in path.split(' '):
            content = getattr(content, tag)

        catfish.bag.add_item(id, content)
        catfish.bag.log_activity('PICK', line)
        return content # Temporary
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
        plan, args_raw, line = component
        activity = EXTRACTORS[plan](args_raw, line)
        strategy.add_activity(plan, activity)
    return strategy
