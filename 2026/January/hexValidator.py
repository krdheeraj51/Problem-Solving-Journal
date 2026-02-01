#                     Hex Validator
# Given a string, determine whether it is a valid CSS hex color. A valid CSS hex color must:

# Start with a #, and
# be followed by either 3 or 6 hexadecimal characters.
# Hexadecimal characters are numbers 0 through 9 and letters a through f (case-insensitive).

def is_valid_hex_color(s):
    if not s.startswith('#'):
        return False
    
    hex_part = s[1:]
    if len(hex_part) not in [3, 6]:
        return False
    
    for char in hex_part:
        if char.lower() not in '0123456789abcdef':
            return False
    
    return True