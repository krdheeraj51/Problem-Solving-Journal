# Last Letter
# Given a string, return the letter from the string that appears last in the alphabet.

# If two or more letters tie for the last in the alphabet, return the first one.
# Ignore all non-letter characters.
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-13

def last_letter(s):
    # Filter out non-letter characters and convert to uppercase
    letters = [char.upper() for char in s if char.isalpha()]
    
    print(letters)  # Debugging: print the list of letters
    # If there are no letters, return an empty string
    if not letters:
        return ''
    
    # Find the last letter in the alphabet
    last = max(letters)
    
    return last

print(last_letter("hello world!"))  # Output: "W"
print(last_letter("world"))