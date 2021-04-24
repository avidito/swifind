import pytest

from swifind.exception import (SwiplError,
                               ArgumentsError,
                               LogicalError,
                               SwifindError,
                               ObjectTypeError)

class TestSwiplError(object):
    def test_inheritance(self):
        sp_error = SwiplError("Test")
        assert isinstance(sp_error, Exception)

    def test_valid_error_message(self):
        error_msg = "Exception message"
        sp_error = SwiplError(error_msg)
        with pytest.raises(SwiplError, match=f"^{error_msg}$") as exception_info:
            raise sp_error

class TestArgumentsError(object):
    def test_inheritance(self):
        args_error = ArgumentsError('ORIGIN', 1)
        assert isinstance(args_error, SwiplError)
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

    def test_with_invalid_subtype_condition(self):
        args_error = ArgumentsError('PICK', 10)

        args_error.type('PATH', 'indexes')
        msg = "indexes in 'PATH' from 'PICK' violates swiple rule at line 10."
        with pytest.raises(ArgumentsError, match=f"^{msg}$") as exception_info:
            raise args_error

class TestLogicalError(object):
    def test_inheritance(self):
        logical_error = LogicalError('ORIGIN', 'must be valid.', 10)
        assert isinstance(logical_error, SwiplError)
        assert isinstance(logical_error, Exception)

    def test_with_logical_error(self):
        logical_error = LogicalError('ORIGIN', 'must be valid.', 10)
        msg = "Error at line 10: 'ORIGIN' activity must be valid."
        with pytest.raises(LogicalError, match=f"^{msg}$") as exception_info:
            raise logical_error

class TestSwifindError(object):
    def test_inheritance(self):
        sf_error = SwifindError('Test')
        assert isinstance(sf_error, Exception)

    def test_valid_error_message(self):
        error_msg = "Exception Message"
        sf_error = SwifindError(error_msg)
        with pytest.raises(SwifindError, match=f"^{error_msg}$") as exception_info:
            raise sf_error

class TestObjectTypeError(object):
    def test_inheritance(self):
        object_error = ObjectTypeError('Object Type Test')
        assert isinstance(object_error, SwifindError)
        assert isinstance(object_error, Exception)

    def test_valid_error_message(self):
        error_msg = "'Plan' must be linked with 'Plan' object, not 'int' object."
        object_error = ObjectTypeError(error_msg)
        with pytest.raises(ObjectTypeError, match=f"^{error_msg}$") as exception_info:
            raise object_error
