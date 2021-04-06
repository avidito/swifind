import requests
import bs4

from .interpreter.validator import validate_swipy
from .interpreter.extractor import extract_swipy
from .interpreter.parser import parse_swipy

class Swimmer:
    """
    Default swimmer class.
    """
    def __init__(self, path):
        self.validate = validate_swipy(parse_swipy(path))
        self.strategy = extract_swipy(parse_swipy(path))

    def swim(self):
        """
        Start swimming from root.
        """
        self.strategy.execute()
        print("Done")
