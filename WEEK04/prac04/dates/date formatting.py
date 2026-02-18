from datetime import datetime

dt = datetime(2026, 2, 7, 15, 4, 9)

# 1) strftime формат
print(dt.strftime("%Y-%m-%d"))

# 2) время
print(dt.strftime("%H:%M:%S"))

# 3) красиво
print(dt.strftime("%d.%m.%Y %H:%M"))

# 4) parse через strptime
s = "2026-02-07 15:04:09"
parsed = datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
print(parsed)

# 5) ISO формат
print(dt.isoformat())