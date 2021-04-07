import re

from .parser import iterate_components
from .exception import ArgumentsError

def validate_root(args_raw, line_id):
    """
    Validate syntax of root activity.
    """
    args = re.findall(r"([^'\s]\S*|'.+?')", args_raw)
    args_error = ArgumentsError('root', line_id)
    args_count = len(args)

    # Argument Count
    if (args_count < 1): args_error.missing(argument_missing=ARGUMENTS['root'][args_count])
    elif(args_count > 1): args_error.over(argument_need=1, argument_given=args_count)
    # Argument Type
    elif(not args[0].isprintable()): args_error.type(argument_type_error=ARGUMENTS['root'][0])
    else: return

    raise args_error

def validate_collect(args_raw, line_id):
    """
    Validate syntax of collect activity
    """
    args = re.findall(r"([^'\s]\S*|'.+?')", args_raw)
    args_error = ArgumentsError('collect', line_id)
    args_count = len(args)

    # Argument Count
    if (args_count < 2): args_error.missing(argument_missing=ARGUMENTS['collect'][args_count])
    elif(args_count > 2): args_error.over(argument_need=2, argument_given=args_count)
    # Argument Type
    elif(not args[0].isalnum()): args_error.type(argument_type_error=ARGUMENTS['collect'][0])
    elif(not args[1].isprintable()): args_error.type(argument_type_error=ARGUMENTS['collect'][1])
    else: return

    raise arguments_error

# Mapper
VALIDATORS = {
    'ROOT': validate_root,
    'COLLECT': validate_collect
}

ARGUMENTS = {
    'ROOT': ('URL',),
    'COLLECT': ('ID', 'PATH',)
}

# Validator Functions
@iterate_components
def validate_swipy(components):
    """
    Validate swipy components.
    """
    line_id, activity, arguments = next(components)
    VALIDATORS[activity](arguments, line_id)
    return True
