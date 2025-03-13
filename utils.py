import logging
from logging.handlers import RotatingFileHandler


def setup_logger():
    logger = logging.getLogger("lsm")
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    file_handler = RotatingFileHandler("lsm.log", maxBytes = 1_000_000, backupCount = 3)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger



logger = setup_logger()
