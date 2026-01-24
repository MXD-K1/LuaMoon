import os

path = os.getcwd()
venv_name = '.vmoon'
venv_path = os.path.join(path, venv_name)
packages_path = os.path.normpath(path + '\\' + venv_name + '\\' + 'packages')
lockfile_path = os.path.normpath(path + '\\' + venv_name + '\\' + 'luamoon.lock')
index_file_path = os.path.normpath('../../index.jsonc')
lua_version = '5.4'  # default version
