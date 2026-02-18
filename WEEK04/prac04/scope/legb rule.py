# LEGB: Local -> Enclosing -> Global -> Built-in

# 1) Global
x = "GLOBAL"
def f():
    return x
print(f())

# 2) Local
def f2():
    x = "LOCAL"
    return x
print(f2())

# 3) Enclosing
def outer():
    x = "ENCLOSING"
    def inner():
        return x
    return inner()
print(outer())

# 4) Built-in (len)
print(len([1, 2, 3]))

# 5) Перекрытие built-in (плохая идея, но пример)
len = 123
print("len variable =", len)
# print(len([1,2]))  # ошибка, если раскомментировать