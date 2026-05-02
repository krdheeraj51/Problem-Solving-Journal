# Anagram Groups
# Given an array of words, return a 2d array of the words grouped into anagrams.

# Words are anagrams if they contain the same letters in any order.
# Each word belongs to exactly one group.
# Return order doesn't matter.
# For example, given ["listen", "silent", "hello", "enlist", "world"], return [["listen", "silent", "enlist"], ["hello"], ["world"]].

def group_anagrams(words):
    anagram_dict = {}
    for word in words:
        # Sort the letters of the word to create a key
        sorted_word = ''.join(sorted(word))
        # print(f"Current anagram groups: {anagram_dict}")  # Debugging statement
        # Add the word to the corresponding anagram group
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    
    # Return the groups of anagrams as a list of lists
    return list(anagram_dict.values())

# Example usage:
print(group_anagrams(["listen", "silent", "hello", "enlist", "world "]))    
