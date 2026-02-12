from luamoon.resources.toml import read_toml
from luamoon.core import path

def list_packages():
    data = read_toml(path)
    for entry in data['dependencies'].items():
        print(f"{entry[0]}=={entry[1]}")
