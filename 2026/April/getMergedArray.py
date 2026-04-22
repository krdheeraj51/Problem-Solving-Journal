def mergedArray(arr1, arr2):
    mergedArray = []
    mergedArray.extend(arr1)
    mergedArray.extend(arr2)

    return mergedArray

# Example usage:
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
print(mergedArray(arr1, arr2))  # Output: [1, 2, 3, 4, 5, 6]

