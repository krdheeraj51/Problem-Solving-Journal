# Domino Chain Validator
# Given a 2D array representing a sequence of dominoes, determine whether it forms a valid chain.

# Each element in the array represents a domino and will be an array of two numbers from 1 to 6, (inclusive).
# For the chain to be valid, the second number of each domino must match the first number of the next domino.
# The first number of the first domino and the last number of the last domino don't need to match anything.
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-12


def is_valid_domino_chain(chain):
    for i in range(len(chain) - 1):
        if chain[i][1] != chain[i + 1][0]:
            return False
    return True

print(is_valid_domino_chain([[1, 2], [2, 3], [3, 4]]))  # Output: True
print(is_valid_domino_chain([[1, 2], [3, 4], [4, 5]]))  # Output: False

