jumlah_angka = int(input("Masukan Jumlah Angka Yang Diinginkan: "))
angka_list = []

for i in range(jumlah_angka):
    angka = int(input(f"Masukan Angka ke-{i}: "))
    angka_list.append(angka)

rerata = sum(angka_list) / jumlah_angka
print(f"\nRerata: {rerata}\n")

angka_list.sort()

print("Setelah Diurutkan:")
new_line_printed = False

for i, angka in enumerate(angka_list):
    if angka > rerata and not new_line_printed:
        print("\n------------------------------")
        new_line_printed = True

    print(f"angka ke-{i} : {angka}")
