from luamoon.cli.main import get_arg_parser
from luamoon.core.main import *


def main():
    parser = get_arg_parser()
    args = parser.parse_args()

    if args.subparsers == 'init':
        init_project()
    elif args.subparsers == 'add':
        add_package(args.package_name)
    elif args.subparsers == 'remove':
        remove_package(args.package_name)
    elif args.subparsers == 'list':
        list_packages()

if __name__ == '__main__':
    main()

