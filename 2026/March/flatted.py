# Flattened
# Given an array, determine if it is flat.

# An array is flat if none of its elements are arrays.

def is_flat(arr):
    for element in arr:
        if isinstance(element, list):
            return False
    return True