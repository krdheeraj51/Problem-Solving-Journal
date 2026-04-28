# Number Words
# Given an integer from 0 to 99, return its English word representation.

# 0 returns "zero".
# Numbers 1-19 have unique names ("one", "two", ..., "ten", "eleven", ..., "eighteen", "nineteen").
# Multiples of 10 from 20-90 have their own names ("twenty", "thirty", ..., "eighty", "ninety").
# Numbers 21-99 that are not multiples of 10 are written as two words joined by a hyphen. For example "forty-two" and "fifty-three".

# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-28

def number_word(n):
    if n == 0:
        return "zero"
    
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    if n < 10:
        return units[n]
    elif n < 20:
        return teens[n - 10]
    else:
        ten_part = tens[n // 10]
        unit_part = units[n % 10]
        if unit_part:
            return f"{ten_part}-{unit_part}"
        else:
            return ten_part