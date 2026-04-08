# FizzBuzz Validator
# Given an array of sequential integers, with multiples of 3 and 5 replaced, determine if it's a valid FizzBuzz sequence.

# In a valid FizzBuzz sequence:

# Multiples of 3 are replaced with "Fizz".
# Multiples of 5 are replaced with "Buzz".
# Multiples of both 3 and 5 are replaced with "FizzBuzz".
# All other numbers remain as integers.
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-08

def fizz_buzz_validator(sequence):
    start = None 
    for val in sequence:
        if isinstance(val, int):
            start = val
            break
        if start == None:
            return False
    for i, value in enumerate(sequence, start=start):
        if i % 3 == 0 and i % 5 == 0:
            expected = "FizzBuzz"
        elif i % 3 == 0:
            expected = "Fizz"
        elif i % 5 == 0:
            expected = "Buzz"
        else:
            expected = i
        
        if value != expected:
            return False
            
    return True

print(fizz_buzz_validator([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]))  # Output: True
print(fizz_buzz_validator([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "Fizz"]))  # Output: False