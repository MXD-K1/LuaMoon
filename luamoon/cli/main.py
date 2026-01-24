import argparse

from luamoon.cli.strings import *

def get_arg_parser():
    parser = argparse.ArgumentParser(prog=NAME, description=DESCRIPTION)
    parser.add_argument('-v', '--version', action='version', version=VERSION)
    # parser.add_argument('-h', '--help', action='help', help=HELP['general'])

    subparsers = parser.add_subparsers(dest='command')

    init_parser = subparsers.add_parser('init')
    init_parser.add_argument('-l', '--lua', help=HELP['init-lua'])
    # todo: support choosing lua version
    init_parser.add_argument('-e', '--env', help=HELP['init-env'])
    # todo: venv name is not changing fix that.

    add_parser = subparsers.add_parser('add')
    add_parser.add_argument('package_name')

    remove_parser = subparsers.add_parser('remove')
    remove_parser.add_argument('package_name')

    subparsers.add_parser('list')

    return parser
