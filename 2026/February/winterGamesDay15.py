# 2026 Winter Games Day 15: Freestyle Skiing
# Given a trick name consisting of two words, determine if it is a valid freestyle skiing trick name.

# A trick is valid if the first word is in the list of valid first words, and the second word is in the list of valid second words.

# The two words will be separated by a single space.
# Valid first words:

# "Misty"
# "Ghost"
# "Thunder"
# "Solar"
# "Sky"
# "Phantom"
# "Frozen"
# "Polar"

# Valid second words:

# "Twister"
# "Icequake"
# "Avalanche"
# "Vortex"
# "Snowstorm"
# "Frostbite"
# "Blizzard"
# "Shadow"

def is_valid_trick(trick_name):
    valid_first_words = ["Misty", "Ghost", "Thunder", "Solar", "Sky", "Phantom", "Frozen", "Polar"]
    valid_second_words = ["Twister", "Icequake", "Avalanche", "Vortex", "Snowstorm", "Frostbite", "Blizzard", "Shadow"]
    
    words = trick_name.split()
    
    if len(words) != 2:
        return False
    
    first_word, second_word = words
    
    return first_word in valid_first_words and second_word in valid_second_words