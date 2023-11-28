a = []
jumlah_angka = int(input("Masukkan banyak angka: "))

for i in range(1, jumlah_angka + 1):
    masukkan_angka = int(input(f"Masukkan angka ke-{i}: "))
    a.append(masukkan_angka)

lima = []
for i, angka in enumerate(a, start=1):
    if angka == 5:
        lima.append(i)

print("")
print(f"Jumlah Inputan 5 ada        : {len(lima)}")
print(f"Array Berisi angka 5 ada di : {', '.join(map(str, lima))}")
