import pytest

from tests.constant import TIMESTAMP_ATTRIBUTES

from swifind.bag import Bag

class TestBagInitiation(object):
    def test_object_type(self):
        bag_test = Bag()
        assert isinstance(bag_test, Bag)
        assert bag_test.items == {}

        result_logs = bag_test.logs
        expected_logs = {
            'swimming': {'counter': 0},
            'activity': []
        }
        assert result_logs == expected_logs

class TestAddItem(object):
    def test_add_valid_item(self):
        bag_test = Bag()
        bag_test.add_item('title', 'Test Title')
        bag_test.add_item('link', 'http://example.link')

        assert bag_test.items.get('title') == 'Test Title'
        assert bag_test.items.get('link') == 'http://example.link'

class TestBagAddLog(object):
    def test_add_swimming_logs(self):
        bag_test = Bag()
        bag_test.add_log('start')
        bag_test_start_time = bag_test.logs['swimming'].get('start_time')
        assert bag_test_start_time is not None

        bag_test.add_log('end')
        bag_test_end_time = bag_test.logs['swimming'].get('end_time')
        assert bag_test_end_time is not None

    def test_add_activity_logs(self):
        bag_test = Bag()
        bag_test.add_log('ORIGIN', 1, 0)
        bag_test.add_log('PICK', 10, 1)

        result_logs = [{k:v for k,v in log.items() if k not in TIMESTAMP_ATTRIBUTES} for log in bag_test.logs['activity']]
        expected_logs = [
            {'activity':'ORIGIN', 'order':0, 'line':1, 'status':'PASS'},
            {'activity':'PICK', 'order':1, 'line':10, 'status':'PASS'},
        ]
        assert result_logs == expected_logs

class TestBagGetItems(object):
    def test_get_valid_items(self):
        bag_test = Bag()
        bag_test.add_item('title', 'Test Title')
        bag_test.add_item('link', 'http://example.link')

        result_items = bag_test.get_items()
        expected_items = {
            'title': 'Test Title',
            'link': 'http://example.link'
        }
        assert result_items == expected_items

class TestBagGetLogs(object):
    def test_get_valid_logs(self):
        bag_test = Bag()
        bag_test.add_log('ORIGIN', 1, 0)
        bag_test.add_log('PICK', 10, 1)

        bag_test_logs = bag_test.get_logs()
        swimming_logs = {k:v for k,v in bag_test_logs['swimming'].items() if k not in TIMESTAMP_ATTRIBUTES}
        activity_logs = [{k:v for k,v in activity.items() if k not in TIMESTAMP_ATTRIBUTES} for activity in bag_test_logs['activity']]

        result_logs = {'swimming': swimming_logs, 'activity': activity_logs}
        expected_logs = {
            'swimming': {'counter': 2},
            'activity': [
                {'activity':'ORIGIN', 'order':0, 'line':1, 'status':'PASS'},
                {'activity':'PICK', 'order':1, 'line':10, 'status':'PASS'}
            ]
        }
        assert result_logs == expected_logs
