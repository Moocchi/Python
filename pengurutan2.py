def printKelas(classNumber, arr):
    print("\nKelas X-{} :\n".format(classNumber))
    n = len(arr) // 2
    for i in range(n):
        print("{} | {}".format(arr[i * 2], arr[i * 2 + 1]))

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Step 1: Input Kelas and Data
kelas = int(input("Masukkan Banyak Kelas : "))
data = int(input("Masukkan Banyak Data  : "))
total_data = data * 2

# Step 2: Input Data
a_data = []
for i in range(total_data):
    masuk = int(input("Masukkan Data ke-{} : ".format(i + 1)))
    a_data.append(masuk)

# Step 3: Sorting Data
selection_sort(a_data)

# Step 4: Print Kelas
n = len(a_data) // 2
for i in range(kelas):
    start_idx = i * n // kelas
    end_idx = (i + 1) * n // kelas
    printKelas(i + 1, a_data[start_idx * 2:end_idx * 2])
