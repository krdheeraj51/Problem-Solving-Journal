# No Consecutive Repeats
# Given a string, determine if it has no repeating characters.

# A string has no repeats if it does not have the same character two or more times in a row.

def no_consecutive_repeats(s):
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            return False
    return True