import os

def ambil_matriks_dari_pengguna(jumlah_baris, jumlah_kolom):
    matriks = []
    print(f"\nMasukkan nilai untuk matriks {jumlah_baris}x{jumlah_kolom}:")
    for i in range(jumlah_baris):
        baris = []
        for j in range(jumlah_kolom):
            nilai = int(input(f"Masukkan nilai untuk elemen ({i+1},{j+1}): "))
            baris.append(nilai)
        matriks.append(baris)
    return matriks

def kurangi_matriks(matriks1, matriks2):
    hasil = []
    for i in range(len(matriks1)):
        baris = [matriks1[i][j] - matriks2[i][j] for j in range(len(matriks1[0]))]
        hasil.append(baris)
    return hasil

def tampilkan_matriks(matriks):
    for baris in matriks:
        print(baris)

def main():
    
    os.system('cls')
    jumlah_baris1 = int(input("Masukkan jumlah baris untuk Matriks 1: "))
    jumlah_kolom1 = int(input("Masukkan jumlah kolom untuk Matriks 1: "))

    jumlah_baris2 = int(input("\nMasukkan jumlah baris untuk Matriks 2: "))
    jumlah_kolom2 = int(input("Masukkan jumlah kolom untuk Matriks 2: "))

    if jumlah_baris1 != jumlah_baris2 or jumlah_kolom1 != jumlah_kolom2:
        print("Matriks tidak dapat dikurangkan. Dimensi berbeda.")
        return

    print("\nMatriks 1:")
    matriks1 = ambil_matriks_dari_pengguna(jumlah_baris1, jumlah_kolom1)

    print("\nMatriks 2:")
    matriks2 = ambil_matriks_dari_pengguna(jumlah_baris2, jumlah_kolom2)

    hasil_matriks = kurangi_matriks(matriks1, matriks2)

    print("\nMatriks 1:")
    tampilkan_matriks(matriks1)

    print("\n-")

    print("\nMatriks 2:")
    tampilkan_matriks(matriks2)

    print("\nHasil Pengurangan Matriks:")
    tampilkan_matriks(hasil_matriks)

if __name__ == "__main__":
    main()
