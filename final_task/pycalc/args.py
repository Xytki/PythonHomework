"""args module"""
import argparse


def prepare_parser():
    """Handle the command line arguments."""

    parser = argparse.ArgumentParser(description='Python command-line calculator')

    parser.add_argument(
        '-m',
        '--modules',
        default=[],
        dest='modules',
        metavar='MODULE',
        action="append",
        help='Additional modules to import'
    )
    parser.add_argument(
        'expr',
        nargs=1,
        metavar='EXPRESSION',
        help='Expression string'
    )

    return parser.parse_args()
