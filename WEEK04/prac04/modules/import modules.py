# 1) import math
import math
print(math.sqrt(49))

# 2) from math import pi
from math import pi
print(pi)

# 3) import as (псевдоним)
import random as rnd
print(rnd.randint(1, 5))

# 4) импорт нескольких имён
from math import sin, cos
print(round(sin(1), 4), round(cos(1), 4))

# 5) проверка __name__ (как запускается файл)
print("module name =", __name__)