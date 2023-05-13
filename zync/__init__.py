from .logging import logger, bugger
from .slugify import Slugger, slugger

methods = ["logger", "bugger", "Slugger", "slugger"]

__all__ = methods


__version__ = "0.1.0"
__author__ = "TJ Bredemeyer"
