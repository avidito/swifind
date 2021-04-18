from datetime import datetime

from swifind.constant import ALL_ACTIVITY

class Bag:
    """
    Data container to hold collected data from web-scraping.
    """
    def __init__(self):
        self.items = {}
        self.logs = {
                'swimming':{'counter': 0},
                'activity':[]
            }

    # Getter Methods
    def get_items(self):
        """
        Retrieve all collected data.
        """
        items = {**self.items}
        return items

    def get_logs(self):
        """
        Retrieve all logs data.
        """
        logs = {**self.logs}
        return logs

    # Adder Methods
    def add_item(self, id, content):
        """
        Add content to bag.
        """
        self.items[id] = content

    def add_log(self, mode, *args, **kwargs):
        """
        Add log of activity or journey to bag.
        """
        timestamp = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        if mode in ('start', 'end', 'unpack'):
            self.logs['swimming'][f'{mode}_time'] = timestamp
        elif mode in ALL_ACTIVITY:
            [line, order] = args
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
