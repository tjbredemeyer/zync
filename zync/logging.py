import logging


class Logger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)

    def __call__(self, log):
        self.logger.info(log)


logger_base = Logger(__name__)


def logger(log):
    return logger_base(log)


class Bugger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)

    def __call__(self, log):
        self.logger.debug(log)


bugger_base = Bugger(__name__)


def bugger(log):
    return bugger_base(log)
