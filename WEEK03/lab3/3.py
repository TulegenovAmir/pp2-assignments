triplets = ["ZER","ONE","TWO","THR","FOU","FIV","SIX","SEV","EIG","NIN"]

def to_number(s):
    num = 0
    for i in range(0, len(s), 3):
        num = num * 10 + triplets.index(s[i:i+3])
    return num

def to_triplets(n):
    if n == 0:
        return "ZER"
    res = ""
    while n > 0:
        res = triplets[n % 10] + res
        n //= 10
    return res

expr = input()
for op in "+-*":
    if op in expr:
        a,b = expr.split(op)
        a = to_number(a)
        b = to_number(b)
        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        else:
            result = a * b
        print(to_triplets(result))
        break
