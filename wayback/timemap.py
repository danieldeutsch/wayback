import json
import requests
from datetime import datetime


_endpoint = 'http://web.archive.org/web/timemap/json/'


class Timemap(object):
    def __init__(self, url, timestamp, status_code):
        self.url = url
        self.date = datetime.strptime(timestamp, '%Y%m%d%H%M%S')
        self.timestamp = timestamp
        self.status_code = status_code


def timemap(url, start=None, end=None):
    timemaps = []
    endpoint = _endpoint + url
    response = requests.get(endpoint)
    data = json.loads(response.content.decode('utf-8'))
    for row in data[1:]:
        time = Timemap(row[2], row[1], row[4])
        if (not start or start <= time.date) and (not end or time.date <= end):
            timemaps.append(time)
    return timemaps
