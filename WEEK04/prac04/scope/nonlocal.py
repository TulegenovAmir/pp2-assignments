# 1) nonlocal меняет переменную внешней функции
def outer():
    x = 1
    def inner():
        nonlocal x
        x += 1
        return x
    return inner()

print(outer())

# 2) счётчик-замыкание
def make_counter():
    c = 0
    def inc():
        nonlocal c
        c += 1
        return c
    return inc

cnt = make_counter()
print(cnt(), cnt(), cnt())

# 3) nonlocal в нескольких внутренних вызовах
def outer2():
    s = "A"
    def addB():
        nonlocal s
        s += "B"
    def addC():
        nonlocal s
        s += "C"
    addB(); addC()
    return s

print(outer2())

# 4) отличие: без nonlocal была бы ошибка (UnboundLocalError)
def outer3():
    x = 10
    def inner():
        nonlocal x
        x = x + 5
        return x
    return inner()

print(outer3())

# 5) nonlocal для списка (можно и без него, но пример)
def outer4():
    a = [1]
    def inner():
        nonlocal a
        a = a + [2]
        return a
    return inner()

print(outer4())