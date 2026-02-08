from luamoon.cli.main import get_arg_parser
from luamoon.core.main import *
from luamoon.core.commands import *

NOT_IMPLEMENTED_MSG = "Sorry, this feature isn’t available yet :)"

def main():
    parser = get_arg_parser()
    args = parser.parse_args()

    if args.command == 'init':
        if args.lua_version:
            change_lua_version(args.lua)
        if args.env:
            change_venv_name(args.env)

        if args.runtime == 'lua':
            init(args.type_, args.runtime)
        else:
            print(NOT_IMPLEMENTED_MSG)

    elif args.command == 'add':
        add_package(args.package_name)
    elif args.command == 'update':
        update_package(args.package_name)
    elif args.command == 'remove':
        remove_package(args.package_name)
    elif args.command == 'list':
        list_packages()
    elif args.command == 'search':
        print(NOT_IMPLEMENTED_MSG)
    elif args.command == 'publish':
        print(NOT_IMPLEMENTED_MSG)
    elif args.command == 'config':
        print(NOT_IMPLEMENTED_MSG)
    elif args.command == 'run':
        print(NOT_IMPLEMENTED_MSG)

if __name__ == '__main__':
    main()
