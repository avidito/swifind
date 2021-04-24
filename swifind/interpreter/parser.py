import re

def read_script(path):
    """
    Reading script from path and remove empty string.
    """
    with open(path, 'r') as f:
        raw = f.read().strip()
    raw_components = ((id+1, line.strip()) for id, line in enumerate(raw.split('\n')) if (line.strip()))
    return raw_components

def parse_swipl(path):
    """
    Parse swipl script to list of component.
    """
    raw_components = read_script(path)
    components = ((line_id, *line.split(' ', 1)) for line_id, line in raw_components)
    components_padded_args = ((line, *activity) if (len(activity) == 2) else (line, *activity, '') for line, *activity in components)
    return components_padded_args

def parse_recursive_tag(tag):
    if (tag):
        if(tag[-1] == '*'):
            return tag[:-1], True
        elif (tag[-1] != '*'):
            return tag, False

def parse_basic_element(element):
    tag = element.strip()
    [tag, rflag] = parse_recursive_tag(tag)
    return ('find',), tag, {'recursive': rflag}

def parse_element_with_index(element):
    [tag, index] = element[:-1].split('[')
    [tag, rflag] = parse_recursive_tag(tag)
    return ('find_all', int(index)), tag, {'recursive': rflag}

def parse_element_with_selector(element):
    [tag, selector] = element[:-1].split('{')
    [prop, value] = selector.split('=')
    [tag, rflag] = parse_recursive_tag(tag)
    attrs = { prop: value.strip('"') }
    return ('find',), tag, {'attrs': attrs, 'recursive': rflag}

def parse_element_notation(element):
    if (re.match(r".+\[\S+\]", element)):
        return parse_element_with_index(element)

    if(re.match(r".+\{\S+\}", element)):
        return parse_element_with_selector(element)

    return parse_basic_element(element)
