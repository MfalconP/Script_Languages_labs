import logging
import time
from functools import wraps
import inspect


def log(level=logging.DEBUG):
    def decorator(func_or_class):
        logger = logging.getLogger(func_or_class.__module__)
        logger.setLevel(level)

        @wraps(func_or_class)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func_or_class(*args, **kwargs)
            end_time = time.time()
            elapsed_time = end_time - start_time
            logger.log(level, f"Called {func_or_class.__name__} with args={args} kwargs={kwargs}, "
                              f"returned {result}, took {elapsed_time:.6f}s")
            return result

        if inspect.isclass(func_or_class):
            def __new__(cls, *args, **kwargs):
                instance = object.__new__(cls)
                logger.log(level,
                           f"Created instance of class {func_or_class.__name__} with args={args} kwargs={kwargs}")
                return instance

            wrapper.__new__ = __new__

        return wrapper

    return decorator


@log(logging.INFO)
class MyClass:
    def __init__(self, arg):
        self.arg = arg


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)


    @log(logging.INFO)
    def add(x, y):
        return x + y

    add(2, 3)

    MyClass(42)
