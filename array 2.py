a = []

jumlah_angka = int(input("Masukkan banyak angka: ")) 

for i in range(1, jumlah_angka + 1):
    masukkan_angka = int(input(f"Masukkan angka ke-{i}: "))
    a.append(masukkan_angka)

genap = []

for i, angka in enumerate(a, start=1):
    if angka % 2 == 0:
        genap.append(angka)
        print(f"Genap array ke-{i} adalah: {angka}")
