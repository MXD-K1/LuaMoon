import os
import json

from luamoon.core import index_file_path, package_path
from luamoon.resources.lockfile import add_package_data, remove_package_data

def add_package(package_name):
    with open(index_file_path, 'r') as index_file:
        data = json.load(index_file)
    try:
        pkg_data = data[package_name]  # todo: resolve the appropriate version
    except KeyError:
        return  # todo: Add appropriate error message in the cli

    # todo: check lua versions and library versions

    # download_pkg(pkg_data['source'], os.path.normpath(packages_path + '\\' + package_name + '.zip'))
    # todo: check if the pkg is downloaded successfully
    # todo: extract it properly

    add_package_data(package_name, pkg_data)

def remove_package(package_name):
    remove_package_data(package_name)
    try:
        os.remove(os.path.join(package_path, package_name))
    except FileNotFoundError:
        return  # todo: Add proper cli error message

def update_package(package_name):
    pass

def search_package(package_name):
    pass

def list_packages():
    pass
