def make_generator(f):
    def generator():
        n = 1
        while True:
            yield f(n)
            n += 1
    return generator()


def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    fibonacci_gen = make_generator(fibonacci)

    for i in range(10):
        print(next(fibonacci_gen))

    geometric_gen = make_generator(lambda x: 2**x)

    print("*************************************")

    for i in range(10):
        print(next(geometric_gen))
