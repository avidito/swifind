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
        result_logs = bag_test.logs
        assert result_logs == expected_logs

class TestBagAddLog(object):
    def test_add_journey_logs(self):
        bag_test = Bag()
        bag_test.add_log('start')
        bag_test_start_time = bag_test.logs['swimming'].get('start_time')
        assert bag_test_start_time is not None

        bag_test.add_log('end')
        bag_test_end_time = bag_test.logs['swimming'].get('end_time')
        assert bag_test_end_time is not None

    def test_add_activity_logs(self):
        bag_test = Bag()
        bag_test.add_log('ORIGIN', 1)
        
        assert bag_test.logs['activity']
