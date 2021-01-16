import logging


class LogFile(object):

    def __init__(self, filename: str):
        logging.basicConfig(filename, level=logging.DEBUG)

    def write(self, message: str):
        logging.info(message)
