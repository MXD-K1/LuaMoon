import os

import requests

RETRIES = 4
TIMEOUT = 15

def get_url_content(url: str, timeout=TIMEOUT, retries=RETRIES):
    response = requests.get(url, timeout=timeout)
    for _ in range(retries):
        if response.status_code == 200:
            return response.content
    else:
        raise Exception(f"Could not fetch url '{url}'")
        # todo: Add appropriate error message in the cli

# noinspection PyTypeChecker
def download_pkg(url: str, pkg_name: str, pkg_version: str, path: str) -> str:
    response_bytes = get_url_content(url.format(version=pkg_version))
    full_path = os.path.join(path, pkg_name + '.zip')

    with open(full_path, "wb") as zip_f:
        zip_f.write(response_bytes)
