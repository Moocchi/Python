import os
import time
from colorama import init, Fore, Style
init()

def animasi_text(color, text):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(0.01)

def rata_rata():
    a = []
    os.system('cls')
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

def nilai_genap():
    a = []

    os.system('cls')
    jumlah_angka = int(input("Masukkan banyak angka: ")) 

    for i in range(1, jumlah_angka + 1):
        masukkan_angka = int(input(f"Masukkan angka ke-{i}: "))
        a.append(masukkan_angka)

    genap = []

    for i, angka in enumerate(a, start=1):
        if angka % 2 == 0:
            genap.append(angka)
            print(f"Genap array ke-{i} adalah: {angka}")

def banyak_5():
    a = []

    os.system('cls')
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

def min_max():
    a = []

    os.system('cls')
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

header = "========== Selamat datang ==========\n"
menu = '''\n1. Rata - Rata\n2. Nilai Genap\n3. Banyak 5\n4. Min Max\n5. Keluar\n'''
os.system('cls')
animasi_text(Fore.YELLOW, header)
time.sleep(0.5)
animasi_text(Fore.GREEN, menu)
pilihan = int(input("\nMassukan pilihan : "))

if pilihan == 1:
    rata_rata()
elif pilihan == 2:
    nilai_genap()
elif pilihan == 3:
    banyak_5()
elif pilihan == 4:
    min_max()
elif pilihan == 5:
    os.system('cls')
    print("Makasih mas")
    exit()
else:
    os.system('cls')
    print("salah bejir")
