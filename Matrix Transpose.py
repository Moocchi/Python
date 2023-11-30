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

def transpose_matriks(matriks):
    return [[matriks[j][i] for j in range(len(matriks))] for i in range(len(matriks[0]))]

def tampilkan_matriks(matriks):
    for baris in matriks:
        print(baris)

def main():
    
    os.system('cls')
    jumlah_baris = int(input("Masukkan jumlah baris untuk Matriks: "))
    jumlah_kolom = int(input("Masukkan jumlah kolom untuk Matriks: "))

    print("\nMatriks:")
    matriks = ambil_matriks_dari_pengguna(jumlah_baris, jumlah_kolom)

    hasil_transpose = transpose_matriks(matriks)

    print("\nMatriks:")
    tampilkan_matriks(matriks)

    print("\nTranspose Matriks:")
    tampilkan_matriks(hasil_transpose)

if __name__ == "__main__":
    main()
