import os

nama_i = []

os.system('cls')
nama = int(input("Masukkan Jumlah : "))

for i in range(nama):
    kata = input("Masukkan Kata : ")
    nama_i.append(kata)

print("\nHasil Sorting :")

for i in range(1, len(nama_i)):
    key = nama_i[i]
    j = i - 1
    while j >= 0 and key < nama_i[j]:
        nama_i[j + 1] = nama_i[j]
        j -= 1
    nama_i[j + 1] = key

nama_dict = {}

for nama in nama_i:
    first_letter = nama[0].upper()
    if first_letter not in nama_dict:
        nama_dict[first_letter] = [nama]
    else:
        nama_dict[first_letter].append(nama)

for letter, names in nama_dict.items():
    print(f"\n{letter}: {', '.join(names)}")
    print("-------------------")
