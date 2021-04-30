import re

from ..exception import ArgumentsError

"""
Validator Functions

Function to validate each activity. Each function use namespace 'validate_', followed by activity name.
Available activity:
- ORIGIN
- PICK
- SWIM
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
        return 'ORIGIN', args, line_id

    raise args_error

def validate_pick(args_raw, line_id):
    args = re.findall(r"([^'\s]\S*|'.+?')", args_raw)
    args_error = ArgumentsError('PICK', line_id)
    args_count = len(args)
    if (args_count > 1):
        indexes = re.findall(r"(?<=\[)[^\s]+(?=\])", args[1])
        selectors = re.findall(r"(?<=\{)[^\s]+(?=\})", args[1])
    else:
        indexes = ''
        selectors = ''

    # Argument Count
    if (args_count < 2): args_error.missing(argument_missing=ARGUMENTS['PICK'][args_count])
    elif(args_count > 3): args_error.over(argument_need=2, argument_given=args_count)

    # Argument Type
    elif(not re.match(r"^[a-zA-Z0-9_]+$", args[0])): args_error.type(argument_type_error=ARGUMENTS['PICK'][0])
    elif(not args[1].isprintable()): args_error.type(argument_type_error=ARGUMENTS['PICK'][1])

    # Default Argument type
    elif(len(args) == 3 and not args[2].isalnum()): args_error.type(argument_type_error=ARGUMENTS['PICK'][2])

    # Index Type
    elif(indexes and any(map(lambda x: not x.isnumeric(), indexes))): args_error.type(argument_type_error=ARGUMENTS['PICK'][1], sub_argument='indexes')
    elif(selectors and any(map(lambda x: not x.isprintable(), selectors))): args_error.type(argument_type_error=ARGUMENTS['PICK'][1], sub_argument='selectors')
    else:
        if len(args) < 3:
            args = [*args, None]
        return 'PICK', args, line_id

    raise args_error

def validate_swim(args_raw, line_id):
    # Parse arguments
    args = re.findall(r"([^'\s]\S*|'.+?')", args_raw)
    args_error = ArgumentsError('SWIM', line_id)
    args_count = len(args)

    # Argument Count
    if (args_count < 1): args_error.missing(argument_missing=ARGUMENTS['SWIM'][args_count])
    elif(args_count > 1): args_error.over(argument_need=1, argument_given=args_count)

    # Argument Type
    elif(not args[0].isprintable()): args_error.type(argument_type_error=ARGUMENTS['SWIM'][0])
    else:
        return 'SWIM', args, line_id

    raise args_error

"""
Validator Mapper and Function.
"""
VALIDATORS = {
    'ORIGIN': validate_origin,
    'PICK': validate_pick,
    'SWIM': validate_swim
}

ARGUMENTS = {
    'ORIGIN': ('URL',),
    'PICK': ('ID', 'PATH', 'ATTR'),
    'SWIM': ('URL',)
}

def validate_swipl(components):
    """
    Validate swipy components.
    """
    valid_components = [VALIDATORS[activity](args, line) for line, activity, args in components]
    return valid_components
