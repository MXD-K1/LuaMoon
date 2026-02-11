import os
import json
import shutil
import tempfile

from luamoon.fetch.extract import extract_zip
from luamoon.fetch.download import download_pkg
from luamoon.core import index_file_path, package_path
from luamoon.resources.lockfile import add_package_data
from luamoon.resources.global_config import add_pkg_to_cache

def add_package(pkg_name: str, pkg_version=None):
    with open(index_file_path, 'r') as index_file:
        data = json.load(index_file)
    try:
        pkg_data = data[pkg_name]  # todo: resolve the appropriate version
    except KeyError:
        return  # todo: Add appropriate error message in the cli

    # todo: check lua versions and library versions

    with tempfile.TemporaryDirectory() as path:
        success = download_pkg(pkg_data['source'], pkg_name, pkg_version or pkg_data['version'], path)
        if success:
            extract_zip(os.path.join(path, pkg_name), path)

        for _, folders, _ in os.walk(path):
            folder = folders[0]
            os.rename(os.path.join(path, folder), os.path.join(path, pkg_name))

        shutil.move(os.path.join(path, pkg_name), package_path)
        add_pkg_to_cache(os.path.join(path, pkg_name), pkg_name, pkg_version or pkg_data['version'])
        # todo: check if the pkg is downloaded successfully
        # todo: extract it properly

    add_package_data(pkg_name, pkg_data)
