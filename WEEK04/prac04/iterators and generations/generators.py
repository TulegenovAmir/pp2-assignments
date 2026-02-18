# 1) yield простые значения
def g1():
    yield 1
    yield 2
    yield 3
print(list(g1()))

# 2) генератор квадратов
def squares(n):
    for i in range(1, n + 1):
        yield i * i
print(list(squares(5)))

# 3) генератор чётных из списка
def evens(nums):
    for x in nums:
        if x % 2 == 0:
            yield x
print(list(evens([1,2,3,4,5,6])))

# 4) бесконечный генератор (берём первые 5)
def powers2():
    x = 1
    while True:
        yield x
        x *= 2

p = powers2()
for _ in range(5):
    print(next(p), end=" ")
print()

# 5) yield from
def letters():
    yield from "abc"
print(list(letters()))