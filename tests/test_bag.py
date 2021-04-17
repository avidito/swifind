import pytest

from swifind.bag import Bag

class TestBagInitiation(object):
    def test_object_type(self):
        bag_test = Bag()
        assert isinstance(bag_test, Bag)
        assert bag_test.data == {}

        expected_logs = {
            'swimming': {'counter': 0},
            'activity': []
        }
        assert bag_test.logs == expected_logs

class TestBagAddLog(object):
    def test_add_journey_logs(self):
        bag_test = Bag()
        bag_test.add_log('start')
        assert bag_test.logs['swimming'].get('start_time') is not None

        bag_test.add_log('end')
        assert bag_test.logs['swimming'].get('end_time') is not None

    def test_add_activity_logs(self):
        bag_test = Bag()
        bag_test.add_log('ORIGIN', 1)
        assert bag_test.logs['activity']

    def test_invalid_add_logs(self):
        ... # Implement later
