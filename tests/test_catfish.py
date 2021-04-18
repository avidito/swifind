import os
import pytest

from tests.constant import CATFISH_INITIATION, CATFISH_SWIM

from swifind.constant import ALL_ACTIVITY
from swifind.catfish import Catfish
from swifind.strategy import Strategy
from swifind.bag import Bag
from swifind.interpreter.exception import ArgumentsError

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
        assert strategy.root is not None
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
