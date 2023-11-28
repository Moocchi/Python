def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# Get user input for the array
try:
    n = int(input("Enter the number of elements (max 10): "))
    if n > 10 or n <= 0:
        raise ValueError("Number of elements should be between 1 and 10.")
except ValueError as e:
    print(f"Error: {e}")
    exit()

arr = []
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

# Print the unsorted array
print("Unsorted Array:", arr.copy())

# Perform quick sort
arr = quick_sort(arr)

# Print the sorted array
print("Sorted Array:", arr)
