import random


class PasswordGenerator:
    def __init__(self, length, charset=None, count=float('inf')):
        if charset is None:
            self.charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        else:
            self.charset = charset
        self.length = length
        self.count = count
        self.generated_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.generated_count >= self.count:
            raise StopIteration
        password = ''.join(random.choices(self.charset, k=self.length))
        self.generated_count += 1
        return password


if __name__ == '__main__':
    pg = PasswordGenerator(8, count=5)
    for password in pg:
        print(password)

    pg = PasswordGenerator(8, count=3)
    print(next(pg))
    print(next(pg))
    print(next(pg))
