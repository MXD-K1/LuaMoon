import os
import subprocess

from luamoon.utils.os_utils import detect_platform, get_exe_version
from luamoon import PATH

def run_command(cmd) -> str | None:
    try:
        process = subprocess.run(cmd, shell=True, text=True, capture_output=True, check=True)
        return process.stdout.strip() or process.stderr.strip() or None
    except subprocess.CalledProcessError as e:
        if e.stdout.strip() or e.stderr.strip():
            return e.stdout.strip() or e.stderr.strip() or None
        raise e
    # Note: If PATH was edited at the system/user level on Windows, the current Python process may not see the change.
    # Restarting the IDE/terminal may not be enough; a full system restart ensures the new PATH is applied everywhere.

def get_which_cmd() -> str:
    if detect_platform() == "MacOS" or detect_platform() == "Linux":
        return "which"
    elif detect_platform() == "Windows":
        return "where"
    else:
        # todo: raise an error or support other systems
        raise NotImplementedError

def detect_lua() -> tuple[str, str] | None:
    try:
        lua_path = run_command(f'{get_which_cmd()} lua')
    except subprocess.CalledProcessError:
        return None  # Lua bin was not detected

    if lua_path:
        try:
            lua_version = run_command(f'lua -v')
            lua_version = lua_version.split()[1]
        except subprocess.CalledProcessError:
            # todo: report error or simply ignore
            return None
        return lua_path, lua_version
    return None

def detect_luajit() -> tuple[str, str] | None:
    try:
        luajit_path = run_command(f'{get_which_cmd()} luajit')
    except subprocess.CalledProcessError:
        return None  # Luajit bin was not detected

    if luajit_path:
        try:
            luajit_version = run_command(f'luajit -v')
            luajit_version = luajit_version.split()[1]
        except subprocess.CalledProcessError:
            # todo: report error or simply ignore
            return None
        return luajit_path, luajit_version
    return None

def detect_luarocks() -> tuple[str, str] | None:
    try:
        luarocks_path = run_command(f'{get_which_cmd()} luarocks').split('\n')[0]
    except subprocess.CalledProcessError:
        return None  # Lua bin was not detected

    if luarocks_path:
        try:
            luarocks_version = run_command(f'luarocks --version')
            luarocks_version = luarocks_version.split()[1]
        except subprocess.CalledProcessError:
            # todo: report error or simply ignore
            return None
        return luarocks_path, luarocks_version
    return None

def detect_love2d() -> tuple[str, str] | None:
    love_path = run_command(f'{get_which_cmd()} love')
    if love_path:
        if os.path.exists(love_path):
            love_version = get_exe_version(f'"{love_path}"')
            love_version = love_version.split()[0]
            return love_path, love_version
        return search_love2d()
    else:
        # Love2D bin was not detected, try to search for possible locations
        return search_love2d()

def search_love2d() -> tuple[str, str] | None:
    """Note: it only works on windows (Linux and macOS to be supported later)"""
    if detect_platform() == "Windows":
        dirs = [
            os.path.join(PATH.get("SYSTEMDRIVE"), "\\", "Program Files", "LOVE", "love.exe"),
            os.path.join(PATH.get("SYSTEMDRIVE"), "\\", "Program Files (x86)", "LOVE", "love.exe"),
            os.path.join(PATH.get("LOCALAPPDATA"), "LOVE", "love.exe"),
            os.path.join(PATH.get("SYSTEMDRIVE"), "\\", "LOVE", "love.exe")
        ]

        love_path = None
        for dir_ in dirs:
            if os.path.exists(dir_):
                love_path = dir_

        if love_path:
            love_version = get_exe_version(f'{love_path}')
            love_version = love_version.split()[0]
            return love_path, love_version
        return None

    elif detect_platform() == "Linux":
        dirs = [
            os.path.join("/usr/bin", "love"),
            os.path.join("/usr/local/bin", "love"),
            os.path.join("/snap/bin", "love"),
            os.path.join(PATH.get("HOME"), ".local", "bin", "love")
        ]

        pass

    elif detect_platform() == "MacOS":
        dirs = [
            "/Applications/LOVE.app/Contents/MacOS/love",  # standard install
            os.path.join(os.environ.get("HOME", ""), "Applications", "LOVE.app", "Contents", "MacOS", "love"),  # user install
            os.path.join("/usr/local/bin", "love"),  # Homebrew install
            os.path.join("/opt/homebrew/bin", "love"),  # Homebrew on Apple Silicon
            os.path.join("/usr/bin", "love"),  # system bin
            os.path.join("/snap/bin", "love")  # if installed via snap
        ]

        pass

    else:
        return None
