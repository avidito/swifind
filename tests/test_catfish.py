import os
import pytest

from tests.constant import CATFISH_PREPARE


from swifind.catfish import Catfish
from swifind.strategy import Strategy
from swifind.bag import Bag
from swifind.interpreter.exception import ArgumentsError

class TestCatfishInitiation(object):
    def test_object_type(self):
        catfish_test = Catfish()
        assert isinstance(catfish_test, Catfish)
        assert catfish_test.validate == False
        assert catfish_test.view is None
        assert isinstance(catfish_test.strategy, Strategy)
        assert isinstance(catfish_test.bag, Bag)

class TestCatfishPrepare(object):
    def test_attribute_existence(self):
        catfish_test = Catfish()
        path = os.path.join(CATFISH_PREPARE, 'valid_components_ex1.swipl')

        catfish_test.prepare(path)
        assert catfish_test.validate == True

        strategy = catfish_test.strategy
        assert strategy.root is not None
        assert strategy.tail is not None

    def test_with_invalid_component(object):
        catfish_test = Catfish()
        path = os.path.join(CATFISH_PREPARE, 'invalid_components_ex1.swipl')

        msg = "'ORIGIN' activity missing required arguments: 'URL' at line 1."
        with pytest.raises(ArgumentsError, match=f"^{msg}$") as exception_info:
            catfish_test.prepare(path)
            assert catfish_test.validate == False
            assert catfish_test.view is None
