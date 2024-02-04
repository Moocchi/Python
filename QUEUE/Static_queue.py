MAX_LOKET = 5
isi_loket = [[] for _ in range(MAX_LOKET)]

def tambah_antrian():
    nomor_loket = int(input("Masukkan nomor loket (1-5): "))
    
    if 1 <= nomor_loket <= MAX_LOKET:
        nama_pelanggan = input("Masukkan nama pelanggan: ")
        isi_loket[nomor_loket - 1].append(nama_pelanggan)
        print(f"Antrian berhasil ditambahkan di loket {nomor_loket}")
    else:
        print("Nomor loket tidak valid")

def hapus_antrian():
    nomor_loket = int(input("Masukkan nomor loket (1-5): "))

    if 1 <= nomor_loket <= MAX_LOKET:
        if isi_loket[nomor_loket - 1]:
            removed_pelanggan = isi_loket[nomor_loket - 1].pop(0)
            print(f"Antrian {removed_pelanggan} di loket {nomor_loket} berhasil dihapus")
        else:
            print(f"Loket {nomor_loket} tidak memiliki antrian")
            time.sleep(1)
            
    else:
        print("Nomor loket tidak valid")
        time.sleep(1)

def status_loket():
    for i in range(1, MAX_LOKET + 1):
        print(f"Loket [{i}]: ", end="")
        if not isi_loket[i - 1]:
            print("Tidak ada antrian")
        else:
            print(", ".join(isi_loket[i - 1]))
            antrian_loket = len(isi_loket[i - 1])
            print(f"Banyaknya antrian di loket: {antrian_loket}")


def main():
    while True:
        os.system('cls')
        status_loket()
        
        print("\n1. Tambah Antrian\n2. Hapus antrian\n3. Exit")
        pilihan = int(input("\nPilihan : "))

        if pilihan == 1:
            tambah_antrian()
        elif pilihan == 2:
            hapus_antrian()
        elif pilihan == 3:
            os.system('cls')
            print("MP")
            exit()
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    import time
    import os
    main()
