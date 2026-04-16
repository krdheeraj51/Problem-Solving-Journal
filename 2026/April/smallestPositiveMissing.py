# Smallest Positive Missing Number
#  You are given an integer array arr[]. Your task is to find the smallest positive number missing from the array.

# Note: Positive number starts from 1. The array can have negative integers too.

# Examples:

# Input: arr[] = [2, -3, 4, 1, 1, 7]
# Output: 3
# Explanation: Smallest positive missing number is 3.

def smallest_positive_missing(arr):
    # Create a set of positive numbers in the array for O(1) lookups
    positive_numbers = set(num for num in arr if num > 0)
    
    # Start checking from 1 upwards to find the smallest missing positive number
    smallest_missing = 1
    while smallest_missing in positive_numbers:
        smallest_missing += 1
        
    return smallest_missing

print(smallest_positive_missing([2, -3, 4, 1, 1, 7]))  # Output: 3
print(smallest_positive_missing([-1, -2, -3]))  # Output: 1