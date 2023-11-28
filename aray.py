a = []
ya = int(input("Masukkan jumlah elemen: "))

for i in range(1, ya + 1):
    masuk = int(input(f"Masukkan Nilai A[{i}]: "))
    a.append(masuk)

print("\nArray:")
for i in range(1, ya + 1):
    print(f"A[{i}] : {a[i - 1]}")

total_nilai = sum(a)
hasil = total_nilai / ya
print(f"Rata - ratanya adalah : {hasil}")
