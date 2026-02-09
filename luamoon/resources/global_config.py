import os
import shutil

import toml

from luamoon import CACHE_DIR, CONFIG_FILE_PATH

headers = {
        'paths': {
            'lua': '',
            'love2d': '',
            'luarocks': ''
        },
        'config': {}
    }

def init_cache_dir(headers_=None):
    global headers
    if headers_ is None:
        headers_ = headers
    if not os.path.exists(CACHE_DIR):
        os.mkdir(CACHE_DIR)
        os.mkdir(os.path.join(CACHE_DIR, 'packages'))
        with open(CONFIG_FILE_PATH, 'w') as f:
            toml.dump(headers_, f)
    else:
        with open(CONFIG_FILE_PATH, 'r') as f:
            headers_ = toml.load(f)
            update_headers(headers_)

def update_headers(headers_):
    global headers
    headers |= headers_

def add_pkg_to_cache(pkg_dir, pkg_name, pkg_version):
    shutil.copytree(pkg_dir, os.path.join(CACHE_DIR, 'packages', f'{pkg_name}-{pkg_version}'))
