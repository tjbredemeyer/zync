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
    def format(self, record):
        record.levelname = "bugger"
        levelname = record.levelname.upper()
        record.levelname = levelname
        return super().format(record)


class LoggerFormat(logging.Formatter):
    def format(self, record):
        record.levelname = "logger"
        levelname = record.levelname.upper()
        record.levelname = levelname
        return super().format(record)


class Bugger:
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


bugger_base = Bugger("bugger")
logger_base = Logger("logger")


def bugger(log):
    frame = inspect.currentframe().f_back
    path = inspect.getframeinfo(frame).filename
    line = inspect.getframeinfo(frame).positions.lineno
    col = inspect.getframeinfo(frame).positions.col_offset
    url = "%s:%s:%s" % (path, line, col)
    return bugger_base(log, line, url)


def logger(log):
    frame = inspect.currentframe().f_back
    path = inspect.getframeinfo(frame).filename
    line = inspect.getframeinfo(frame).positions.lineno
    col = inspect.getframeinfo(frame).positions.col_offset
    url = "%s:%s:%s" % (path, line, col)
    log = f"<a href='{url}'>click here</a>"
    return logger_base(log, line, url)
