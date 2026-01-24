import os
import json

from downloader import download_pkg

path = os.getcwd()
venv_name = '.vmoon'
venv_path = os.path.join(path, venv_name)
packages_path = os.path.normpath(path + '\\' + venv_name + '\\' + 'packages')
lockfile_path = os.path.normpath(path + '\\' + venv_name + '\\' + 'luamoon.lock')
index_file_path = os.path.normpath('../../index.jsonc')

headers = {
    'version': '1.0.0',
    'lua-version': None,  # todo: get the lua version
    'packages': []
}

def change_venv_name(new_venv_name):
    global venv_name
    venv_name = new_venv_name

def init_project():
    try:
        os.mkdir(venv_path)
        os.mkdir(packages_path)
    except FileExistsError:
        pass  # Todo: Add appropriate error message in the cli

    with open(lockfile_path, 'w') as lockfile:
        json.dump(headers, lockfile, indent=4)

    # Todo: Ship the binary in the venv dir

def add_package(package_name):
    with open(index_file_path, 'r') as index_file:
        data = json.load(index_file)
    try:
        pkg_data = data[package_name]
    except KeyError:
        pass  # Todo: Add appropriate error message in the cli

    # todo: check lua versions and library versions

    download_pkg(pkg_data['url'], os.path.normpath(packages_path + '\\' + package_name))
    # todo: check if the pkg is downloaded successfully
    # todo: extract it properly





def remove_package(package_name):
    pass

def list_packages():
    pass
