# Sum the Letters
# Given a string, return the sum of its letters.

# Letters are A-Z in uppercase or lowercase
# Letter values are: "A" = 1, "B" = 2, ..., "Z" = 26
# Uppercase and lowercase letters have the same value.
# Ignore all non-letter characters.
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-02

def sum_letters(s):
    total = 0
    for char in s:
        if char.isalpha():
            total += ord(char.upper()) - ord('A') + 1
    return total