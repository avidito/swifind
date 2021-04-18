import pytest
import types
from bs4 import BeautifulSoup

from tests.constant import DUMMY_SWIPL

from swifind.catfish import Catfish
from swifind.strategy import Strategy, Plan
from swifind.interpreter.extractor import (extract_origin,
                                           extract_pick,
                                           extract_swipl)

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
        func(catfish_test)

        catfish_test_view = catfish_test.view
        assert catfish_test_view is not None
        assert isinstance(catfish_test_view, BeautifulSoup)

        result_log = { k: v for k, v in catfish_test.bag.logs['activity'][0].items() if (k != 'timestamp')}
        expected_log = {
            'activity': 'ORIGIN',
            'order': 0,
            'line': 1,
            'status': 'PASS',
        }
        assert result_log == expected_log

class TestExtractPick(object):
    def test_return_value_type(self):
        func = extract_pick(['title', "'h1 a text'"], 10)
        assert isinstance(func, types.FunctionType)

    def test_local_variable(self):
        func = extract_pick(['title', "'h1 a text'"], 10)
        assert ('id', 'line', 'path',) == func.__code__.co_freevars

        vars_results = [var.cell_contents for var in func.__closure__]
        vars_expected = ['title', 10, 'h1 a text']
        assert vars_results == vars_expected

    def test_with_valid_arguments(self):
        catfish_test = Catfish(DUMMY_SWIPL)
        extract_origin(['https://quotes.toscrape.com/'], 1)(catfish_test)
        func = extract_pick(['title', "'h1 a text'"], 10)
        func(catfish_test)

        result_data = catfish_test.bag.data.get('title', None)
        expected_data = 'Quotes to Scrape'
        assert result_data == expected_data

        result_log = { k: v for k, v in catfish_test.bag.logs['activity'][1].items() if (k != 'timestamp')}
        expected_log = {
            'activity': 'PICK',
            'order': 1,
            'line': 10,
            'status': 'PASS',
        }
        assert result_log == expected_log

class TestExtractSwipl(object):
    def test_with_return_values(self):
        strategy_test = Strategy()
        components_test = [
                    ['ORIGIN', ['http://www.testing.com'], 1],
                ]
        result = extract_swipl(strategy_test, components_test)
        assert isinstance(result, Strategy)
        assert result.root is not None
        assert result.tail is not None
