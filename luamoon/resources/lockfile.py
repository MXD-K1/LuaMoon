import toml
from typing import Any

from luamoon.resources import *

headers: dict[str, Any] | None = {
        'version': '1.0.0',
        'lua-version': '',
        'packages': {}
    }

def create_lockfile(headers_):
    global headers
    headers = headers_
    with open(lockfile_path, 'w') as lockfile:
        toml.dump(headers_, lockfile)

def create_lockfile_headers(lua_version):
    global headers
    headers = {
        'version': '1.0.0',
        'lua-version': lua_version,
        'packages': {}
    }


def add_package_data(pkg_name, pkg_data):
    headers['packages'][pkg_name] = pkg_data
    with open(lockfile_path, 'w') as f:
        toml.dump(headers, f)

def remove_package_data(pkg_name):
    try:
        del headers['packages'][pkg_name]
    except KeyError:
        return  # todo: raise an error in the cli

    with open(lockfile_path, 'w') as f:
        toml.dump(headers, f)

def update_package_data():
    pass
