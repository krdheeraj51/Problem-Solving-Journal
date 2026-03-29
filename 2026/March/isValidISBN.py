# ISBN-10 Validator
# Given a string, determine if it's a valid ISBN-10.

# An ISBN-10 consists of hyphens ("-") and 10 other characters. After removing the hyphens ("-"):

# The first 9 characters must be digits, and
# The final character may be a digit or the letter "X", which represents the number 10.
# To validate it:

# Multiply each digit (or value) by its position (multiply the first digit by 1, the second by 2, and so on).
# Add all the results together.
# If the total is divisible by 11, it's valid.

def is_valid_isbn10(s):
    s = s.replace('-', '')
    
    if len(s) != 10:
        return False
    
    total = 0
    for i in range(10):
        if s[i].isdigit():
            total += (i + 1) * int(s[i])
        elif s[i] == 'X' and i == 9:
            total += (i + 1) * 10
        else:
            return False    
    
    return total % 11 == 0

print(is_valid_isbn10("3-598-21508-8"))  # Output: True
print(is_valid_isbn10("0-306-40615-2"))  # Output: True
print(is_valid_isbn10("3-598-21508-9"))  # Output: False
print(is_valid_isbn10("0-8044-2957-X"))  # Output: True