n = int(input())
arr = list(map(int, input().split()))
q = int(input())

for _ in range(q):
    op = input().split()
    if op[0] == "add":
        arr = list(map(lambda x: x + int(op[1]), arr))
    elif op[0] == "multiply":
        arr = list(map(lambda x: x * int(op[1]), arr))
    elif op[0] == "power":
        arr = list(map(lambda x: x ** int(op[1]), arr))
    else:
        arr = list(map(lambda x: abs(x), arr))

print(*arr)
