# Pascal's Triangle Row
# Given an integer n, return the nth row of Pascal's triangle as an array.

# In Pascal's Triangle, each row begins and ends with 1, and each interior value is the sum of the two values directly above it.

# Here's the first 5 rows of the triangle:

def pascal_row(n):
    if n == 0:
        return [1]
    
    row = [1]
    for i in range(1, n + 1):
        row.append(row[i - 1] * (n - i + 1) // i)
    
    return row
print(pascal_row(5))  # Output: [1]
# print(pascal_row(1))  # Output: [1, 1]
# print(pascal_row(2))  # Output: [1, 2, 1]
# print(pascal_row(3))  # Output: [1, 3, 3, 1]
# print(pascal_row(4))  # Output: [1, 4, 6, 4, 1]