import pytest
import types
from bs4 import BeautifulSoup

from swifind.catfish import Catfish
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
        assert vars_expected == vars_results

    def test_with_valid_arguments(self):
        catfish_test = Catfish()
        func = extract_origin(['https://quotes.toscrape.com/'], 1)
        func(catfish_test)
        assert catfish_test.view is not None
        assert isinstance(catfish_test.view, BeautifulSoup)

        expected_log = {
            'activity': 'ORIGIN',
            'order': 0,
            'line': 1,
            'status': 'PASS',
        }
        result_log = { k: v for k, v in catfish_test.bag.logs['activity'][0].items() if (k != 'timestamp')}
        assert expected_log == result_log

class TestExtractPick(object):
    def test_return_value_type(self):
        func = extract_pick(['title', "'h1 a text'"], 10)
        assert isinstance(func, types.FunctionType)

    def test_local_variable(self):
        func = extract_pick(['title', "'h1 a text'"], 10)
        assert ('id', 'line', 'path',) == func.__code__.co_freevars

        vars_results = [var.cell_contents for var in func.__closure__]
        vars_expected = ['title', 10, 'h1 a text']
        assert vars_expected == vars_results

    def test_with_valid_arguments(self):
        catfish_test = Catfish()
        extract_origin(['https://quotes.toscrape.com/'], 1)(catfish_test)
        func = extract_pick(['title', "'h1 a text'"], 10)
        func(catfish_test)

        result = catfish_test.bag.data.get('title', None)
        assert result is not None
        assert result == 'Quotes to Scrape'

        expected_log = {
            'activity': 'PICK',
            'order': 1,
            'line': 10,
            'status': 'PASS',
        }
        result_log = { k: v for k, v in catfish_test.bag.logs['activity'][1].items() if (k != 'timestamp')}
        assert expected_log == result_log

class TestExtractSwipl(object):
    def test_with_return_values_datatype(self):
        ... # Implement later

    def test_with_valid_components(self):
        ... # Implement later

    def test_with_invalid_components(self):
        ... # Implement later
