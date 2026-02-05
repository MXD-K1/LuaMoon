import os

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

def init_cache_dir(headers_=None) -> dict:
    global headers
    if headers_ is None:
        headers_ = headers
    if not os.path.exists(CACHE_DIR):
        os.mkdir(CACHE_DIR)
        os.mkdir(os.path.join(CACHE_DIR, 'packages'))
        with open(CONFIG_FILE_PATH, 'w') as f:
            toml.dump(headers_, f)
        return headers_
    else:
        with open(CONFIG_FILE_PATH, 'r') as f:
            headers_ = toml.load(f)
        return headers_
