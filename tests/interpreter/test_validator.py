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
    def test_with_valid_arguments(self):
        assert validate_pick("title 'body > div > div.row.header-box > div.col-md-8 > h1 > a'", 10)
        assert validate_pick("content 'body > div > p > a'", 10)
        assert validate_pick("subtitle 'body > div > div.row.header-box > h2'", 10)

    def test_with_missing_arguments(self):
        with pytest.raises(ArgumentsError) as exception_info:
            validate_pick('', 10)
            assert exception_info.match("'PICK' activity missing required arguments: 'ID' at line 10.")

        with pytest.raises(ArgumentsError) as exception_info:
            validate_pick('quotes', 10)
            assert exception_info.match("'PICK' activity missing required arguments: 'URL' at line 10.")

class TestValidateSwipl(object):
    ... # Implement later
