import platform

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
