class SwiplError(Exception):
    """
    Raised when the swipl script is violate swipl rule.
    """
    def __init__(self, message):
        super().__init__(message)

class ArgumentsError(SwiplError):
    """
    Raised when activity arguments violate swipl rule.
    """
    def __init__(self, activity, line_id):
        self.activity = activity
        self.line_id = line_id

    def missing(self, argument_missing):
        """
        Raised when there is missing arguments.
        """
        message = f"'{self.activity}' activity missing required arguments: '{argument_missing}' at line {self.line_id}."
        super().__init__(message)

    def over(self, argument_need, argument_given):
        """
        Raised when there is too many arguments.
        """
        message = f"'{self.activity}' activity takes {argument_need} arguments, but {argument_given} were given at line {self.line_id}."
        super().__init__(message)

    def type(self, argument_type_error):
        """
        Raised when there is arguments with wrong format or data type.
        """
        message = f"'{argument_type_error}' from '{self.activity}' activity violates swipl rule at line {self.line_id}."
        super().__init__(message)

class LogicalError(SwiplError):
    """
    Raised when activity plan violate sequence rule.
    """
    def __init__(self, activity, message, line):
        error_message = f"Error at line {line}: '{activity}' activity {message}"
        super().__init__(error_message)
