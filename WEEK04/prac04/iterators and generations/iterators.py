# 1) iter + next
it = iter([1, 2, 3])
print(next(it), next(it), next(it))

# 2) StopIteration (ловим ошибку)
it = iter([10])
print(next(it))
try:
    print(next(it))
except StopIteration:
    print("StopIteration")

# 3) list() "съедает" итератор
it = iter(range(4))
print(list(it))

# 4) reversed() — итератор
rev = reversed([5, 6, 7])
print(next(rev), next(rev), next(rev))

# 5) enumerate() — итератор пар (индекс, значение)
print(list(enumerate(["a", "b", "c"], start=1)))