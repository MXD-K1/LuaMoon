from luamoon.core import *

from luamoon.core.downloader import download_pkg
from luamoon.lockfile.main import *


def change_venv_name(new_venv_name):
    global venv_name
    venv_name = new_venv_name

def init_project():
    try:
        os.mkdir(venv_path)
        os.mkdir(packages_path)
    except FileExistsError:
        pass  # Todo: Add appropriate error message in the cli

    # todo: Ship the binary in the venv dir
    # todo: Ship the lua binary in the venv dir

def add_package(package_name):
    with open(index_file_path, 'r') as index_file:
        data = json.load(index_file)
    try:
        pkg_data = data[package_name]
        pkg_data = pkg_data[0]  # todo: resolve the appropriate version
    except KeyError:
        pass  # Todo: Add appropriate error message in the cli

    # todo: check lua versions and library versions

    download_pkg(pkg_data['source'], os.path.normpath(packages_path + '\\' + package_name + '.zip'))
    # todo: check if the pkg is downloaded successfully
    # todo: extract it properly

    add_package_data(package_name, pkg_data)

def remove_package(package_name):
    pass

def list_packages():
    pass
