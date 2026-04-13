# Name Initials
# Given a full name as a string, return their initials.

# Names to initialize are separated by a space.
# Initials should be made uppercase.
# Initials should be separated by dots.
# For example, "Tommy Millwood" returns "T.M.".
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-13

def name_initials(full_name):
    # Split the full name into parts
    name_parts = full_name.split()
    
    # Get the first letter of each part, convert to uppercase, and join with dots
    initials = '.'.join(part[0].upper() for part in name_parts) + '.'
    
    return initials

