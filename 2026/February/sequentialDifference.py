# Sequential Difference
# Given an array of numbers, return a new array containing the value needed to get from each number to the next number.

# For the last number, use 0 since there is no next number.
# For example, given [1, 2, 4, 7], return [1, 2, 3, 0].

def sequential_difference(arr):
    differences = []
    
    for i in range(len(arr) - 1):
        difference = arr[i + 1] - arr[i]
        differences.append(difference)
    
    differences.append(0)  # For the last number, add 0
    
    return differences