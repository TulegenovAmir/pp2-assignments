# Обычно "модуль" — это другой файл my_module.py
# Здесь покажу 5 вещей, которые обычно кладут в модуль.

# 1) константа
PI = 3.14159

# 2) функция
def add(a, b):
    return a + b

# 3) ещё функция
def circle_area(r):
    return PI * r * r

# 4) класс
class Greeter:
    def __init__(self, name):
        self.name = name
    def hello(self):
        return f"Hi, {self.name}!"

# 5) блок запуска (как "тест модуля")
if __name__ == "__main__":
    print(add(2, 3))
    print(circle_area(2))
    print(Greeter("Ernur").hello())