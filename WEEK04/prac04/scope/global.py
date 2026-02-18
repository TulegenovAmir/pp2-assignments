# 1) чтение глобальной переменной
g = 10
def read():
    return g
print(read())

# 2) изменение глобальной через global
counter = 0
def inc():
    global counter
    counter += 1
inc(); inc()
print(counter)

# 3) глобальная и локальная разные
x = 5
def f():
    x = 99
    return x
print(x, f(), x)

# 4) глобальная константа
PI = 3.14159
def circle_area(r):
    return PI * r * r
print(circle_area(2))

# 5) изменение глобального списка без global (можно)
arr = []
def push(v):
    arr.append(v)
push(1); push(2)
print(arr)