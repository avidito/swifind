# Validation Exception
class SwipyValidationError(Exception):
    """
    Raised when the syntax is violate swipy rule.
    """
    def __init__(self, component, line):
        message = f"Error while validate `{component}` on line {line}"
        super().__init__(message)
