# Add Punctuation
# Given a string of sentences with missing periods, add a period (".") in the following places:

# Before each space that comes immediately before an uppercase letter
# And at the end of the string
# Return the resulting string.
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-02-28

def add_punctuation(s):
    result = ""
    for i in range(len(s)):
        if s[i] == " " and i + 1 < len(s) and s[i + 1].isupper():
            result += ". "
        else:
            result += s[i]
    if not result.endswith("."):
        result += "."
    return result

# Test cases
print(add_punctuation("Hello World This Is A Test"))  # "Hello. World. This. Is. A. Test."
print(add_punctuation("This is a test"))  # "This is a test."   