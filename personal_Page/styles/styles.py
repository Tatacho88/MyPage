import reflex as rx
from enum import Enum
from .fonts import Font
from .colors import Color, TextColor

STYLESHEETS = [
    "https://unpkg.com/nes.css/css/nes.css",
    "https://fonts.googleapis.com/css?family=Press+Start+2P&display=swap"
]
BASE_STYLE = {
    "font_family": Font.DEFAUT.value,
    "color": TextColor.PRIMARY.value,
    "background": Color.PRIMARY.value
}

class Size(Enum):
    SMALL="0.25em"
    DEFAULT="1em"
    BIG="2em"
    VERY_BIG="4em"
    