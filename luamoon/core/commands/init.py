import os
import shutil

from luamoon.core import *
from luamoon.core.main import get_lua_version
from luamoon.resources.lockfile import update_lockfile_headers, create_lockfile
from luamoon.resources.toml import create_project_toml, create_lib_toml
from luamoon.binaries import *

def init(purpose, runtime_type):
    if purpose == 'project':
        init_project(runtime_type)
    elif purpose == 'lib':
        init_lib(runtime_type)


def add_binaries(runtime_type):
    if runtime_type == 'lua':
        lua_path = detect_lua()[0]
        shutil.copy2(lua_path, os.path.join(path, venv_name, 'bin'))
    elif runtime_type == 'love':
        love_path = detect_love2d()[0]
        shutil.copy2(love_path, os.path.join(path, venv_name, 'bin'))
    # todo:decide when to add luarocks


def init_project(runtime_type):
    # create dirs and files
    try:
        os.mkdir(venv_path)
        os.mkdir(os.path.join(path, 'src'))
        os.mkdir(os.path.join(path, venv_name, 'bin'))
        os.mkdir(package_path)
        os.mkdir(os.path.join(path, venv_name, 'include'))

        add_binaries(runtime_type)

        with open(os.path.join(path, 'README.md'), 'w'): pass
        with open(os.path.join(path, 'src', 'main.lua'), 'w') as f:
            f.write('print("Hello World")')

        create_project_toml()

        headers_ = update_lockfile_headers(get_lua_version())
        create_lockfile(headers_)

    except FileExistsError:
        pass  # todo: Add appropriate error message in the cli
        # todo: ask for overriding

    # todo: support existing projects

    # todo: Ship the binary in the venv dir
    # todo: Ship the lua binary in the venv dir

def init_lib(runtime_type):
    # create dirs and files
    try:
        os.mkdir(venv_path)
        os.mkdir(os.path.join(path, 'src'))
        os.mkdir(os.path.join(path, venv_name, 'bin'))
        os.mkdir(os.path.join(path, venv_name, 'packages'))
        os.mkdir(os.path.join(path, venv_name, 'include'))

        add_binaries(runtime_type)

        with open(os.path.join(path, 'README.md'), 'w'): pass
        with open(os.path.join(path, 'src', 'main.lua'), 'w') as f:
            f.write('print("Hello World")')

        create_lib_toml()
        headers_ = update_lockfile_headers(get_lua_version())
        create_lockfile(headers_)

    except FileExistsError:
        pass  # todo: Add appropriate error message in the cli
        # todo: ask for overriding

    # todo: support existing projects

    # todo: Ship the binary in the venv dir
    # todo: Ship the lua binary in the venv dir
