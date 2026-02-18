import json

# 1) dumps: dict -> строка
d = {"a": 1, "b": 2}
print(json.dumps(d))

# 2) dumps с красивым форматированием
print(json.dumps(d, indent=2))

# 3) ensure_ascii=False (чтобы кириллица была норм)
d2 = {"city": "Алматы"}
print(json.dumps(d2, ensure_ascii=False))

# 4) сортировка ключей
print(json.dumps({"b": 1, "a": 2}, sort_keys=True))

# 5) преобразование списка dict
users = [{"id": 1}, {"id": 2}]
print(json.dumps(users))