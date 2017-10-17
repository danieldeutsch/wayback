import argparse
import os
import requests

import wayback
from wayback import ProgressBar
from wayback.helpers import validate_time

_endpoint = 'http://web.archive.org/web/'


def scrape(url, timestamp=None):
    endpoint = _endpoint
    if timestamp:
        endpoint += timestamp
    endpoint += '/' + url

    response = requests.get(endpoint)
    return response.content


def _get_filename(output_dir, url, date):
    return os.path.join(output_dir, url, date.strftime('%Y/%m/%d'), date.strftime('%Y%m%d%H%M%S') + '.html')


def main(args):
    for url in ProgressBar(args.urls, lambda url: url):
        timemaps = wayback.timemap(url, args.start_date, args.end_date)
        for time in ProgressBar(timemaps, lambda time: time.timestamp):
            filename = _get_filename(args.output_dir, url, time.date)
            directory = os.path.split(filename)[0]
            if not os.path.exists(directory):
                os.makedirs(directory)

            if args.force or not os.path.exists(filename):
                with open(filename, 'wb') as out_file:
                    out_file.write(scrape(time.url, time.timestamp))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--urls', nargs='+', type=str, required=True)
    parser.add_argument('-s', '--start-date', type=validate_time, required=True)
    parser.add_argument('-e', '--end-date', type=validate_time, required=True)
    parser.add_argument('-o', '--output-dir', type=str, required=True)
    parser.add_argument('-f', '--force', action='store_true', required=False)
    args = parser.parse_args()

    main(args)
