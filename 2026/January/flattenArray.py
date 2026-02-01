# Flatten the Array
# Given an array that contains nested arrays, return a new array with all values flattened into a 
# single, one-dimensional array. Retain the original order of the items in the arrays.

def flatten_array(nested_array):
    flattened = []
    for item in nested_array:
        if isinstance(item, list):
            flattened.extend(flatten_array(item))
        else:
            flattened.append(item)
    return flattened

# Example usage:
nested_array = [1, [2, [3, 4], 5], 6, [7, 8]]
print(flatten_array(nested_array))  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# Learning Points:
# 1. Recursion: The function uses recursion to handle arrays nested at multiple levels.
# 2. Type Checking: The isinstance function is used to check if an item is a list, allowing the function to
#    differentiate between nested arrays and individual elements.
# 3. List Manipulation: The extend method is used to add multiple elements to the flattened list at once, 
# while append is used for single elements.
# 4. Order Preservation: The function maintains the order of elements as they appear in the original nested array.
