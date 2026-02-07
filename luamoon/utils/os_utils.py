import platform
import pefile

def detect_platform() -> str:
    if platform.system() == 'Darwin':
        return "MacOS"
    elif platform.system() == 'Windows':
        return "Windows"
    elif platform.system() == 'Linux':
        return "Linux"
    else:
        return "Unknown"
        # todo: add proper cli error

def get_exe_version(exe_path) -> str | None:
    pe = pefile.PE(exe_path)
    return pe.FileInfo[0][0].StringTable[0].entries[b'FileVersion'].decode()
