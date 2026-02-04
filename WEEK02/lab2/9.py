n=int(input())
numbers=list(map(int, input().split()))
max_number=max(numbers)
min_number=min(numbers)
for i in range(n):
    if numbers[i]==max_number:
        numbers[i]=min_number
for num in numbers:
    print(num, end=" ")