from datetime import datetime, timedelta

# 1) плюс 1 день
d = datetime(2026, 2, 7)
print(d + timedelta(days=1))

# 2) минус 2 часа
t = datetime(2026, 2, 7, 10, 0)
print(t - timedelta(hours=2))

# 3) разница дат
a = datetime(2026, 2, 7, 12, 0)
b = datetime(2026, 2, 7, 9, 30)
diff = a - b
print(diff, diff.seconds // 60, "minutes")

# 4) через неделю
print(d + timedelta(weeks=1))

# 5) округление до минут (пример)
x = datetime(2026, 2, 7, 12, 34, 56)
rounded = x.replace(second=0, microsecond=0)
print(rounded)