import os

path = os.getcwd()
project_name = path.split(os.path.sep)[-1]  # auto-detected
venv_name = '.luamoon'
venv_path = os.path.join(path, venv_name)
index_file_path = os.path.normpath('../../index.json')
lockfile_path = os.path.normpath(path + '\\' + 'luamoon.lock')
package_path = os.path.join(venv_path, 'packages')
include_path = os.path.join(venv_path, 'include')
bin_path = os.path.join(venv_path, 'bin')
lua_version = '5.4'  # default version

__all__ = ['lua_version', 'lockfile_path', 'index_file_path', 'venv_name', 'venv_path', 'path', 'package_path',
           'include_path', 'bin_path', 'project_name']
