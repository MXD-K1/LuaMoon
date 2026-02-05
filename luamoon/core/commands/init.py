import os

from luamoon.core import *
from luamoon.core.main import get_lua_version
from luamoon.resources.lockfile import create_lockfile_headers, create_lockfile
from luamoon.resources.toml import create_project_toml, create_lib_toml


def init_project():
    # create dirs and files
    try:
        os.mkdir(venv_path)
        os.mkdir(os.path.join(path, 'src'))
        os.mkdir(os.path.join(path, venv_name, 'bin'))
        os.mkdir(os.path.join(path, venv_name, 'packages'))
        os.mkdir(os.path.join(path, venv_name, 'include'))

        with open(os.path.join(path, 'README.md'), 'w'): pass
        with open(os.path.join(path, 'src', 'main.lua'), 'w') as f:
            f.write('print("Hello World")')

        create_project_toml()

    except FileExistsError:
        pass  # todo: Add appropriate error message in the cli
        # todo: ask for overriding

    # todo: support existing projects

    # todo: Ship the binary in the venv dir
    # todo: Ship the lua binary in the venv dir

    headers_ = create_lockfile_headers(get_lua_version())
    create_lockfile(headers_)

def init_lib():
    # create dirs and files
    try:
        os.mkdir(venv_path)
        os.mkdir(os.path.join(path, 'src'))
        os.mkdir(os.path.join(path, venv_name, 'bin'))
        os.mkdir(os.path.join(path, venv_name, 'packages'))
        os.mkdir(os.path.join(path, venv_name, 'include'))

        with open(os.path.join(path, 'README.md'), 'w'): pass
        with open(os.path.join(path, 'src', 'main.lua'), 'w') as f:
            f.write('print("Hello World")')

        create_lib_toml()

    except FileExistsError:
        pass  # todo: Add appropriate error message in the cli
        # todo: ask for overriding

    # todo: support existing projects

    # todo: Ship the binary in the venv dir
    # todo: Ship the lua binary in the venv dir

    headers_ = create_lockfile_headers(get_lua_version())
    create_lockfile(headers_)
