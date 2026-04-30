# Array Search
# Given an array, arr[] of n integers, and an integer element x, find whether element x is present in the array. Return the index of the first occurrence of x in the array, or -1 if it doesn't exist.

# Examples:

# Input: arr[] = [1, 2, 3, 4], x = 3
# Output: 2
# Explanation: For array [1, 2, 3, 4], the element to be searched is 3. Since 3 is present at index 2, the output is 2.
# Input: arr[] = [1, 2, 3, 4], x = 5

def array_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i  # Return the index of the first occurrence
    return -1  # Return -1 if x is not found in the array

# Example usage:
print(array_search([1, 2, 3, 4], 3))
print(array_search([1, 2, 3, 4], 5))    