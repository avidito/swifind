from swifind.interpreter.validator import validate_swipl
from swifind.interpreter.extractor import extract_swipl
from swifind.interpreter.parser import parse_swipl

from swifind.strategy import Strategy
from swifind.bag import Bag

class Catfish:
    """
    Default Catfish class.
    """
    def __init__(self):
        self.validate = False
        self.strategy = Strategy()
        self.bag = Bag()

    def prepare(self, path):
        """
        Initiate swiming strategy from swipl script.
        """
        self.validate, components = validate_swipl(parse_swipl(path))

        components = parse_swipl(path) # Temporary
        self.strategy = extract_swipl(components)

    def swim(self):
        """
        Start swimming.
        """
        print("Swimming") # Temporary

    def unpack(self):
        """
        Unpack Bag content.
        """
        return {"testing_key":"testing_result"}
