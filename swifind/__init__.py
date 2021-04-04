import requests
import bs4

from .interpreter.validator import validate_swipy
from .interpreter.extractor import extract_swipy

class Swimmer:
    """
    Default swimmer class.
    """
    def __init__(self, path):
        validate_swipy(path)
        self.root, self.strategies, self.payload = extract_swipy(path)

    def swim(self):
        """
        Start swimming from root.
        """
        req = requests.get(self.root)
        return req.status_code
