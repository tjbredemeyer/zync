"""This initializes the methods in zync."""

from .logger import logger, bugger, wegger
from .slugify import Slugger, slugger

__all__ = [
    "bugger",
    "logger",
    "wegger",
    "Slugger",
    "slugger",
]
