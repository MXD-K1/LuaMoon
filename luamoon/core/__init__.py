import os

path = os.getcwd()
venv_name = '.luamoon'
venv_path = os.path.join(path, venv_name)
index_file_path = os.path.normpath('../../index.json')
lockfile_path = os.path.normpath(path + '\\' + 'luamoon.lock')
lua_version = '5.4'  # default version

__all__ = ['lua_version', 'lockfile_path', 'index_file_path', 'venv_name', 'venv_path', 'path']
