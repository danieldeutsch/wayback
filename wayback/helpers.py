import argparse
import dateutil.parser


def validate_time(arg):
    try:
        return dateutil.parser.parse(arg, fuzzy=True)
    except ValueError:
        message = 'Not a valid date: {}'.format(arg)
        raise argparse.ArgumentTypeError(message)
