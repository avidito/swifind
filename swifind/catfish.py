from swifind.interpreter.validator import validate_swipl
from swifind.interpreter.extractor import extract_swipl
from swifind.interpreter.parser import parse_swipl
from swifind.bag import Bag

class Catfish:
    """
    Default Catfish class.
    """
    def __init__(self, path):
        self.validate = validate_swipl(parse_swipl(path))
        self.strategy = extract_swipl(parse_swipl(path))
        self.bag = Bag()

    def swim(self):
        """
        Start swimming from origin.
        """
        self.strategy.execute()
        print("Done")

    def unpack(self):
        """
        Unpack Bag content.
        """
        return self.bag.get_all()
