import os

PATH = os.environ.copy()

# noinspection SpellCheckingInspection
CACHE_DIR = os.path.join(PATH['HOMEDRIVE'], PATH['HOMEPATH'], '.luamoon')
CONFIG_FILE_PATH = os.path.join(CACHE_DIR, 'config.toml')  # global config
