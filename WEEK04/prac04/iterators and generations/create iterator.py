# 1) простой итератор-класс 1..n
class OneToN:
    def __init__(self, n):
        self.n = n
        self.cur = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur > self.n:
            raise StopIteration
        v = self.cur
        self.cur += 1
        return v

print(list(OneToN(5)))

# 2) итератор по словам строки
class Words:
    def __init__(self, s):
        self.words = s.split()
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= len(self.words):
            raise StopIteration
        w = self.words[self.i]
        self.i += 1
        return w

print(list(Words("hi there friend")))

# 3) итератор с шагом
class StepRange:
    def __init__(self, start, stop, step):
        self.cur = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur >= self.stop:
            raise StopIteration
        v = self.cur
        self.cur += self.step
        return v

print(list(StepRange(0, 10, 3)))

# 4) итератор: первые n чётных
class Evens:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.cur = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        v = self.cur
        self.cur += 2
        self.count += 1
        return v

print(list(Evens(6)))

# 5) ручной проход next()
it = iter(OneToN(3))
print(next(it), next(it), next(it))