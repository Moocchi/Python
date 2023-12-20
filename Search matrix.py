import os

def print_matrix(matrix):
    print("Matrix:")
    for i in range(3):
        for j in range(3):
            print(matrix[i * 3 + j], end=" ")
        print()

def input_matrix():
    matrix = []
    for i in range(3):
        row = []
        for j in range(3):
            value = int(input(f"Masukkan nilai untuk baris {i + 1}, kolom {j + 1}: "))
            row.append(value)
        matrix.extend(row)
    return matrix

os.system('cls')

while True:
    matrix = input_matrix()
    os.system('cls')
    print_matrix(matrix)

    cari = int(input("\nCari Angka : "))
    
    found_indices = [index for index, value in enumerate(matrix) if value == cari]

    if found_indices:
        print(f"\nNilai {cari} ditemukan di:")
        for index in found_indices:
            row = index // 3
            col = index % 3
            print(f"Baris {row + 1}, kolom {col + 1}")
        break
    else:
        print(f"\nNilai {cari} tidak ditemukan dalam matriks.")
        break
