# Sort 0s, 1s and 2s 
# Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.
# # Note: You need to solve this problem without utilizing the built-in sort function.
# Examples:
# Input: arr[] = [0, 1, 2, 0, 1, 2]
# Output: [0, 0, 1, 1, 2, 2]
# Explanation: 0s, 1s and 2s are segregated into ascending order.
# Input: arr[] = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
# Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
# Explanation: 0s, 1s and 2s are segregated into ascending order.

def sort_012(arr):
    count_0 = arr.count(0)
    count_1 = arr.count(1)
    count_2 = arr.count(2)
    
    sorted_arr = [0] * count_0 + [1] * count_1 + [2] * count_2
    return sorted_arr
# Example usage:
arr = [0, 1, 2, 0, 1, 2]
print(sort_012(arr))  # Output: [0, 0, 1, 1, 2, 2]
arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
print(sort_012(arr))  # Output: [0, 0, 0,   0, 0, 1, 1, 1, 1, 1, 2, 2]


# Learning in this challenge:
  # - we can learn how to count the occurrences of a specific value in a list using the count() method
  # eg. arr.count(0) will give us the number of times 0 appears in the list arr
  # - we can learn how to create a new list by concatenating multiple lists using the + operator
  # eg. [0] * count_0 + [1] * count_1
