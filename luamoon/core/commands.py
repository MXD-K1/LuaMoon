import os

from luamoon.core import *
from luamoon.core.main import get_lua_version
from luamoon.resources.lockfile import *

def init_project():
    # create dirs and files
    try:
        os.mkdir(venv_path)
        os.mkdir(os.path.join(path, 'src'))
        os.mkdir(os.path.join(path, venv_name, 'bin'))
        os.mkdir(os.path.join(path, venv_name, 'packages'))
        os.mkdir(os.path.join(path, venv_name, 'include'))

        with open(os.path.join(path, 'README.md'), 'w'): pass


    except FileExistsError:
        pass  # todo: Add appropriate error message in the cli
        # todo: ask for overriding

    # todo: support existing projects

    # todo: Ship the binary in the venv dir
    # todo: Ship the lua binary in the venv dir

    headers_ = create_lockfile_headers(get_lua_version())
    create_lockfile(headers_)

def init_lib():
    pass

def add_package(package_name):
    with open(index_file_path, 'r') as index_file:
        data = json.load(index_file)
    try:
        pkg_data = data[package_name]
        pkg_data = pkg_data[0]  # todo: resolve the appropriate version
    except KeyError:
        return  # todo: Add appropriate error message in the cli

    # todo: check lua versions and library versions

    # download_pkg(pkg_data['source'], os.path.normpath(packages_path + '\\' + package_name + '.zip'))
    # todo: check if the pkg is downloaded successfully
    # todo: extract it properly

    add_package_data(package_name, pkg_data)

def remove_package(package_name):
    pass

def list_packages():
    pass
