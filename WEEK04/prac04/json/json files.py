import json

# 1) записать в файл
data = {"name": "Ernur", "score": 95}
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("saved data.json")

# 2) прочитать из файла
with open("data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
print(loaded)

# 3) запись списка
arr = [1, 2, 3]
with open("arr.json", "w", encoding="utf-8") as f:
    json.dump(arr, f)
print("saved arr.json")

# 4) чтение + проверка типа
with open("arr.json", "r", encoding="utf-8") as f:
    x = json.load(f)
print(x, type(x))

# 5) безопасное чтение (если файла нет)
try:
    with open("missing.json", "r", encoding="utf-8") as f:
        json.load(f)
except FileNotFoundError:
    print("file not found")