a = []
jumlah_angka = int(input("Masukkan banyak angka: "))

for i in range(1, jumlah_angka + 1):
    masukkan_angka = int(input(f"Masukkan angka ke-{i}: "))
    a.append(masukkan_angka)

besar = max(a)
kecil = min(a)

print("")
print(a)
print(f"Nilai Maximum nya adalah : {besar}")
print(f"Nilai Minimum nya adalah : {kecil}")
