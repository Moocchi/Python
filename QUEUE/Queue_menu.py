MAX_NAMA = 50
MAX_ANTRIAN = 10

class Antrian:
    def __init__(self):
        self.nomorAntrian = 0
        self.nama = ""

class AntrianQueue:
    def __init__(self):
        self.antrian = [Antrian() for _ in range(MAX_ANTRIAN)]
        self.jumlahAntrian = 0

def tambahAntrian(antrianQueue):
    if antrianQueue.jumlahAntrian < MAX_ANTRIAN:
        newAntrian = Antrian()
        newAntrian.nomorAntrian = antrianQueue.jumlahAntrian + 1

        print(f"No. Antrian Anda: {newAntrian.nomorAntrian}")
        newAntrian.nama = input("Masukkan Nama Anda: ")

        antrianQueue.antrian[antrianQueue.jumlahAntrian] = newAntrian
        antrianQueue.jumlahAntrian += 1

        print("Antrian berhasil ditambahkan!")
        input("Press Enter to continue...")

    else:
        print("Antrian penuh. Tidak dapat menambahkan antrian baru.")
        input("Press Enter to continue...")

def hapusAntrian(antrianQueue):
    if antrianQueue.jumlahAntrian > 0:
        print(f"Antrian nomor {antrianQueue.antrian[0].nomorAntrian} dengan nama {antrianQueue.antrian[0].nama} telah dihapus.")

        # Geser antrian ke depan setelah menghapus
        for i in range(antrianQueue.jumlahAntrian - 1):
            antrianQueue.antrian[i] = antrianQueue.antrian[i + 1]
        antrianQueue.jumlahAntrian -= 1

        input("Press Enter to continue...")
    else:
        print("Antrian kosong. Tidak ada antrian untuk dihapus.")
        input("Press Enter to continue...")

def cetakAntrian(antrianQueue):
    print("------- Daftar Antrian -------")
    if antrianQueue.jumlahAntrian == 0:
        print("Antrian Masih Kosong :( ")
        input("Press Enter to continue...")
    else:
        for i in range(antrianQueue.jumlahAntrian):
            print(f"No. Antrian  : {antrianQueue.antrian[i].nomorAntrian}")
            print(f"Nama         : {antrianQueue.antrian[i].nama}")
            print("----------------------------")
        input("Press Enter to continue...")

def main():
    antrianQueue = AntrianQueue()

    pilihan = 0

    while pilihan != 4:
        print("===== Menu =====")
        print("1. Tambah Antrian")
        print("2. Hapus Antrian")
        print("3. Cetak Antrian")
        print("4. Keluar\n")
        pilihan = int(input("Pilihan: "))

        if pilihan == 1:
            tambahAntrian(antrianQueue)
        elif pilihan == 2:
            hapusAntrian(antrianQueue)
        elif pilihan == 3:
            cetakAntrian(antrianQueue)
        elif pilihan == 4:
            print("Keluar dari program.")
        else:
            print("Pilihan tidak valid. Silakan masukkan opsi yang benar.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
