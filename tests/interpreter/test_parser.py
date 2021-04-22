import os
import types
import pytest

from tests.constant import READ_SCRIPT_PATH, PARSE_SWIPL_PATH

from swifind.interpreter.parser import (read_script,
                                        parse_swipl)

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
