import json

from luamoon.lockfile import *
from luamoon.core import lua_version

headers = {
    'version': '1.0.0',
    'lua-version': lua_version,
    'packages': {}
}

def add_package_data(pkg_name, pkg_data):
    headers['packages'][pkg_name] = pkg_data
    with open(lockfile_path, 'w') as f:
        json.dump(headers, f, indent=4)

def remove_package_data(pkg_name):
    global headers
    try:
        del headers['packages'][pkg_name]
    except KeyError:
        return  # todo: raise an error in the cli

    with open(lockfile_path, 'w') as f:
        json.dump(headers, f, indent=4)
