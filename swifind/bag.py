class Bag:
    """
    Data container to hold collected data from web-scraping.
    """
    def __init__(self):
        self.data = {
            "origin": "https://quotes.toscrape.com/",
            "title": "Quotes to Scrape"
        }

    def get_all(self):
        """
        Take out all information inside bag.
        """
        result = {k:v for k, v in self.data.items()}
        self.data = {}
        return result
