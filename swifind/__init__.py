from .interpreter.validator import validate_swipl
from .interpreter.extractor import extract_swipl
from .interpreter.parser import parse_swipl

class Catfish:
    """
    Default Catfish class.
    """
    def __init__(self, path):
        self.validate = validate_swipl(parse_swipl(path))
        self.strategy = extract_swipl(parse_swipl(path))

    def swim(self):
        """
        Start swimming from root.
        """
        self.strategy.execute()
        print("Done")
