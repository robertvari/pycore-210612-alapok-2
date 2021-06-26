import time, logging
from datetime import datetime

def my_timer(func):
    def wrapper(*args, **kwargs):
        print(f"my_timer started with {func.__name__}")

        start = time.time()
        result = func(*args, **kwargs)
        print(f"Process time: {time.time() - start}")

        return result
    return wrapper


def my_logger(func):
    logging.basicConfig(filename=f"{func.__name__}.log", level=logging.INFO)

    def wrapper(*args, **kwargs):
        print(f"my_logger started with {func.__name__}")

        logging.info(f"{datetime.now()} Run with args: {args} and kwargs {kwargs}")

        result = func(*args, **kwargs)
        return result
    return wrapper