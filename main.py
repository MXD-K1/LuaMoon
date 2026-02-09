from luamoon.cli.main import get_arg_parser
from luamoon.core.main import *
from luamoon.core.commands import *
from luamoon.colors import Color, colorize_text, rich_print


NOT_IMPLEMENTED_MSG = colorize_text(Color.INFO, "Sorry, this feature isn’t available yet :)")

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
            rich_print(NOT_IMPLEMENTED_MSG)

    elif args.command == 'add':
        add_package(args.package_name)
    elif args.command == 'update':
        update_package(args.package_name)
    elif args.command == 'remove':
        remove_package(args.package_name)
    elif args.command == 'list':
        list_packages()
    elif args.command == 'search':
        rich_print(NOT_IMPLEMENTED_MSG)
    elif args.command == 'publish':
        rich_print(NOT_IMPLEMENTED_MSG)
    elif args.command == 'config':
        rich_print(NOT_IMPLEMENTED_MSG)
    elif args.command == 'run':
        change_paths()
        run_project('project', 'src/main.lua')  # strings to be replaced

if __name__ == '__main__':
    main()
