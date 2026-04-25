# Word Compressor
# Given a string, return a compressed version of the string using the following rules:

# The first occurrence of a word remains unchanged.
# Subsequent occurrences are replaced with the position of the first occurrence, where the first word is at position 1.
# Words are separated by a single space.
# For example, given "practice makes perfect and perfect practice makes perfect", return "practice makes perfect and 3 1 2 3".

def word_compressor(s):
    words = s.split()
    word_positions = {}
    compressed_words = []
    
    for i, word in enumerate(words):
        if word not in word_positions:
            word_positions[word] = i + 1  # Store the position (1-indexed)
            compressed_words.append(word)
        else:
            compressed_words.append(str(word_positions[word]))
    
    return ' '.join(compressed_words)