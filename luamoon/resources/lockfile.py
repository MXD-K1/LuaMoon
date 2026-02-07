import toml
from typing import Any

from luamoon.resources import *

headers = {
        'version': '1.0.0',
        'lua-version': '5.1',
        'packages': {}
    }

def create_lockfile(headers_):
    global headers
    headers = headers_
    with open(lockfile_path, 'w') as lockfile:
        toml.dump(headers_, lockfile)

def update_lockfile_headers(lua_version):
    global headers
    headers['lua-version'] = lua_version
    # todo: add a new_headers param
    return headers


def add_package_data(pkg_name, pkg_data):
    pkg = {pkg_name: pkg_data}
    headers['packages'].append(pkg)
    with open(lockfile_path, 'w') as f:
        toml.dump(headers, f)

def remove_package_data(pkg_name):
    try:
        for pkg in headers['packages']:
            if pkg['name'] == pkg_name:
                headers['packages'].remove(pkg)
    except ValueError:
        return  # todo: raise an error in the cli

    with open(lockfile_path, 'w') as f:
        toml.dump(headers, f)

def update_package_data():
    pass
