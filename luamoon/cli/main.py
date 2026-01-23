import argparse
from os import remove

from colorama import Fore, Style

from strings import *

def get_arg_parser():
    parser = argparse.ArgumentParser(prog=NAME, description=DESCRIPTION)
    parser.add_argument('-v', '--version', action='version', version=VERSION)
    # parser.add_argument('-h', '--help', action='help', help=HELP['general'])

    subparsers = parser.add_subparsers(dest='subparsers')

    subparsers.add_parser('init')

    add_parser = subparsers.add_parser('add')
    add_parser.add_argument('package_name')

    remove_parser = subparsers.add_parser('remove')
    remove_parser.add_argument('package_name')

    subparsers.add_parser('list')

    return parser


if __name__ == '__main__':
    _parser = get_arg_parser()
    parsed_args = _parser.parse_args()
    print(parsed_args)
