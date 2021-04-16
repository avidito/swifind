import pytest
import types
import copy

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
        vars_results = [var.cell_contents for var in func.__closure__]
        vars_expected = [1, 'https://quotes.toscrape.com/',]
        assert ('line', 'url',) == func.__code__.co_freevars
        assert vars_expected == vars_results

    def  test_with_valid_arguments(self):
        catfish_test = Catfish()
        func = extract_origin(['https://quotes.toscrape.com/'], 1)
        func(catfish_test)
        assert catfish_test.view is not None

class TestExtractPick(object):
    def  test_with_valid_arguments(self):
        ... # Implement later

    def test_return_value_type(self):
        ... # Implement later

    def test_local_variable(self):
        ... # Implement later

class TestExtractSwipl(object):
    def test_with_return_values_datatype(self):
        ... # Implement later

    def test_with_valid_components(self):
        ... # Implement later

    def test_with_invalid_components(self):
        ... # Implement later
