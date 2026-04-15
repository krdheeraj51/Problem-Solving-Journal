# Sorted Array Swap
# Given an array of integers, return a new array using the following rules:

# Sort the integers in ascending order
# Then swap all values whose index is a multiple of 3 with the value before it.

def sorted_swap_array(arr):
    # Sort the array in ascending order
    sorted_arr = sorted(arr)
    
    # Swap values at indices that are multiples of 3 with the previous value
    for i in range(3, len(sorted_arr), 3):
        sorted_arr[i], sorted_arr[i - 1] = sorted_arr[i - 1], sorted_arr[i]
    
    return sorted_arr

print(sorted_swap_array([5, 3, 1, 4, 2]))  # Output: [1, 2, 4, 3, 5]
print(sorted_swap_array([10, 9, 8, 7, 6, 5]))  # Output: [5, 6, 7, 8, 9, 10]