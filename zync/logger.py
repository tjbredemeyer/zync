"""
This is the logger module for the zync package.

The objective is to simplify the logging process while distibuting only
the logging information that is needed for development and debugging.

Options for logger are
###### 1. bugger - DEBUG message
###### 2. logger - INFO message
###### 3. egger - ERROR message

The output includes the message level, date, and relative path.
"""
import logging
import inspect
import os


W = "\033[39m"
B = "\033[94m"
G = "\033[92m"
Y = "\033[33m"
R = "\033[91m"
M = "\033[35m"
C = "\033[36m"
L = "\033[2m"
X = "\033[0m"


class BuggerFormat(logging.Formatter):
    """Formatting bugger output"""

    def format(self, record):
        """Formatting bugger output"""
        record.levelname = "bugger"
        levelname = record.levelname.upper()
        record.levelname = levelname
        return super().format(record)


class LoggerFormat(logging.Formatter):
    """Formatting logger output"""

    def format(self, record):
        """Formatting logger output"""
        record.levelname = "logger"
        levelname = record.levelname.upper()
        record.levelname = levelname
        return super().format(record)


class EggerFormat(logging.Formatter):
    """Formatting egger output"""

    def format(self, record):
        """Formatting egger output"""
        record.levelname = "egger"
        levelname = record.levelname.upper()
        record.levelname = levelname
        return super().format(record)


class Bugger:
    """the bugger log class"""

    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler(".zync.log")
        formatter = BuggerFormat(
            f"{G}[{X}"
            f"{G}%(levelname)s:{X}"
            f"{G}{L}%(asctime)s{X}"
            f"{G}]{X}"
            f"{M}%(location)s{X}"
            f"{G}> {X}"
            f"%(message)s{X}",
            datefmt="%H:%M:%S",
        )
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def __call__(self, log, line, location):
        self.logger.debug(log, extra={"line": line, "location": location})


class Logger:
    """the logger log class"""

    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        file_handler = logging.FileHandler(".zync.log")
        formatter = LoggerFormat(
            f"{Y}[{X}"
            f"{Y}%(levelname)s:{X}"
            f"{Y}{L}%(asctime)s{X}"
            f"{Y}]{X}"
            f"{M}%(location)s{X}"
            f"{Y}> {X}"
            f"%(message)s{X}",
            datefmt="%H:%M:%S",
        )
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def __call__(self, log, line, location):
        self.logger.info(log, extra={"line": line, "location": location})


class Egger:
    """the egger log class"""

    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.ERROR)
        file_handler = logging.FileHandler(".zync.log")
        formatter = EggerFormat(
            f"{R}[{X}"
            f"{R}%(levelname)s:{X}"
            f"{R}{L}%(asctime)s{X}"
            f"{R}]{X}"
            f"{M}%(location)s{X}"
            f"{R}> {X}"
            f"%(message)s{X}",
            datefmt="%H:%M:%S",
        )
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def __call__(self, log, line, location):
        self.logger.error(log, extra={"line": line, "location": location})


bugger_base = Bugger("bugger")
logger_base = Logger("logger")
egger_base = Egger("egger")


def get_relative_path(frame):
    """getting the relative path for logging position"""
    filename = inspect.getframeinfo(frame).filename
    current_dir = os.path.dirname(os.path.abspath(__file__))
    relative_path = os.path.relpath(filename, current_dir)
    return relative_path


def bugger(log):
    """the bugger method"""
    frame = inspect.currentframe().f_back
    path = get_relative_path(frame)
    line = inspect.getframeinfo(frame).positions.lineno
    col = inspect.getframeinfo(frame).positions.col_offset
    url = "%s:%s:%s" % (path, line, col)
    return bugger_base(log, line, url)


def logger(log):
    """the logger method"""
    frame = inspect.currentframe().f_back
    path = get_relative_path(frame)
    line = inspect.getframeinfo(frame).positions.lineno
    col = inspect.getframeinfo(frame).positions.col_offset
    url = "%s:%s:%s" % (path, line, col)
    return logger_base(log, line, url)


def egger(log):
    """the egger method"""
    frame = inspect.currentframe().f_back
    path = get_relative_path(frame)
    line = inspect.getframeinfo(frame).positions.lineno
    col = inspect.getframeinfo(frame).positions.col_offset
    url = "%s:%s:%s" % (path, line, col)
    return egger_base(log, line, url)
