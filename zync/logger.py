import logging
import inspect


WHITE = "\033[39m"
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD_RED = "\033[31;1m"
RESET = "\033[0m"


class Bugger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler("zync.log")
        formatter = logging.Formatter(
            f"{WHITE}[%(levelname)s] %(asctime)s "
            f"@ %(location)s (line %(line)s): %(message)s{RESET}",
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
        file_handler = logging.FileHandler("zync.log")
        formatter = logging.Formatter(
            f"{BLUE}[%(levelname)s] %(asctime)s "
            f"@ %(location)s (line %(line)s): %(message)s{RESET}",
            datefmt="%H:%M:%S",
        )
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def __call__(self, log, line, location):
        self.logger.info(log, extra={"line": line, "location": location})


class Wagger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.WARNING)
        file_handler = logging.FileHandler("zync.log")
        formatter = logging.Formatter(
            f"{GREEN}[%(levelname)s] %(asctime)s "
            f"@ %(location)s (line %(line)s): %(message)s{RESET}",
            datefmt="%H:%M:%S",
        )
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def __call__(self, log, line, location):
        self.logger.warning(log, extra={"line": line, "location": location})


class Egger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.ERROR)
        file_handler = logging.FileHandler("zync.log")
        formatter = logging.Formatter(
            f"{YELLOW}[%(levelname)s] %(asctime)s "
            f"@ %(location)s (line %(line)s): %(message)s{RESET}",
            datefmt="%H:%M:%S",
        )
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def __call__(self, log, line, location):
        self.logger.error(log, extra={"line": line, "location": location})


class Critter:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.CRITICAL)
        file_handler = logging.FileHandler("zync.log")
        formatter = logging.Formatter(
            f"{RED}[%(levelname)s] %(asctime)s "
            f"@ %(location)s (line %(line)s): %(message)s{RESET}",
            datefmt="%H:%M:%S",
        )
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def __call__(self, log, line, location):
        self.logger.critical(log, extra={"line": line, "location": location})


class Fatal:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.FATAL)
        file_handler = logging.FileHandler("zync.log")
        formatter = logging.Formatter(
            f"{BOLD_RED}[%(levelname)s] %(asctime)s "
            f"@ %(location)s (line %(line)s): %(message)s{RESET}",
            datefmt="%H:%M:%S",
        )
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def __call__(self, log, line, location):
        self.logger.fatal(log, extra={"line": line, "location": location})


bugger_base = Bugger("bugger")
logger_base = Logger("logger")
wagger_base = Wagger("wagger")
egger_base = Egger("egger")
critter_base = Critter("critter")
fatal_base = Fatal("fatal")


def bugger(log):
    frame = inspect.currentframe().f_back
    line = inspect.getframeinfo(frame).positions.lineno
    location = inspect.getframeinfo(frame).filename
    return bugger_base(log, line, location)


def logger(log):
    frame = inspect.currentframe().f_back
    line = inspect.getframeinfo(frame).positions.lineno
    location = inspect.getframeinfo(frame).filename
    return logger_base(log, line, location)


def wagger(log):
    frame = inspect.currentframe().f_back
    line = inspect.getframeinfo(frame).positions.lineno
    location = inspect.getframeinfo(frame).filename
    return wagger_base(log, line, location)


def egger(log):
    frame = inspect.currentframe().f_back
    line = inspect.getframeinfo(frame).positions.lineno
    location = inspect.getframeinfo(frame).filename
    return egger_base(log, line, location)


def critter(log):
    frame = inspect.currentframe().f_back
    line = inspect.getframeinfo(frame).positions.lineno
    location = inspect.getframeinfo(frame).filename
    return critter_base(log, line, location)


def fatal(log):
    frame = inspect.currentframe().f_back
    line = inspect.getframeinfo(frame).positions.lineno
    location = inspect.getframeinfo(frame).filename
    return fatal_base(log, line, location)


bugger("01234567890123456789012345678901234567890123")
logger("01234567890123456789012345678901234567890123")
wagger("01234567890123456789012345678901234567890123")
egger("012345678901234567890123456789012345678901234")
critter("0123456789012345678901234567890123456789012")
fatal("012345678901234567890123456789012345678901234")
