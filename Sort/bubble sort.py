import os
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

arr = []
while len(arr) < 10:
    element = input(f"Massukan angka sampai (10) Array ke {len(arr) + 1} (atau pencet 'q' untuk selesai): ")
    if element.lower() == 'q':
        break
    try:
        num = int(element)
        arr.append(num)
    except ValueError:
        print("Input invalid. Massukan nomor atau 'q' untuk selesai.")

if len(arr) > 0 :
    os.system('cls')
    print("Array Asli    :", arr)
    bubble_sort(arr)
    print("Array Terurut :", arr)
else:
    print("Tidak ada input yang dimasukkan :(.keluar program")
