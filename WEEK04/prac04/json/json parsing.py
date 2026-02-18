import json

# 1) loads: строка -> dict
s = '{"name":"Ali","age":20}'
data = json.loads(s)
print(data, type(data))

# 2) доступ к полям
print(data["name"], data["age"])

# 3) список в json
s2 = '[1, 2, 3, 4]'
arr = json.loads(s2)
print(arr, type(arr))

# 4) вложенные объекты
s3 = '{"user":{"id":1,"skills":["py","js"]}}'
d3 = json.loads(s3)
print(d3["user"]["skills"][0])

# 5) обработка ошибки json
bad = "{name: 5}"
try:
    json.loads(bad)
except json.JSONDecodeError:
    print("bad json")