import os
from time import sleep

import requests

from luamoon.colors import colorize_text, Color, rich_print

RETRIES = 4
TIMEOUT = 15

def get_url_content(url: str, timeout=TIMEOUT, retries=RETRIES):

    for i in range(retries, -1, -1):
        try:
            response = requests.get(url, timeout=timeout)
        except requests.exceptions.ConnectionError:
            sleep(timeout // 5)
            if retries > 0:
                rich_print(colorize_text(Color.WARNING, f"Retrying ({i} remaining)"))
                continue
        else:
            if response.status_code == 200:
                return response.content
    else:
        rich_print(colorize_text(Color.ERROR, f"Could not fetch url '{url}'"))
        return None
        # todo: Add appropriate error message in the cli


# noinspection PyTypeChecker
def download_pkg(url: str, pkg_name: str, pkg_version: str, path: str) -> str:
    response_bytes = get_url_content(url.format(version=pkg_version))
    full_path = os.path.join(path, pkg_name + '.zip')

    with open(full_path, "wb") as zip_f:
        zip_f.write(response_bytes)
