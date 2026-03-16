# Evenly Divisible
# Given two integers, determine if you can evenly divide the first one by the second one.

def evenly_divide(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False
# Test Cases
print(evenly_divide(98, 7)) # True
print(evenly_divide(85, 4)) # False


