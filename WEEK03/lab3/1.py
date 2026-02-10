def is_valid_number(n):
    
    n = abs(n)  
    for digit in str(n):
        if int(digit) % 2 != 0: 
            return False
    return True


number = int(input())


if is_valid_number(number):
    print("Valid")
else:
    print("Not valid")
