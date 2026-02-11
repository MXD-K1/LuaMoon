import os
import shutil

from luamoon.core import *
from luamoon.core.main import get_lua_version
from luamoon.resources.lockfile import update_lockfile_headers, create_lockfile
from luamoon.resources.toml import create_project_toml, create_lib_toml, update_project_headers, update_lib_headers
from luamoon.binaries import *
from luamoon import PATH
from luamoon.core import package_path, include_path, bin_path, project_name

def change_paths():
    PATH['PATH'] = f'{bin_path};' + PATH['PATH']
    PATH['LUA_PATH'] = os.path.join(f'{package_path}', '?.lua')  # lua path
    PATH['LUA_CPATH'] = f'{include_path}'
    # do not concatenate with the existing path

def init(purpose, runtime_type):
    if purpose == 'project':
        init_project(runtime_type)
    elif purpose == 'lib':
        init_lib(runtime_type)

def ignore(_, files):
    """Temp Function."""
    return [f for f in files for ext in [".ico", ".txt", ".md", ".png"] if f.endswith(ext)]

def add_binaries(runtime_type):
    if runtime_type == 'lua':
        lua_path = detect_lua()[0]
        shutil.copy2(lua_path, os.path.join(path, venv_name, 'bin'))
    elif runtime_type == 'love':
        love_path = detect_love2d()[0].split(os.path.sep)[:-1]
        love_path = f'{os.path.sep}'.join(love_path)
        try:
            shutil.copytree(love_path, os.path.join(path, venv_name, 'bin'), dirs_exist_ok=True, ignore=ignore)
        except Exception as e:
            print(e)
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

        with open(os.path.join(path, 'README.md'), 'w') as f:
            f.write(f'# {project_name.capitalize()}\n')
        with open(os.path.join(path, 'src', 'main.lua'), 'w') as f:
            f.write('print("Hello World")')

        update_project_headers({"project": {"name": project_name}})
        create_project_toml()

        headers_ = update_lockfile_headers(get_lua_version())
        create_lockfile(headers_)

    except FileExistsError:
        pass  # todo: Add appropriate error message in the cli
        # todo: ask for overriding

    # todo: support existing projects

    change_paths()

    # todo: Ship the binary in the venv dir
    # todo: Ship the lua binary in the venv dir

def init_lib(runtime_type):
    # create dirs and files
    try:
        os.mkdir(venv_path)
        os.mkdir(os.path.join(path, 'src'))
        os.mkdir(os.path.join(path, venv_name, 'bin'))
        os.mkdir(package_path)
        os.mkdir(os.path.join(path, venv_name, 'include'))

        add_binaries(runtime_type)

        with open(os.path.join(path, 'README.md'), 'w') as f:
            f.write(f'# {project_name.capitalize()}\n')
        with open(os.path.join(path, 'src', 'main.lua'), 'w') as f:
            f.write('print("Hello World")')

        update_project_headers({"package": {"name": project_name}})
        create_lib_toml()

        headers_ = update_lockfile_headers(get_lua_version())
        create_lockfile(headers_)

    except FileExistsError:
        pass  # todo: Add appropriate error message in the cli
        # todo: ask for overriding

    # todo: support existing projects

    change_paths()

    # todo: Ship the binary in the venv dir
    # todo: Ship the lua binary in the venv dir
