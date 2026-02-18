# 1) переменная модуля
VERSION = "1.0"

# 2) функция: максимум
def my_max(a, b):
    return a if a > b else b

# 3) функция: факториал
def fact(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

# 4) класс
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 5) "публичные" имена (не обязательно)
__all__ = ["VERSION", "my_max", "fact", "Point"]