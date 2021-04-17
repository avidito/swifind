import os
import types
import pytest

from tests.constant import READ_SCRIPT_PATH, PARSE_SWIPL_PATH

from swifind.interpreter.parser import (read_script,
                                        parse_swipl)

class TestReadScript(object):
    def test_with_valid_script(self):
        path = os.path.join(READ_SCRIPT_PATH, 'valid_components_ex1.swipl')
        raw_components = read_script(path)
        assert isinstance(raw_components, types.GeneratorType)

        expected = [
                (1, "ORIGIN https://www.testing.com/"),
                (3, "PICK title 'h1 a text'"),
            ]
        for component, exp in zip(raw_components, expected):
            assert isinstance(component, tuple)
            assert isinstance(component[0], int)
            assert isinstance(component[1], str)
            assert component == exp


    def test_with_empty_script(self):
        path = os.path.join(READ_SCRIPT_PATH, 'empty_script.swipl')
        raw_components = read_script(path)
        assert isinstance(raw_components, types.GeneratorType)

        with pytest.raises(StopIteration) as exception_info:
            next(raw_components)

class TestParseSwipl(object):
    def test_with_valid_script(self):
        path = os.path.join(PARSE_SWIPL_PATH, 'valid_script_ex1.swipl')
        components = parse_swipl(path)
        assert isinstance(components, types.GeneratorType)

        expected = [
                (1, 'ORIGIN', 'http://quotes.toscrape.com'),
                (2, 'PICK', "title 'h1 a text'"),
                (3, 'PICK', "subtitle 'h2 a text'")
            ]
        for component, exp in zip(components, expected):
            assert component == exp

    def test_with_no_argument_activity(self):
        path = os.path.join(PARSE_SWIPL_PATH, 'no_argument_activity_ex1.swipl')
        components = parse_swipl(path)
        assert isinstance(components, types.GeneratorType)

        expected = [
                (1, 'ORIGIN', ''),
                (2, 'PICK', '')
            ]
        for component, exp in zip(components, expected):
            assert isinstance(component, tuple)
            assert isinstance(component[0], int)
            assert isinstance(component[1], str)
            assert isinstance(component[2], str)
            assert component == exp
