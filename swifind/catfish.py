from swifind.interpreter.validator import validate_swipl
from swifind.interpreter.extractor import extract_swipl
from swifind.interpreter.parser import parse_swipl

from swifind.strategy import Strategy
from swifind.bag import Bag

class Catfish:
    """
    Default Catfish class.
    """
    def __init__(self, path):
        strategy = Strategy()
        components = validate_swipl(parse_swipl(path))
        self.strategy = extract_swipl(strategy, components)
        self.bag = Bag()

    class Closure(object):
        """
        Wrapper class for Catfish.
        """
        @classmethod
        def log_wrapper(cls, func):
            """
            Wrapper for adding log at start and end of swimming.
            """
            def wrapper(*args, **kwargs):
                [catfish] = args
                catfish.bag.add_log('start')
                func(*args, **kwargs)
                catfish.bag.add_log('end')

            return wrapper

    @Closure.log_wrapper
    def swim(self):
        """
        Start swimming.
        """
        for pointer in self.strategy.get_activity():
            pointer.func(self, pointer.order)

    def retrieve(self, include_logs=False):
        """
        Get collected item from Bag.
        """
        items = {'items': self.bag.get_items()}
        if (include_logs):
            logs = self.bag.get_logs()
            items = {**items, 'logs': logs}
        return items
