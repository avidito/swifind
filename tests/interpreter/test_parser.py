import os
import types
import pytest

from tests.constant import READ_SCRIPT_PATH

from swifind.interpreter.parser import (read_script,
                                        parse_swipl)

class TestReadScript(object):
    def test_with_valid_script(self):
        path = os.path.join(READ_SCRIPT_PATH, 'valid_components_ex1.swipl')
        raw_components = read_script(path)
        assert isinstance(raw_components, types.GeneratorType)
        for component in raw_components:
            assert isinstance(component, tuple)
            assert isinstance(component[0], int)
            assert isinstance(component[1], str)

    def test_with_empty_script(self):
        path = os.path.join(READ_SCRIPT_PATH, 'empty_script.swipl')
        raw_components = read_script(path)
        assert isinstance(raw_components, types.GeneratorType)

        with pytest.raises(StopIteration) as exception_info:
            next(raw_components)

class TestParseSwipl(object):
    def test_with_valid_script(self):
        ... # Implement later

    def test_with_no_argument_activity(self):
        ... # Implement later
