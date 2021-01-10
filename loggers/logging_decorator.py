import logging
from functools import wraps

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s -%(levelname)s -%(message)s"
)


def logger(func):
    """
    logger decorator
    :param func: the function to decorate
    :return: func: the function decorated
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            value = func(*args, **kwargs)
        except Exception as e:
            logging.error("Something wrong happened with the function call")
            logging.error("Details: {}".format(e))
            raise
        return value
    return wrapper
