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
    args_error = ArgumentsError('origin', line_id)
    args_count = len(args)

    # Argument Count
    if (args_count < 1): args_error.missing(argument_missing=ARGUMENTS['origin'][args_count])
    elif(args_count > 1): args_error.over(argument_need=1, argument_given=args_count)
    # Argument Type
    elif(not args[0].isprintable()): args_error.type(argument_type_error=ARGUMENTS['origin'][0])
    else: return

    raise args_error

def validate_pick(args_raw, line_id):
    args = re.findall(r"([^'\s]\S*|'.+?')", args_raw)
    args_error = ArgumentsError('pick', line_id)
    args_count = len(args)

    # Argument Count
    if (args_count < 2): args_error.missing(argument_missing=ARGUMENTS['pick'][args_count])
    elif(args_count > 2): args_error.over(argument_need=2, argument_given=args_count)
    # Argument Type
    elif(not args[0].isalnum()): args_error.type(argument_type_error=ARGUMENTS['pick'][0])
    elif(not args[1].isprintable()): args_error.type(argument_type_error=ARGUMENTS['pick'][1])
    else: return

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

@iterate_components
def validate_swipl(components):
    """
    Validate swipy components.
    """
    line_id, activity, arguments = next(components)
    VALIDATORS[activity](arguments, line_id)
    return True
