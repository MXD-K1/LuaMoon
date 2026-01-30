import os

from luamoon.core import *

def get_lua_version():
    return lua_version

def change_venv_name(new_venv_name):
    global venv_name, venv_path, packages_path, lockfile_path
    venv_name = new_venv_name
    venv_path = os.path.join(path, venv_name)
    packages_path = os.path.normpath(path + '\\' + venv_name + '\\' + 'packages')
    lockfile_path = os.path.normpath(path + '\\' + venv_name + '\\' + 'luamoon.lock')

def change_lua_version(new_lua_version):
    global lua_version
    lua_version = new_lua_version