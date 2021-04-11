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
        msg = "'ORIGIN' activity missing required arguments: 'URL' at line 1."
        with pytest.raises(ArgumentsError, match=f"^{msg}$") as exception_info:
            validate_origin('', 1)

    def test_with_too_many_arguments(self):
        msg = "'ORIGIN' activity takes 1 arguments, but 2 were given at line 1."
        with pytest.raises(ArgumentsError, match=f"^{msg}$") as exception_info:
            validate_origin('https://www.test.com testing_dot_com', 1)

        msg = "'ORIGIN' activity takes 1 arguments, but 4 were given at line 1."
        with pytest.raises(ArgumentsError, match=f"^{msg}$") as exception_info:
            validate_origin('https://www.test.com testing dot com', 1)

    def test_with_invalid_data_type(self):
        msg = "`URL` from `ORIGIN` activity is violates swipy rule at line 1."
        with pytest.raises(ArgumentsError, match=f"^{msg}$") as exception_info:
            validate_origin("http:\b//www.com", 1)

class TestValidatePick(object):
    def test_with_valid_arguments(self):
        assert validate_pick("title 'body > div > div.row.header-box > div.col-md-8 > h1 > a'", 10)
        assert validate_pick("content 'body > div > p > a'", 10)
        assert validate_pick("subtitle 'body > div > div.row.header-box > h2'", 10)

    def test_with_missing_arguments(self):
        msg = "'PICK' activity missing required arguments: 'ID' at line 10."
        with pytest.raises(ArgumentsError, match=f"^{msg}$") as exception_info:
            validate_pick('', 10)

        msg = "'PICK' activity missing required arguments: 'PATH' at line 10."
        with pytest.raises(ArgumentsError, match=f"^{msg}$") as exception_info:
            validate_pick('quotes', 10)

    def test_with_too_many_arguments(self):
        msg = "'PICK' activity takes 2 arguments, but 3 were given at line 10."
        with pytest.raises(ArgumentsError, match=f"^{msg}$") as exception_info:
            validate_pick("title extra 'body > div > div.row.header-box > div.col-md-8 > h1 > a'", 10)

        msg = "'PICK' activity takes 2 arguments, but 12 were given at line 10."
        with pytest.raises(ArgumentsError, match=f"^{msg}$") as exception_info:
            validate_pick("title body > div > div.row.header-box > div.col-md-8 > h1 > a", 10)

        msg = "'PICK' activity takes 2 arguments, but 5 were given at line 10."
        with pytest.raises(ArgumentsError, match=f"^{msg}$") as exception_info:
            validate_pick("title 'body > div > 'h1' > a'", 10)

    def test_with_invalid_data_type(self):
        msg = "`ID` from `PICK` activity is violates swipy rule at line 10."
        with pytest.raises(ArgumentsError, match=f"^{msg}$") as exception_info:
            validate_pick("?!?! 'body > h1 > a'", 10)

        msg = "`PATH` from `PICK` activity is violates swipy rule at line 10."
        with pytest.raises(ArgumentsError, match=f"^{msg}$") as exception_info:
            validate_pick("abc 'body > h1 \b> a'", 10)

class TestValidateSwipl(object):
    ... # Implement later
