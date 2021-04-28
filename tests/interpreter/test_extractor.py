import pytest
import types
from bs4 import BeautifulSoup

from tests.constant import DUMMY_SWIPL

from swifind.interpreter.extractor import (extract_origin,
                                           extract_pick,
                                           extract_swim,
                                           extract_swipl)
from swifind.catfish import Catfish
from swifind.strategy import Strategy, Plan

class TestExtractOrigin(object):
    def test_return_value_type(self):
        func = extract_origin(['https://quotes.toscrape.com/'], 1)
        assert isinstance(func, types.FunctionType)

    def test_local_variable_existence(self):
        func = extract_origin(['https://quotes.toscrape.com/'], 1)
        assert ('line', 'url',) == func.__code__.co_freevars

        vars_results = [var.cell_contents for var in func.__closure__]
        vars_expected = [1, 'https://quotes.toscrape.com/',]
        assert vars_results == vars_expected

    def test_with_valid_arguments(self):
        catfish_test = Catfish(DUMMY_SWIPL)
        func = extract_origin(['https://quotes.toscrape.com/'], 1)
        func(catfish_test, 0)

        catfish_test_view = catfish_test.view
        assert catfish_test_view is not None
        assert isinstance(catfish_test_view, BeautifulSoup)

        result_log = { k: v for k, v in catfish_test.bag.logs['activity'][0].items() if (k != 'timestamp')}
        expected_log = {'activity': 'ORIGIN', 'order': 0, 'line': 1, 'status': 'PASS',}
        assert result_log == expected_log

class TestExtractPick(object):
    def test_return_value_type(self):
        func = extract_pick(['title', "'div div div h1 a'", None], 10)
        assert isinstance(func, types.FunctionType)

        func = extract_pick(['quote', "'div div[1] span'", None], 10)
        assert isinstance(func, types.FunctionType)

    def test_local_variable(self):
        func = extract_pick(['title', "'div div div h1 a'", None], 10)
        assert ('attr', 'id', 'line', 'path',) == func.__code__.co_freevars

        vars_results = [var.cell_contents for var in func.__closure__]
        vars_expected = [None, 'title', 10, 'div div div h1 a']
        assert vars_results == vars_expected

    def test_with_valid_arguments(self):
        catfish_test = Catfish(DUMMY_SWIPL)
        extract_origin(['https://quotes.toscrape.com/'], 1)(catfish_test, 0)

        # Test 1
        func = extract_pick(['title', "'div div div h1 a'", None], 10)
        func(catfish_test, 1)

        result_data = catfish_test.bag.items.get('title', None)
        expected_data = 'Quotes to Scrape'
        assert result_data == expected_data

        result_log = { k: v for k, v in catfish_test.bag.logs['activity'][1].items() if (k != 'timestamp')}
        expected_log = {'activity': 'PICK', 'order': 1, 'line': 10, 'status': 'PASS',}
        assert result_log == expected_log

        # Test 2
        func = extract_pick(['link', "'footer div p a'", 'href'], 10)
        func(catfish_test, 1)

        result_data = catfish_test.bag.items.get('link', None)
        expected_data = 'https://www.goodreads.com/quotes'
        assert result_data == expected_data

        result_log = { k: v for k, v in catfish_test.bag.logs['activity'][1].items() if (k != 'timestamp')}
        expected_log = { 'activity': 'PICK', 'order': 1, 'line': 10, 'status': 'PASS',}
        assert result_log == expected_log

        # Test 3
        func = extract_pick(['author', "'div div[1] div div span[1] small'", None], 10)
        func(catfish_test, 1)

        result_data = catfish_test.bag.items.get('author', None)
        expected_data = 'Albert Einstein'
        assert result_data == expected_data

        result_log = { k: v for k, v in catfish_test.bag.logs['activity'][1].items() if (k != 'timestamp')}
        expected_log = { 'activity': 'PICK', 'order': 1, 'line': 10, 'status': 'PASS',}
        assert result_log == expected_log

        # Test 4
        func = extract_pick(['author', "'small*{class=\"author\"}'", None], 10)
        func(catfish_test, 1)

        result_data = catfish_test.bag.items.get('author', None)
        expected_data = 'Albert Einstein'
        assert result_data == expected_data

        result_log = { k: v for k, v in catfish_test.bag.logs['activity'][1].items() if (k != 'timestamp')}
        expected_log = { 'activity': 'PICK', 'order': 1, 'line': 10, 'status': 'PASS',}
        assert result_log == expected_log

        # Test 5
        func = extract_pick(['third_quote', "'div*{class=\"row\"} div*{class=\"col-md-8\"} div[2] span'", None], 10)
        func(catfish_test, 1)

        result_data = catfish_test.bag.items.get('third_quote', None)
        expected_data = '“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”'
        assert result_data == expected_data

        result_log = { k: v for k, v in catfish_test.bag.logs['activity'][1].items() if (k != 'timestamp')}
        expected_log = { 'activity': 'PICK', 'order': 1, 'line': 10, 'status': 'PASS',}
        assert result_log == expected_log

    def test_with_non_exist_attr(self):
        catfish_test = Catfish(DUMMY_SWIPL)
        extract_origin(['https://quotes.toscrape.com/'], 1)(catfish_test, 0)
        func = extract_pick(['title', "'h1 a'", 'class'], 10)
        func(catfish_test, 1)

        result_data = catfish_test.bag.items.get('title', None)
        expected_data = None
        assert result_data == expected_data

        result_log = { k: v for k, v in catfish_test.bag.logs['activity'][1].items() if (k != 'timestamp')}
        expected_log = {'activity': 'PICK', 'order': 1, 'line': 10, 'status': 'PASS',}
        assert result_log == expected_log

class TestExtractSwim(object):
    def test_return_value_type(self):
        func = extract_swim(['https://quotes.toscrape.com/page/10/'], 5)
        assert isinstance(func, types.FunctionType)

    def test_local_variable_existence(self):
        func = extract_swim(['https://quotes.toscrape.com/page/10/'], 5)
        assert ('line', 'url',) == func.__code__.co_freevars

        vars_results = [var.cell_contents for var in func.__closure__]
        vars_expected = [5, 'https://quotes.toscrape.com/page/10/',]
        assert vars_results == vars_expected

    def test_with_valid_arguments(self):
        catfish_test = Catfish(DUMMY_SWIPL)
        extract_origin(['https://quotes.toscrape.com/'], 1)(catfish_test, 0)
        func = extract_swim(['https://quotes.toscrape.com/'], 5)
        func(catfish_test, 1)

        catfish_test_view = catfish_test.view
        assert catfish_test_view is not None
        assert isinstance(catfish_test_view, BeautifulSoup)

        result_log = { k: v for k, v in catfish_test.bag.logs['activity'][1].items() if (k != 'timestamp')}
        expected_log = {'activity': 'SWIM', 'order': 1, 'line': 5, 'status': 'PASS',}
        assert result_log == expected_log

class TestExtractSwipl(object):
    def test_with_return_values(self):
        strategy_test = Strategy()
        components_test = [
                    ['ORIGIN', ['http://www.testing.com'], 1],
                    ['PICK', ['title', "'h1 a'", None], 2],
                    ['PICK', ['link', "'footer div p a'", 'href'], 3],
                    ['PICK', ['quote', "'div div[1] div'", 'href'], 4],
                    ['SWIM', ['https://quotes.toscrape.com/page/10/'], 5]
                ]
        result = extract_swipl(strategy_test, components_test)
        assert isinstance(result, Strategy)
        assert result.head is not None
        assert result.tail is not None
        assert result.rank == 5
