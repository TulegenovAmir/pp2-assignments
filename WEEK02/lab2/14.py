n = int(input())
numbers = list(map(int, input().split()))

freq = {}

for num in numbers:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

max_count = max(freq.values())

answer = min(num for num in freq if freq[num] == max_count)

print(answer)
