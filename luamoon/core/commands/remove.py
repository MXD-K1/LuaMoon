import os

from luamoon.core import package_path
from luamoon.resources.lockfile import remove_package_data

def remove_package(package_name):
    remove_package_data(package_name)
    try:
        os.remove(os.path.join(package_path, package_name))
    except FileNotFoundError:
        return  # todo: Add proper cli error message
