import re

from .parser import iterate_components
from .exception import ArgumentsError

"""
Validator Functions

Function to validate each activity. Each function use namespace 'validate_', followed by activity name.
Available activity:
- ORIGIN
- PICK
"""
def validate_origin(args_raw, line_id):
    # Parse arguments
    args = re.findall(r"([^'\s]\S*|'.+?')", args_raw)
    args_error = ArgumentsError('ORIGIN', line_id)
    args_count = len(args)

    # Argument Count
    if (args_count < 1): args_error.missing(argument_missing=ARGUMENTS['ORIGIN'][args_count])
    elif(args_count > 1): args_error.over(argument_need=1, argument_given=args_count)
    # Argument Type
    elif(not args[0].isprintable()): args_error.type(argument_type_error=ARGUMENTS['ORIGIN'][0])
    else:
        return 'ORIGIN', args

    raise args_error

def validate_pick(args_raw, line_id):
    args = re.findall(r"([^'\s]\S*|'.+?')", args_raw)
    args_error = ArgumentsError('PICK', line_id)
    args_count = len(args)

    # Argument Count
    if (args_count < 2): args_error.missing(argument_missing=ARGUMENTS['PICK'][args_count])
    elif(args_count > 2): args_error.over(argument_need=2, argument_given=args_count)
    # Argument Type
    elif(not args[0].isalnum()): args_error.type(argument_type_error=ARGUMENTS['PICK'][0])
    elif(not args[1].isprintable()): args_error.type(argument_type_error=ARGUMENTS['PICK'][1])
    else: return 'PICK', args

    raise arguments_error

"""
Validator Mapper and Function.
"""
VALIDATORS = {
    'ORIGIN': validate_origin,
    'PICK': validate_pick
}

ARGUMENTS = {
    'ORIGIN': ('URL',),
    'PICK': ('ID', 'PATH',)
}

def validate_swipl(components):
    """
    Validate swipy components.
    """
    valid_components = [VALIDATORS[activity](args, line) for line, activity, args in components]
    return True, valid_components
