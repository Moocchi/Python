def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

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

# Perform selection sort
selection_sort(arr)

# Print the sorted array
print("Sorted Array:", arr)
