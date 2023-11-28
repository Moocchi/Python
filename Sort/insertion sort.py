def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

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

# Perform insertion sort
insertion_sort(arr)

# Print the sorted array
print("Sorted Array:", arr)