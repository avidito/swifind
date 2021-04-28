import requests
from bs4 import BeautifulSoup

from .parser import parse_element_notation
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
        catfish.view = BeautifulSoup(req.content, 'lxml', multi_valued_attributes=None)
        catfish.bag.add_log('ORIGIN', line, order)

    return activity

def extract_pick(args_raw, line):
    [id, path, attr] = args_raw
    path = path.strip("'")

    def activity(catfish, order):
        content = catfish.view.find('body')
        for element in path.split(' '):
            if (content is None): break

            [method, tag, params] = parse_element_notation(element)
            if (method[0] in ('find_all',)):
                [method, index] = method
                content = getattr(content, method)(tag, **params)[index]
            else:
                content = getattr(content, method[0])(tag, **params)
        else:
            content = content.get(attr, None) if (attr) else '\n'.join([txt for txt in content.stripped_strings])

        catfish.bag.add_item(id, content)
        catfish.bag.add_log('PICK', line, order)

    return activity

def extract_swim(args_raw, line):
    [url] = args_raw

    def activity(catfish, order):
        """
        Get next page to visit.
        """
        req = requests.get(url)
        catfish.view = BeautifulSoup(req.content, 'lxml', multi_valued_attributes=None)
        catfish.bag.add_log('SWIM', line, order)

    return activity

"""
Extractor Mapper and Function.
"""
EXTRACTORS = {
    'ORIGIN': extract_origin,
    'PICK': extract_pick,
    'SWIM': extract_swim,
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
