import os

PATH = os.environ.copy()
HOMEPATH = os.path.expanduser("~")

# noinspection SpellCheckingInspection
CACHE_DIR = os.path.join(HOMEPATH, '.luamoon')
CONFIG_FILE_PATH = os.path.join(CACHE_DIR, 'config.toml')  # global config
