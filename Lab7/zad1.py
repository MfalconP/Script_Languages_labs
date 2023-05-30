from functools import reduce
from collections import defaultdict


def acronym(lst):
    def helper(xs, result):
        return result if xs == [] else helper(xs[1:], result + xs[0][0])
    return helper(lst, "")


def median(lst):
    lst.sort()
    if len(lst) % 2 == 0:
        return (lst[len(lst)//2] + lst[len(lst)//2 - 1]) / 2
    else:
        return lst[len(lst) // 2]


def pierwiastek(x, epsilon):
    def newton_iter(y):
        return (y + x/y) / 2

    def within_tolerance(y):
        return abs(y**2 - x) < epsilon

    def improve_guess(y):
        return newton_iter(y)

    def find_root(guess):
        if within_tolerance(guess):
            return guess
        else:
            return find_root(improve_guess(guess))

    return find_root(1.0)


def make_alpha_dict(s):
    char_word_pairs = reduce(lambda x, y: x+y,
                             map(lambda word: list(map(lambda char: (char, word),
                                                       filter(lambda c: c.isalpha(), word))),
                                 s.split()))
    return dict(reduce(lambda d, pair: (d.update({pair[0].lower(): d[pair[0].lower()]+[pair[1]]}) or d),
                       char_word_pairs, defaultdict(list)))


def flatten(lst):
    return [lst] if not isinstance(lst, (list, tuple)) else sum(map(flatten, lst), [])



if __name__ == '__main__':
    print(acronym(["Zaklad", "Ubezpieczen", "Spolecznych"]))
    print(median([1, 1, 19, 2, 3, 4, 4, 5, 1]))
    print(pierwiastek(3, epsilon=0.1))
    print(make_alpha_dict("on i ona"))
    print(flatten([1, [2, 3], [[4, 5], 6]]))

