from functools import reduce


def forall(pred, iterable):
    return reduce(lambda acc, x: acc and pred(x), iterable, True)


def exists(pred, iterable):
    return any(map(pred, iterable))


def atleast(n, pred, iterable):
    return reduce(lambda count, elem: count + 1 if pred(elem) else count, iterable, 0) >= n


def atmost(n, pred, iterable):
    return reduce(lambda count, x: count + 1 if pred(x) else count, iterable, 0) <= n


if __name__ == '__main__':
    print(forall(lambda x: x > 5, [5, 6, 7, 8, 9, 10, 12]))

    print(exists(lambda x: x > 5, [5, 6, 7, 8, 9, 10, 12]))

    print(atleast(3, lambda x: x > 0, [-1, -2, 0, 2, 1, 1]))

    print(atleast(3, lambda x: x > 0, [-1, -2, 0, 2, 1, 1]))

    print(atmost(3, lambda x: x > 0, [-1, -2, 0, 2, 1, 1, 10]))
