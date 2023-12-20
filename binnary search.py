def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Element found, return its index
        elif arr[mid] < target:
            low = mid + 1  # Search the right half of the array
        else:
            high = mid - 1  # Search the left half of the array

    return -1  # Element not found

# Example usage:
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 1
result = binary_search(array, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the array.")

