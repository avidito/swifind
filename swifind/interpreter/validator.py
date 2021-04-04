from .utils import read_script
from .exception import SwipyValidationError

def validate_root(component):
    """
    Validate syntax of root activity.
    """
    c1 = component.count(' ') == 1
    return c1

# Validator Functions
VALIDATORS = {
    'root': validate_root,
}

def validate_swipy(path):
    """
    Validate swipy file from path.
    """
    raw = read_script(path)[:-1].split('\n')
    for line, row in enumerate(raw):
        component = row.split(' ', 1)[0]
        if not (VALIDATORS[component](row)):
            raise SwipyValidationError(component, line)
    return True
