import requests
import bs4

from .interpreter.validator import validate_script
from .interpreter.extractor import root_extract

class Swimmer:
    """
    Default swimmer class.
    """
    def __init__(self, path):
        validate_script(path)
        self.root = root_extract(path)

    def swim(self):
        """
        Start swimming from root.
        """
        req = requests.get(self.root)
        return req.status_code
