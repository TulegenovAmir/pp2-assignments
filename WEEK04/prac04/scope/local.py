# 1) переменная внутри функции (локальная)
def f():
    x = 10
    return x
print(f())

# 2) локальная не видна снаружи
def g():
    y = 7
    return y
print(g())
# print(y)  # ошибка, если раскомментировать

# 3) локальная переменная "перекрывает" внешнюю
x = 100
def h():
    x = 5
    return x
print(x, h())

# 4) параметры функции — тоже локальные
def add(a, b):
    return a + b
print(add(2, 3))

# 5) переменная цикла в функции — локальная
def count():
    for i in range(3):
        pass
    return i
print(count())  # 2