import functools
from functools import lru_cache


def make_generator_mem(f):
    @lru_cache(maxsize=None)
    def memoized_f(n):
        return f(n)

    def generator():
        n = 1
        while True:
            yield memoized_f(n)
            n += 1

    return generator()


@functools.cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    fibonacci_gen = make_generator_mem(fibonacci)
    for i in range(1000):
        print(f"{i}. {next(fibonacci_gen)}")
        