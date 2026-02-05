import argparse

from luamoon.cli import *

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

    group = init_parser.add_mutually_exclusive_group()
    group.add_argument('--lib', dest='type_', action='store_const', const='lib')
    group.add_argument('--project', dest='type_', action='store_const', const='project')
    init_parser.set_defaults(type_='project')

    add_parser = subparsers.add_parser('add')
    add_parser.add_argument('package_name')

    remove_parser = subparsers.add_parser('remove')
    remove_parser.add_argument('package_name')

    update_parser = subparsers.add_parser('update')
    update_parser.add_argument('package_name')

    search_parser = subparsers.add_parser('search')
    search_parser.add_argument('package_name')

    config_parser = subparsers.add_parser('config')
    config_parser.add_argument('key', nargs='?')
    config_parser.add_argument('value', nargs='?')
    config_parser.add_argument('--list')  # lists the key-value pairs
    config_parser.add_argument('--global', dest='global_')
    config_parser.add_argument('--reset')
    # todo: handle the cases where key and value are needed but not provided
    # todo: if only key is provided print its value

    subparsers.add_parser('list')  # list deps
    subparsers.add_parser('run')  # run a project
    subparsers.add_parser('publish')  # publish a library
    subparsers.add_parser('luarocks')
    # todo: luarocks integration

    return parser
