import pytest
from swifind.interpreter.exception import ArgumentsError
from swifind.interpreter.validator import (validate_origin,
                                           validate_pick,
                                           validate_swipl)

class TestValidateOrigin(object):
    def test_with_valid_arguments(self):
        assert validate_origin('https://www.test.com', 1)
        assert validate_origin('https://sub.check.com', 1)
        assert validate_origin('www.hello.com', 1)

    def test_with_missing_arguments(self):
        with pytest.raises(ArgumentsError) as exception_info:
            validate_origin('', 1)
            assert exception_info.match("'ORIGIN' activity missing required arguments: 'URL' at line 1.") 

class TestValidatePick(object):
    ... # Implement later

class TestValidateSwipl(object):
    ... # Implement later
