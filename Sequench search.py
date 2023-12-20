def sequential_search(arr, target1, target2):
    index_of_target1 = None
    index_of_target2 = None

    for index, element in enumerate(arr):
        if element == target1:
            index_of_target1 = index
        elif element == target2:
            index_of_target2 = index

        if index_of_target1 is not None and index_of_target2 is not None:
            break

    return index_of_target1, index_of_target2

array = [10, 23, 18, 21, 25, 30]

element1 = 18
element2 = 21

result1, result2 = sequential_search(array, element1, element2)

if result1 is not None:
    print(f"The element {element1} is found at index {result1}.")
else:
    print(f"The element {element1} is not present in the array.")

if result2 is not None:
    print(f"The element {element2} is found at index {result2}.")
else:
    print(f"The element {element2} is not present in the array.")
