from enum import Enum


class Color(Enum):
    CYAN = "#00BFFF"

def color_text(color, text):
    return f"[{color.value}]{text}[/{color.value}]"
