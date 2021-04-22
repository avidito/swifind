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

    def activity(catfish, order):
        """
        Get origin page and assign it to strategy.
        """
        req = requests.get(url)
        catfish.view = BeautifulSoup(req.content, 'lxml')
        catfish.bag.add_log('ORIGIN', line, order)

    return activity

def extract_pick(args_raw, line):
    [id, path, attr] = args_raw
    path = path.strip("'")

    def activity(catfish, order):
        content = catfish.view
        for tag in path.split(' '):
            content = getattr(content, tag)
        content = content.get(attr, '') if (attr) else '\n'.join([txt for txt in content.stripped_strings]) 

        catfish.bag.add_item(id, content)
        catfish.bag.add_log('PICK', line, order)

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
        strategy.add_activity(plan, activity, line)
    return strategy
