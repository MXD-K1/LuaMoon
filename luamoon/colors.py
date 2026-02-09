from enum import Enum

from rich import print as rich_print


class Color(Enum):
    SUCCESS = "#00FF00"  # green
    INFO = "#00BFFF"  # cyan
    PROGRESS = "#0000FF"  # blue, for progress bars only
    WARNING = "#FFFF00"  # yellow
    CRITICAL = "#FFA500"  # orange
    ERROR = "#FF0000"  # red
    DEPRECATION = "#FF00FF"  # magenta
    DEBUG = "#CD853F"  # brown

    # these colors might change in the future


def colorize_text(color, text):
    return f"[{color.value}]{text}[/{color.value}]"

__all__ = ["colorize_text", "Color", "rich_print"]
