import re

from .utils import read_script
from .exception import SwipyValidationError

def validate_root(component):
    """
    Validate syntax of root activity.
    """
    args = re.findall(r"[^'\s]\S*|'.+?'", component)[1:]
    c = [
        len(args) == 1,
        args[0].isprintable()
    ]
    return all(c)

def validate_collect(component):
    """
    Validate syntax of collect activity
    """
    args = re.findall(r"[^'\s]\S*|'.+?'", component)[1:]
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
    components = read_script(path)
    for line, component in enumerate(components):
        activity = component.split(' ', 1)[0]
        if not (VALIDATORS[activity](component)):
            raise SwipyValidationError(activity, line)
    return True
