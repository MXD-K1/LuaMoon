from enum import Enum


class Color(Enum):
    GREEN = "#00FF00"  # success
    CYAN = "#00BFFF"  # info
    YELLOW = "#FFFF00"  # warning
    RED = "#FF0000"  # error/failure
    MAGENTA = "#FF00FF"  # debugging

def color_text(color, text):
    return f"[{color.value}]{text}[/{color.value}]"
