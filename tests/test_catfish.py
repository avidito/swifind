import os
import pytest

from tests.constant import (CATFISH_INITIATION,
                            CATFISH_SWIM,
                            CATFISH_RETRIEVE,
                            TIMESTAMP_ATTRIBUTES)

from swifind.catfish import Catfish
from swifind.constant import ALL_ACTIVITY
from swifind.strategy import Strategy
from swifind.bag import Bag
from swifind.exception import ArgumentsError

class TestCatfishInitiation(object):
    def test_object_type(self):
        path = os.path.join(CATFISH_INITIATION, 'object_type_ex1.swipl')
        catfish_test = Catfish(path)

        assert isinstance(catfish_test, Catfish)
        assert isinstance(catfish_test.strategy, Strategy)
        assert isinstance(catfish_test.bag, Bag)

    def test_attribute_existence(self):
        path = os.path.join(CATFISH_INITIATION, 'object_type_ex1.swipl')
        catfish_test = Catfish(path)

        strategy = catfish_test.strategy
        assert strategy.head is not None
        assert strategy.tail is not None

    def test_with_invalid_component(object):
        path = os.path.join(CATFISH_INITIATION, 'invalid_components_ex1.swipl')
        msg = "'ORIGIN' activity missing required arguments: 'URL' at line 1."
        with pytest.raises(ArgumentsError, match=f"^{msg}$") as exception_info:
            catfish_test = Catfish(path)

class TestCatfishSwim(object):
    def test_log_swim(self):
        path = os.path.join(CATFISH_SWIM, 'log_swimming_ex1.swipl')
        catfish_test = Catfish(path)
        catfish_test.swim()

        assert catfish_test.bag.logs['swimming']['counter'] == 3
        assert 'start_time' in catfish_test.bag.logs['swimming']
        assert 'end_time' in catfish_test.bag.logs['swimming']

        expected_activity_logs = [
            {'activity': 'ORIGIN', 'order': 0, 'line': 1, 'status':'PASS'},
            {'activity': 'PICK', 'order': 1, 'line': 2, 'status':'PASS'},
            {'activity': 'PICK', 'order': 2, 'line': 3, 'status':'PASS'}
        ]
        result_activity_logs = [{k:log[k] for k in log if k not in ('timestamp')} for log in catfish_test.bag.logs['activity']]
        assert result_activity_logs == expected_activity_logs

class TestCatfishRetrieve(object):
    def test_only_retrieve_items(self):
        path = os.path.join(CATFISH_SWIM, 'log_swimming_ex1.swipl')
        catfish_test = Catfish(path)
        catfish_test.swim()

        result_items = catfish_test.retrieve()
        expected_items = {
            'items': {
                'title': 'Quotes to Scrape',
                'author': 'GoodReads.com'
            }
        }
        assert result_items == expected_items

    def test_with_retrieve_logs(self):
        path = os.path.join(CATFISH_SWIM, 'log_swimming_ex1.swipl')
        catfish_test = Catfish(path)
        catfish_test.swim()

        catfish_items = catfish_test.retrieve(include_logs=True)
        swimming_logs = {k:v for k,v in catfish_items['logs']['swimming'].items() if k not in TIMESTAMP_ATTRIBUTES}
        activity_logs = [{k:v for k,v in activity.items() if k not in TIMESTAMP_ATTRIBUTES} for activity in catfish_items['logs']['activity']]

        result_items = {'items':catfish_items['items'], 'logs':{'swimming': swimming_logs, 'activity': activity_logs}}
        expected_items = {
            'items': {
                'title': 'Quotes to Scrape',
                'author': 'GoodReads.com'
            },
            'logs': {
                'swimming': {'counter': 3},
                'activity': [
                    {'activity': 'ORIGIN', 'order':0, 'line':1, 'status':'PASS'},
                    {'activity': 'PICK', 'order':1, 'line':2, 'status':'PASS'},
                    {'activity': 'PICK', 'order':2, 'line':3, 'status':'PASS'},
                ]
            }
        }
        assert result_items == expected_items
