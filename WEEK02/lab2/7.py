n = int(input())
numbers = list(map(int, input().split()))

max_number = numbers[0]
position = 1

for i in range(n):
    if numbers[i] > max_number:
        max_number = numbers[i]
        position = i + 1

print(position)
