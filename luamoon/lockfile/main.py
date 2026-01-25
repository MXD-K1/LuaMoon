import json
from typing import Any

from luamoon.lockfile import *

headers: dict[str, Any] | None = None

def create_lockfile(headers_):
    global headers
    headers = headers_
    with open(lockfile_path, 'w') as lockfile:
        json.dump(headers_, lockfile, indent=4)

def create_lockfile_headers(lua_version):
    return {
        'version': '1.0.0',
        'lua-version': lua_version,
        'packages': {}
    }


def add_package_data(pkg_name, pkg_data):
    headers['packages'][pkg_name] = pkg_data
    with open(lockfile_path, 'w') as f:
        json.dump(headers, f, indent=4)

def remove_package_data(pkg_name):
    try:
        del headers['packages'][pkg_name]
    except KeyError:
        return  # todo: raise an error in the cli

    with open(lockfile_path, 'w') as f:
        json.dump(headers, f, indent=4)
