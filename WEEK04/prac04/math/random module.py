import random

# 1) randint
print(random.randint(1, 10))

# 2) choice
print(random.choice(["rock", "paper", "scissors"]))

# 3) shuffle
arr = [1, 2, 3, 4, 5]
random.shuffle(arr)
print(arr)

# 4) sample (уникальные)
print(random.sample(range(1, 21), 5))

# 5) random() float 0..1
print(round(random.random(), 4))