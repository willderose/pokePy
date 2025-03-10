# -----------------------------------------------------------#
# Created by William Desrosiers                             #
# -----------------------------------------------------------#
import logging
from importlib import reload


class PokeFormatter(logging.Formatter):
    """ Simple formatter with colors for desired levels
    """

    COLOR_INFO = '\x1b[39;20m'
    COLOR_WARNING = '\x1b[33;20m'
    COLOR_ERROR = '\x1b[31;20m'
    COLOR_RESET = '\x1b[0m'

    LOGGING_FORMAT = '%(levelname)s [%(name)s.%(funcName)s] - %(message)s'

    def format(self, record: logging.LogRecord):
        levelName = record.levelname
        levelColor = getattr(PokeFormatter, 'COLOR_{}'.format(levelName.upper()), PokeFormatter.COLOR_INFO)
        formatter = logging.Formatter(''.join((levelColor, PokeFormatter.LOGGING_FORMAT, PokeFormatter.COLOR_RESET)))
        return formatter.format(record)


def createLogger(loggerName) -> 'logging.Logger':
    """Create a logger instance that will serve as the parent of this data hierarchy
    """

    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG)
    if not logger.hasHandlers():
        consoleHandler = logging.StreamHandler()
        consoleHandler.setFormatter(PokeFormatter())
        logger.addHandler(consoleHandler)
        logger.info('Successfully created logger')

    return logger
