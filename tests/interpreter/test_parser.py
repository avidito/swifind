import os
import types
import pytest

from tests.constant import READ_SCRIPT_PATH, PARSE_SWIPL_PATH

from swifind.interpreter.parser import (read_script,
                                        parse_swipl,
                                        parse_basic_element,
                                        parse_recursive_tag,
                                        parse_element_with_index,
                                        parse_element_with_selector,
                                        parse_element_notation)

class TestReadScript(object):
    def test_with_valid_script(self):
        path = os.path.join(READ_SCRIPT_PATH, 'valid_components_ex1.swipl')
        result_components = read_script(path)
        assert isinstance(result_components, types.GeneratorType)

        expected_components = [
                (1, "ORIGIN https://www.testing.com/"),
                (3, "PICK title 'h1 a'"),
            ]
        for result, expected in zip(result_components, expected_components):
            assert isinstance(result, tuple)
            assert isinstance(result[0], int)
            assert isinstance(result[1], str)
            assert result == expected

    def test_with_empty_script(self):
        path = os.path.join(READ_SCRIPT_PATH, 'empty_script.swipl')
        result_components = read_script(path)
        assert isinstance(result_components, types.GeneratorType)

        with pytest.raises(StopIteration) as exception_info:
            next(result_components)

class TestParseSwipl(object):
    def test_with_valid_script(self):
        path = os.path.join(PARSE_SWIPL_PATH, 'valid_script_ex1.swipl')
        result_components = parse_swipl(path)
        assert isinstance(result_components, types.GeneratorType)

        expected_components = [
                (1, 'ORIGIN', 'http://quotes.toscrape.com'),
                (2, 'PICK', "title 'h1 a'"),
                (3, 'PICK', "subtitle 'h2 a'")
            ]
        for result, expected in zip(result_components, expected_components):
            assert result == expected

    def test_with_no_argument_activity(self):
        path = os.path.join(PARSE_SWIPL_PATH, 'no_argument_activity_ex1.swipl')
        result_components = parse_swipl(path)
        assert isinstance(result_components, types.GeneratorType)

        expected_components = [
                (1, 'ORIGIN', ''),
                (2, 'PICK', '')
            ]
        for result, expected in zip(result_components, expected_components):
            assert isinstance(result, tuple)
            assert isinstance(result[0], int)
            assert isinstance(result[1], str)
            assert isinstance(result[2], str)
            assert result == expected

class TestParseRecursiveTag(object):
    def test_with_valid_tag(self):
        result = parse_recursive_tag('div*')
        expected = ('div', True)
        assert result == expected

        result = parse_recursive_tag('span')
        expected = ('span', False)
        assert result == expected

    def test_with_empty_tag(self):
        result = parse_recursive_tag('')
        expected = None
        assert result == expected

class TestParseBasicElement(object):
    def test_return_value_datatype(self):
        result = parse_basic_element('div')
        assert isinstance(result[0], tuple)
        assert len(result[0]) == 1
        assert isinstance(result[0][0], str)
        assert isinstance(result[1], str)
        assert isinstance(result[2], dict)

    def test_with_valid_element(self):
        result = parse_basic_element('div')
        expected = (('find',), 'div', {'recursive': False})
        assert result == expected

        result = parse_basic_element('span*')
        expected = (('find',), 'span', {'recursive': True})
        assert result == expected

class TestParseElementWithIndex(object):
    def test_return_value_datatype(self):
        result = parse_element_with_index('div[3]')
        assert isinstance(result[0], tuple)
        assert len(result[0]) == 2
        assert isinstance(result[0][0], str)
        assert isinstance(result[0][1], int)
        assert isinstance(result[1], str)
        assert isinstance(result[2], dict)

    def test_with_valid_element(self):
        result = parse_element_with_index('div[3]')
        expected = (('find_all', 3), 'div', {'recursive': False})
        assert result == expected

        result = parse_element_with_index('span*[2]')
        expected = (('find_all', 2), 'span', {'recursive': True})
        assert result == expected

class TestParseElementWithSelector(object):
    def test_return_value_dataype(self):
        result = parse_element_with_selector('div{class="row"}')
        assert isinstance(result[0], tuple)
        assert len(result[0]) == 1
        assert isinstance(result[0][0], str)
        assert isinstance(result[1], str)
        assert isinstance(result[2], dict)

    def test_with_valid_element(self):
        result = parse_element_with_selector('small{class="author"}')
        expected = (('find',), 'small', {'recursive': False, 'attrs':{'class':'author'}})
        assert result == expected

        result = parse_element_with_selector('div*{class="quote"}')
        expected = (('find',), 'div', {'recursive': True, 'attrs':{'class':'quote'}})
        assert result == expected

class TestParseElementNotation(object):
    def test_with_valid_element(self):
        result = parse_element_notation('div[1]')
        expected = (('find_all', 1), 'div', {'recursive': False})
        assert result == expected

        result = parse_element_notation('span*')
        expected = (('find',), 'span', {'recursive': True})
        assert result == expected

        result = parse_element_notation('div{class="row"}')
        expected = (('find',), 'div', {'recursive': False, 'attrs':{'class':'row'}})
        assert result == expected
