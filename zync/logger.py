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
        record.levelname = "wegger"
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
            f"{W}{L}%(asctime)s {X}"
            f"{G}[{X}"
            f"{G}%(levelname)s{X}"
            f"{G}] {X}"
            f"{W}%(url)s {X}"
            f"%(message)s{X}",
        )
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def __call__(self, log, url):
        self.logger.debug(log, extra={"url": url})


class Logger:
    """the logger log class"""

    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        file_handler = logging.FileHandler(".zync.log")
        formatter = LoggerFormat(
            f"{W}{L}%(asctime)s {X}"
            f"{C}[{X}"
            f"{C}%(levelname)s{X}"
            f"{C}] {X}"
            f"{W}%(url)s {X}"
            f"%(message)s{X}",
        )
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def __call__(self, log, url):
        self.logger.info(log, extra={"url": url})


class Egger:
    """the egger log class"""

    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.ERROR)
        file_handler = logging.FileHandler(".zync.log")
        formatter = EggerFormat(
            f"{W}{L}%(asctime)s {X}"
            f"{R}[{X}"
            f"{R}%(levelname)s{X}"
            f"{R}] {X}"
            f"{W}%(url)s {X}"
            f"%(message)s{X}",
        )
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def __call__(self, log, url):
        self.logger.error(log, extra={"url": url})


bugger_base = Bugger("bugger")
logger_base = Logger("logger")
wegger_base = Egger("wegger")


def link(frame):
    """getting the relative path for logging position"""
    filename = inspect.getframeinfo(frame).filename
    current_dir = os.getcwd()
    path = os.path.relpath(filename, current_dir)
    line = inspect.getframeinfo(frame).positions.lineno
    col = inspect.getframeinfo(frame).positions.col_offset
    # pylint disable=C0209
    href = f"{path}:{line}:{col}"
    href_link = "file '" + href + "'"
    return href_link


def bugger(log):
    """the bugger method"""
    frame = inspect.currentframe().f_back
    url = link(frame)
    return bugger_base(log, url)


def logger(log):
    """the logger method"""
    frame = inspect.currentframe().f_back
    url = link(frame)
    return logger_base(log, url)


def wegger(log):
    """the egger method"""
    frame = inspect.currentframe().f_back
    url = link(frame)
    return wegger_base(log, url)
