from luamoon.cli.main import get_arg_parser
from luamoon.core.main import *
from luamoon.core.commands import *


def main():
    parser = get_arg_parser()
    args = parser.parse_args()

    if args.command == 'init':
        if args.lua:
            change_lua_version(args.lua)
        if args.env:
            change_venv_name(args.env)
        init_project()

    elif args.command == 'add':
        add_package(args.package_name)
    elif args.command == 'remove':
        remove_package(args.package_name)
    elif args.command == 'list':
        list_packages()

if __name__ == '__main__':
    main()

