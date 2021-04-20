import pytest

from swifind.exception import (SwiplValidationError,
                               ArgumentsError)

class TestSwiplValidationError(object):
    def test_inheritance(self):
        sw_error = SwiplValidationError("Test")
        assert isinstance(sw_error, Exception)

    def test_valid_error_message(self):
        msg = "Exception message"
        sw_error = SwiplValidationError(msg)
        with pytest.raises(SwiplValidationError, match=f"^{msg}$") as exception_info:
            raise sw_error

class TestArgumentsError(object):
    def test_inheritance(self):
        args_error = ArgumentsError('ORIGIN', 1)
        assert isinstance(args_error, SwiplValidationError)
        assert isinstance(args_error, Exception)

    def test_with_missing_arguments_condition(self):
        args_error = ArgumentsError('PICK', 10)

        args_error.missing('ID')
        msg = "'PICK' activity missing required arguments: 'ID' at line 10."
        with pytest.raises(ArgumentsError, match=f"^{msg}$") as exception_info:
            raise args_error

        args_error.missing('PATH')
        msg = "'PICK' activity missing required arguments: 'PATH' at line 10."
        with pytest.raises(ArgumentsError, match=f"^{msg}$") as exception_info:
            raise args_error

    def test_with_over_arguments_condition(self):
        args_error = ArgumentsError('ORIGIN', 1)

        args_error.over(1, 2)
        msg = "'ORIGIN' activity takes 1 arguments, but 2 were given at line 1."
        with pytest.raises(ArgumentsError, match=f"^{msg}$") as exception_info:
            raise args_error

        args_error.over(1, 10)
        msg = "'ORIGIN' activity takes 1 arguments, but 10 were given at line 1."
        with pytest.raises(ArgumentsError, match=f"^{msg}$") as exception_info:
            raise args_error

    def test_with_invalid_type_condition(self):
        args_error = ArgumentsError('PICK', 10)

        args_error.type('ID')
        msg = "'ID' from 'PICK' activity violates swipl rule at line 10."
        with pytest.raises(ArgumentsError, match=f"^{msg}$") as exception_info:
            raise args_error

        args_error.type('PATH')
        msg = "'PATH' from 'PICK' activity violates swipl rule at line 10."
        with pytest.raises(ArgumentsError, match=f"^{msg}$") as exception_info:
            raise args_error
