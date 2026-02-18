from datetime import datetime

# 1) текущая дата-время
now = datetime.now()
print(now)

# 2) отдельные части
print(now.year, now.month, now.day)

# 3) создать конкретный datetime
dt = datetime(2026, 2, 7, 12, 30, 0)
print(dt)

# 4) сравнение дат
a = datetime(2026, 1, 1)
b = datetime(2026, 2, 1)
print(a < b)

# 5) timestamp (секунды)
print(int(now.timestamp()))