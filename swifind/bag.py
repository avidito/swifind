from datetime import datetime

class Bag:
    """
    Data container to hold collected data from web-scraping.
    """
    def __init__(self):
        self.data = {
            "origin": "https://quotes.toscrape.com/",
            "title": "Quotes to Scrape"
        }
        self.logs = {'swimming':{}, 'activity':[]}

    def get_all(self):
        """
        Take out all information inside bag.
        """
        result = {k:v for k, v in self.data.items()}
        self.data = {}
        return result

    def log_swimming(self, mode):
        timestamp = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        self.logs['swimming'][f'{mode}_time'] = timestamp

    def log_activity(self, activity, order, line, status='PASS'):
        """
        Logging status of activity.
        """
        log = {
            'activity': activity,
            'order': order,
            'line': line,
            'status': status,
            'timestamp': datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        }
        self.logs['activity'].append(log)
