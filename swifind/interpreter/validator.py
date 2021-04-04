import re

from .parser import parse_swipy
from .exception import SwipyValidationError

def validate_root(component):
    """
    Validate syntax of root activity.
    """
    args = re.findall(r"([^'\s]\S*|'.+?')", component)
    c = [
        len(args) == 1,
        args[0].isprintable()
    ]
    return all(c)

def validate_collect(component):
    """
    Validate syntax of collect activity
    """
    args = re.findall(r"([^'\s]\S*|'.+?')", component)
    c = [
        len(args) == 2,
        args[0].isalnum(),
        args[1].isprintable()
    ]
    return all(c)

# Validator Functions
VALIDATORS = {
    'root': validate_root,
    'collect': validate_collect
}

def validate_swipy(path):
    """
    Validate swipy file from path.
    """
    components = parse_swipy(path)
    try:
        while(1):
            line_id, activity, arguments = next(components)
            if not (VALIDATORS[activity](arguments)):
                raise SwipyValidationError(activity, line_id)
    except StopIteration:
        pass
    return True
