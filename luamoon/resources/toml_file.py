import os

import toml

from luamoon.core import path
from luamoon.utils.dict_utils import *

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
    "package": {
        "name": "mylib",
        "version": "0.1.0",
        "description": "",
        "author": "",
        "license": ""
    },
    "environment": {
        "type": "",
        "src_dir": "",
        "lua_version": "5.1",
    },
    "dependencies": {}
}

# todo: fill the missing fields

def update_project_headers(new_headers):
    deep_update(project_headers, new_headers)

def update_lib_headers(new_headers):
    deep_update(lib_headers, new_headers)

def create_project_toml():
    with open(os.path.join(path, 'luaproject.toml'), 'w') as toml_file:
        toml_file.write(toml.dumps(project_headers))

def create_lib_toml():
    with open(os.path.join(path, 'lualib.toml'), 'w') as toml_file:
        toml_file.write(toml.dumps(lib_headers))

def read_toml(project_dir):
    if os.path.exists(os.path.join(project_dir, 'luaproject.toml')):
        name = 'luaproject.toml'
    elif os.path.exists(os.path.join(project_dir, 'lualib.toml')):
        name = 'lualib.toml'
    else:
        raise FileNotFoundError('luaproject.toml\\lualib.toml not found')  # todo: replace this

    with open(name, 'r') as f:
        return toml.load(f)
