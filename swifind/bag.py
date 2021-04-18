from datetime import datetime

from swifind.constant import ALL_ACTIVITY

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

    def add_log(self, mode, *args, **kwargs):
        """
        Add log of activity or journey to bag.
        """
        timestamp = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        if mode in ('start', 'end', 'unpack'):
            self.logs['swimming'][f'{mode}_time'] = timestamp
        elif mode in ALL_ACTIVITY:
            [line] = args
            status = kwargs.get('status')
            log = {
                'activity': mode,
                'order': self.logs['swimming']['counter'],
                'line': line,
                'status': status if (status) else 'PASS',
                'timestamp': datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            }
            self.logs['activity'].append(log)
            self.logs['swimming']['counter'] += 1

    def add_item(self, id, content):
        """
        Add content to bag.
        """
        self.data[id] = content
