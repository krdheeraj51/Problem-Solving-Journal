# Word Score
# Given a word, return its score using a standard letter-value table:

# Letter	Value
# A	1
# B	2
# ...	...
# Z	26
# Upper and lowercase letters have the same value.

def word_score(word):
    score = 0
    for char in word:
        if char.isalpha():  # Check if the character is a letter
            score += ord(char.upper()) - ord('A') + 1  # Convert to uppercase and calculate score
    return score

# Example usage:
print(word_score("hello"))  # Output: 52 (8 + 5 + 12 + 12 + 15)
print(word_score("hi"))     # Output: 17 (h = 8, i = 9)