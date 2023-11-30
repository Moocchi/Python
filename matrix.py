import os

def buat_matriks(jumlah_baris, jumlah_kolom):
    matriks = []
    for i in range(jumlah_baris):
        baris = []
        for j in range(jumlah_kolom):
            nilai = int(input(f"\nMasukkan nilai untuk baris {i + 1}, kolom {j + 1}: "))
            baris.append(nilai)
        matriks.append(baris)
    return matriks

def tampilkan_matriks(matriks):
    for baris in matriks:
        print(baris)

def main():
    os.system('cls')
    jumlah_baris = int(input("Masukkan jumlah baris: "))
    jumlah_kolom = int(input("Masukkan jumlah kolom: "))

    matriks_pengguna = buat_matriks(jumlah_baris, jumlah_kolom)

    print("\nMatriks Anda:")
    tampilkan_matriks(matriks_pengguna)

if __name__ == "__main__":
    main()
