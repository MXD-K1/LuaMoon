import os

import toml

from luamoon.core import path

project_headers = {
    "project": {
        "name": "myproject",
        "version": "0.1.0",
        "description": "",
        "author": "",
        "license": "",
    },
    "environment": {
        "type": "",
        "lua_version": "5.1",
        "entry_point": ""
    },
    "dependencies": {}
}

lib_headers = {
    "project": {
        "name": "myproject",
        "version": "0.1.0",
        "description": "",
        "author": "",
        "license": ""
    },
    "environment": {
        "type": "",
        "lua_version": "5.1",
    },
    "dependencies": {}
}

# todo: fill the missing fields

def create_project_toml():
    with open(os.path.join(path, 'luaproject.toml'), 'w') as toml_file:
        toml_file.write(toml.dumps(project_headers))

def create_lib_toml():
    with open(os.path.join(path, 'lualib.toml'), 'w') as toml_file:
        toml_file.write(toml.dumps(lib_headers))
