import logging


class Logger:
    __instance = None

    @staticmethod
    def get_instance():
        if Logger.__instance is None:
            return Logger()
        return Logger.__instance

    def __init__(self, level=logging.DEBUG):
        if Logger.__instance is not None:
            raise Exception("Invalid re-instantiation of Logger")
        else:
            logging.basicConfig(
                level=level,
                format='%(asctime)s %(levelname)-8s %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S',
            )
            Logger.__instance = self

    def _prefix(self):
        return ""

    def debug(self, msg):
        logging.debug(f"{self._prefix()}{msg}")

    def info(self, msg):
        logging.info(f"{self._prefix()}{msg}")

    def warning(self, msg):
        logging.warning(f"{self._prefix()}{msg}")

    def error(self, msg):
        logging.error(f"{self._prefix()}{msg}")


def logger():
    return Logger.get_instance()
