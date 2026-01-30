import os

import toml

from luamoon.core import path

project_headers = {
    "project": {
        "name": "myproject",
        "version": "0.1.0",
        "lua_version": "5.1"
    },
    "dependencies": {}
}

def create_project_toml():
    with open(os.path.join(path, 'luaproject.toml'), 'w') as toml_file:
        toml_file.write(toml.dumps(project_headers))
