# Array Insertion
# Given an array, a value to insert into the array, and an index to insert the value at, 
# return a new array with the value inserted at the specified index.

# For example, given the array [1, 2, 3], the value 10, and the index 1, return [1, 10, 2, 3].
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-10
def array_insertion(arr, value, index):
    return arr[:index] + [value] + arr[index:]


print(array_insertion([1, 2, 3], 10, 1))  # Output: [1, 10, 2, 3]