import os
import pytest

from tests.constant import VALIDATE_SWIPL_PATH

from swifind.interpreter.validator import (validate_origin,
                                           validate_pick,
                                           validate_swim,
                                           validate_swipl)
from swifind.exception import ArgumentsError
from swifind.interpreter.parser import parse_swipl

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
        msg = "'URL' from 'ORIGIN' activity violates swipl rule at line 1."
        with pytest.raises(ArgumentsError, match=f"^{msg}$") as exception_info:
            validate_origin("http:\b//www.com", 1)

class TestValidatePick(object):
    def test_with_valid_arguments(self):
        assert validate_pick("title 'h1 a'", 10)
        assert validate_pick("content 'div p a'", 10)
        assert validate_pick("subtitle 'div row h2'", 10)
        assert validate_pick("cls 'div div' class", 10)
        assert validate_pick("span 'div div[1]' class", 10)
        assert validate_pick("quote 'div div[1] div[2]'", 5)

    def test_with_missing_arguments(self):
        msg = "'PICK' activity missing required arguments: 'ID' at line 10."
        with pytest.raises(ArgumentsError, match=f"^{msg}$") as exception_info:
            validate_pick('', 10)

        msg = "'PICK' activity missing required arguments: 'PATH' at line 10."
        with pytest.raises(ArgumentsError, match=f"^{msg}$") as exception_info:
            validate_pick('quotes', 10)

    def test_with_too_many_arguments(self):
        msg = "'PICK' activity takes 2 arguments, but 4 were given at line 10."
        with pytest.raises(ArgumentsError, match=f"^{msg}$") as exception_info:
            validate_pick("title extra miles 'h1 a'", 10)

        msg = "'PICK' activity takes 2 arguments, but 7 were given at line 10."
        with pytest.raises(ArgumentsError, match=f"^{msg}$") as exception_info:
            validate_pick("title body div div.row.header-box div.col-md-8 h1 a", 10)

        msg = "'PICK' activity takes 2 arguments, but 4 were given at line 10."
        with pytest.raises(ArgumentsError, match=f"^{msg}$") as exception_info:
            validate_pick("title 'body div 'h1'' href", 10)

    def test_with_invalid_data_type(self):
        msg = "'ID' from 'PICK' activity violates swipl rule at line 10."
        with pytest.raises(ArgumentsError, match=f"^{msg}$") as exception_info:
            validate_pick("?!?! 'body h1 a'", 10)

        msg = "'PATH' from 'PICK' activity violates swipl rule at line 10."
        with pytest.raises(ArgumentsError, match=f"^{msg}$") as exception_info:
            validate_pick("abc 'body h1 \b a'", 10)

        msg = "'ATTR' from 'PICK' activity violates swipl rule at line 10."
        with pytest.raises(ArgumentsError, match=f"^{msg}$") as exception_info:
            validate_pick("head 'body h1 a' h!ref", 10)

    def test_with_invalid_path_indexes(self):
        msg = "indexes in 'PATH' from 'PICK' violates swiple rule at line 10."
        with pytest.raises(ArgumentsError, match=f"^{msg}$") as exception_info:
            validate_pick("quote 'div div[x] span'", 10)

        msg = "indexes in 'PATH' from 'PICK' violates swiple rule at line 10."
        with pytest.raises(ArgumentsError, match=f"^{msg}$") as exception_info:
            validate_pick("quote 'div[1!] span'", 10)

class TestValidateSwipl(object):
    def test_return_values_datatype(self):
        path = os.path.join(VALIDATE_SWIPL_PATH, 'valid_components_ex1.swipl')
        components = validate_swipl(parse_swipl(path))
        assert (isinstance(components, list))

        for component in components:
            assert isinstance(component, tuple)

    def test_with_valid_components(self):
        path = os.path.join(VALIDATE_SWIPL_PATH, 'valid_components_ex1.swipl')
        result_components = validate_swipl(parse_swipl(path))
        expected_components = [('ORIGIN', ['https://quotes.toscrape.com/'], 1),
                               ('PICK', ['title', "'h1 a'", None], 3),
                               ('PICK', ['header', "'div div row header-box'", None], 4)]
        assert result_components == expected_components

    def test_with_invalid_components(self):
        path = os.path.join(VALIDATE_SWIPL_PATH, 'invalid_components_ex1.swipl')
        msg = "'ORIGIN' activity missing required arguments: 'URL' at line 1."
        with pytest.raises(ArgumentsError, match=f"^{msg}$") as exception_info:
            validate_swipl(parse_swipl(path))

class TestValidateSwim(object):
    def test_with_valid_arguments(self):
        assert validate_swim('https://www.test.com', 1)
        assert validate_swim('https://sub.check.com', 1)
        assert validate_swim('www.hello.com', 1)

    def test_with_missing_arguments(self):
        msg = "'SWIM' activity missing required arguments: 'URL' at line 1."
        with pytest.raises(ArgumentsError, match=f"^{msg}$") as exception_info:
            validate_swim('', 1)

    def test_with_too_many_arguments(self):
        msg = "'SWIM' activity takes 1 arguments, but 2 were given at line 1."
        with pytest.raises(ArgumentsError, match=f"^{msg}$") as exception_info:
            validate_swim('https://www.test.com testing_dot_com', 1)

        msg = "'SWIM' activity takes 1 arguments, but 4 were given at line 1."
        with pytest.raises(ArgumentsError, match=f"^{msg}$") as exception_info:
            validate_swim('https://www.test.com testing dot com', 1)

    def test_with_invalid_data_type(self):
        msg = "'URL' from 'SWIM' activity violates swipl rule at line 1."
        with pytest.raises(ArgumentsError, match=f"^{msg}$") as exception_info:
            validate_swim("http:\b//www.com", 1)
