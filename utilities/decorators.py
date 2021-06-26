import time


def my_timer(func):
    def wrapper(*args, **kwargs):
        print(f"my_timer started with {func.__name__}")

        start = time.time()
        result = func(*args, **kwargs)
        print(f"Process time: {time.time() - start}")

        return result
    return wrapper
