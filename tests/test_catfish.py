import pytest

from swifind.catfish import Catfish

class TestCatfishInitiation(object):
    """
    Test class for Catfish object initiation.
    """
    def test_object_type(self):
        catfish = Catfish()
        assert isinstance(catfish, Catfish)
