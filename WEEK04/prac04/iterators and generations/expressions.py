# 1) обычное generator expression
g = (x * 2 for x in range(5))
print(list(g))

# 2) с условием if
g = (x for x in range(10) if x % 3 == 0)
print(list(g))

# 3) вложенные циклы
g = (a + b for a in [1, 2] for b in [10, 20])
print(list(g))

# 4) sum() с generator expression
print(sum(x for x in range(1, 6)))

# 5) any/all
print(any(x < 0 for x in [1, -2, 3]))
print(all(x > 0 for x in [1, 2, 3]))