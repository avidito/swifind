def read_script(path):
    """
    Reading script from path.
    """
    with open(path, 'r') as f:
        raw = f.read()
    return raw

def validate_script(path):
    """
    Validate swipy file from path.
    """
    raw = read_script(path).split('\n')
    for row in raw[-1]:
        component = row.split(' ')[0]
        if (validator[component](row)):
            return False
    return True

def root_validation(script):
    """
    Validate syntax of root command.
    """
    c1 = len(script.split('=')) == 2
    return (c1)

validator = {
    'root': root_validation,
}
