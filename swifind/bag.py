from datetime import datetime

class Bag:
    """
    Data container to hold collected data from web-scraping.
    """
    def __init__(self):
        self.data = {}
        self.logs = {
                'swimming':{'counter': 0},
                'activity':[]
            }

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

    def log_activity(self, activity, line, status='PASS'):
        """
        Logging status of activity.
        """
        log = {
            'activity': activity,
            'order': self.logs['swimming']['counter'],
            'line': line,
            'status': status,
            'timestamp': datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        }
        self.logs['activity'].append(log)
        self.logs['swimming']['counter'] += 1

    def add_item(self, id, content):
        """
        Add content to bag.
        """
        self.data[id] = content
