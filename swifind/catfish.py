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
        self.strategy = extract_swipl(self.strategy, components)

    def swim(self):
        """
        Start swimming.
        """
        self.bag.log_swimming('start')
        for pointer in self.strategy.get_activity():
            result = pointer.func(self)
            print(result)
        self.bag.log_swimming('start')

    def unpack(self):
        """
        Unpack Bag content.
        """
        return self.bag.data

    def _assign_view(self, view):
        """
        Change catfish active pageview.
        """
        self.view = view
