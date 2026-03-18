# Largest Number
# Given a string of numbers separated by various punctuation, return the largest number.

# The given string will only contain numbers and separators.
# Separators can be commas (","), exclamation points ("!"), question marks ("?"), 
# colons (":"), or semi-colons (";").
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-18


def largest_number(s):
    # Replace all separators with a space
    for sep in [",", "!", "?", ":", ";"]:
        s = s.replace(sep, " ")
    
    # Split the string into numbers and convert to floats
    numbers = [float(num) for num in s.split()]
    
    # Return the largest number
    return max(numbers)

# Test Cases
print(largest_number("1, 2, 3!"))  # 3
print(largest_number("10; 20: 30?"))  # 30
print(largest_number("5! 4, 3: 2; 1"))  # 5
print(largest_number("100, 200, 300!"))  # 300
print(largest_number("12;-50,99.9,49.1!-10.1?88?16"))  # 99
