import pytest

from swifind.catfish import Catfish

class TestCatfishInitiation(object):
    """
    Test class for Catfish object initiation.
    """
    def test_object_type(self):
        catfish = Catfish('_dummy/dummy.swipl')
        assert isinstance(catfish, Catfish)
