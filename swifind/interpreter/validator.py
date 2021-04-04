import re

from .parser import parse_swipy
from .exception import ArgumentsError

def validate_root(component, line_id):
    """
    Validate syntax of root activity.
    """
    args = re.findall(r"([^'\s]\S*|'.+?')", component)
    arguments_error = ArgumentsError('root', line_id)
    args_count = len(args)
    if (args_count < 1): arguments_error.missing(argument_missing=ARGUMENTS['root'][args_count])
    elif(args_count > 1): arguments_error.over(argument_need=1, argument_given=args_count)
    elif(not args[0].isprintable()): arguments_error.type(argument_type_error=ARGUMENTS['root'][0])
    else: return

    raise arguments_error

def validate_collect(component, line_id):
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

VALIDATORS = {
    'root': validate_root,
    'collect': validate_collect
}

ARGUMENTS = {
    'root': ('URL',),
    'collect': ('ID', 'PATH',)
}

# Validator Functions
def validate_swipy(path):
    """
    Validate swipy file from path.
    """
    components = parse_swipy(path)
    try:
        while(1):
            line_id, activity, arguments = next(components)
            VALIDATORS[activity](arguments, line_id)
    except StopIteration:
        pass
    return True
