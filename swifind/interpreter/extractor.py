import requests
from bs4 import BeautifulSoup
import re

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
        index_reg = re.compile(r".+\[\S+\]")
        selector_reg = re.compile(r".+\{\S+\}")
        content = catfish.view.find('body')

        for tag in path.split(' '):
            if (content is None):
                break
            if (index_reg.search(tag)):
                [tag_clean, index] = tag[:-1].split('[')
                content = content.find_all(tag_clean, recursive=False)[int(index)]
            elif (selector_reg.search(tag)):
                [tag_clean, selector] = tag[:-1].split('{')
                [prop, value] = selector.split('=')
                content = content.find(tag_clean, {prop: value.strip('"')}, recursive=False)
            else:
                content = content.find(tag, recursive=False)
        else:
            content = content.get(attr, None) if (attr) else '\n'.join([txt for txt in content.stripped_strings])

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
