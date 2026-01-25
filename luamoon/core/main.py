from luamoon.core import *

from luamoon.core.downloader import download_pkg
from luamoon.lockfile.main import *

def get_lua_version():
    return lua_version

def change_venv_name(new_venv_name):
    global venv_name, venv_path, packages_path, lockfile_path
    venv_name = new_venv_name
    venv_path = os.path.join(path, venv_name)
    packages_path = os.path.normpath(path + '\\' + venv_name + '\\' + 'packages')
    lockfile_path = os.path.normpath(path + '\\' + venv_name + '\\' + 'luamoon.lock')

def change_lua_version(new_lua_version):
    global lua_version
    lua_version = new_lua_version

def init_project():
    try:
        os.mkdir(venv_path)
        os.mkdir(packages_path)
    except FileExistsError:
        pass  # todo: Add appropriate error message in the cli
        # todo: ask for overriding

    # todo: Ship the binary in the venv dir
    # todo: Ship the lua binary in the venv dir

    headers = create_lockfile_headers(get_lua_version())
    create_lockfile(headers)

def add_package(package_name):
    with open(index_file_path, 'r') as index_file:
        data = json.load(index_file)
    try:
        pkg_data = data[package_name]
        pkg_data = pkg_data[0]  # todo: resolve the appropriate version
    except KeyError:
        return  # Todo: Add appropriate error message in the cli

    # todo: check lua versions and library versions

    download_pkg(pkg_data['source'], os.path.normpath(packages_path + '\\' + package_name + '.zip'))
    # todo: check if the pkg is downloaded successfully
    # todo: extract it properly

    add_package_data(package_name, pkg_data)

def remove_package(package_name):
    pass

def list_packages():
    pass
