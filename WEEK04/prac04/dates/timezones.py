from datetime import datetime, timezone, timedelta

# 1) UTC время (aware)
utc_now = datetime.now(timezone.utc)
print(utc_now)

# 2) свой фиксированный часовой пояс (UTC+6, например)
tz_plus6 = timezone(timedelta(hours=6))
print(datetime.now(tz_plus6))

# 3) конвертация UTC -> UTC+6
converted = utc_now.astimezone(tz_plus6)
print(converted)

# 4) создать aware datetime сразу
dt = datetime(2026, 2, 7, 12, 0, tzinfo=timezone.utc)
print(dt)

# 5) разница двух aware дат
a = datetime(2026, 2, 7, 12, 0, tzinfo=timezone.utc)
b = datetime(2026, 2, 7, 18, 0, tzinfo=tz_plus6)  # это тоже 12:00 UTC
print(a == b)