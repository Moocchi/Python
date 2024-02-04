MAX_NAMA = 50
MAX_ANTRIAN = 10

class Antrian:
    def __init__(self):
        self.nomorAntrian = 0
        self.nama = ""
        self.eksekutor = ""

class Barber:
    def __init__(self):
        self.antrian = [Antrian() for _ in range(MAX_ANTRIAN)]
        self.jumlahAntrian = 0
        self.pendapatan = [0, 0, 0]  # Pendapatan dari eksekutor Ganyu, Hu Tao, Xianling
        self.pendapatanMitra = 0  # Pendapatan dari Mitra

def tampilkanHeader():
    print("-------------------------------\n\n")
    print("\t Barber Ganyu")
    print("    Jl. Liyue Block I No. 12\n\n")
    print("-------------------------------")

def tampilkanMenu():
    print("      -------MENU-------")
    print("\n1. Daftar antrian\n2. Hapus\n3. Daftar Tunggu\n4. Pendapatan\n5. Keluar")
    print("\n-------------------------------")

def tambahAntrian(barber, nama):
    if barber.jumlahAntrian < MAX_ANTRIAN:
        newAntrian = Antrian()

        # Mencari nomor antrian tertinggi
        nomorTertinggi = max(antrian.nomorAntrian for antrian in barber.antrian) if barber.jumlahAntrian > 0 else 0

        newAntrian.nomorAntrian = nomorTertinggi + 1
        newAntrian.nama = nama

        # Set eksekutor berdasarkan urutan antrian
        if newAntrian.nomorAntrian % 3 == 1:
            newAntrian.eksekutor = "Ganyu"
        elif newAntrian.nomorAntrian % 3 == 2:
            newAntrian.eksekutor = "Hu Tao"
        else:
            newAntrian.eksekutor = "Xianling"

        barber.antrian[barber.jumlahAntrian] = newAntrian
        barber.jumlahAntrian += 1

        print(f"\nNo. Antrian : {newAntrian.nomorAntrian}")
        print(f"Nama        : {newAntrian.nama}\n")

    else:
        print("Antrian penuh. Tidak dapat menambahkan antrian baru.")

def hapusAntrian(barber):
    if barber.jumlahAntrian > 0:
        # Menampilkan daftar eksekutor
        print("Eksekutor :")
        print("1. Ganyu")
        print("2. Hu Tao")
        print("3. Xianling\n")

        pilihanEksekutor = int(input("Pilihan Eksekutor: "))

        if 1 <= pilihanEksekutor <= 3:
            # Menyimpan data antrian yang akan dihapus
            removedAntrian = barber.antrian[0]

            # Menampilkan informasi antrian yang akan dihapus
            print("\n-------------------------------")
            print(f"No. Antrian : {removedAntrian.nomorAntrian}")
            print(f"Nama        : {removedAntrian.nama}")

            # Menentukan eksekutor berdasarkan pilihan
            targetEksekutor = ""
            if pilihanEksekutor == 1:
                targetEksekutor = "Ganyu"
            elif pilihanEksekutor == 2:
                targetEksekutor = "Hu Tao"
            else:
                targetEksekutor = "Xianling"

            print(f"Eksekutor   : {targetEksekutor}")
            print("-------------------------------")

            # Perbarui pendapatan eksekutor
            if targetEksekutor == "Ganyu":
                barber.pendapatan[0] += 12000
                barber.pendapatanMitra += 8000
            elif targetEksekutor == "Hu Tao":
                barber.pendapatan[1] += 12000
                barber.pendapatanMitra += 8000
            elif targetEksekutor == "Xianling":
                barber.pendapatan[2] += 12000
                barber.pendapatanMitra += 8000

            # Geser antrian ke depan setelah menghapus
            for i in range(barber.jumlahAntrian - 1):
                barber.antrian[i] = barber.antrian[i + 1]
                # Perbarui nomor antrian setelah penghapusan
                barber.antrian[i].nomorAntrian = i + 1

            barber.jumlahAntrian -= 1

            print(f"\nAntrian dengan nomor {removedAntrian.nomorAntrian} telah dihapus oleh eksekutor {targetEksekutor}.\n")

        else:
            print("Pilihan eksekutor tidak valid.\n")
    else:
        print("Antrian kosong. Tidak ada antrian untuk dihapus.\n")

def daftarTunggu(barber):
    print("------- Data Antrian -------\n")
    if barber.jumlahAntrian == 0:
        print("Antrian Masih Kosong :(\n")
    else:
        for i in range(barber.jumlahAntrian):
            print(f"No. Antrian  : {barber.antrian[i].nomorAntrian}")
            print(f"Nama         : {barber.antrian[i].nama}")

            # Perhitungan sisa antrian
            sisaAntrian = barber.jumlahAntrian - i - 1
            print(f"Sisa Antrian : {sisaAntrian}")
            print("----------------------------\n")


def tampilkanPendapatan(barber):
    print("-------- Pendapatan --------")
    print(f"keuntungan Mitra        :Rp. {barber.pendapatanMitra},-")
    print(f"- Ganyu                 :Rp. {barber.pendapatan[0]},-")
    print(f"- Hu Tao                :Rp. {barber.pendapatan[1]},-")
    print(f"- Xianling              :Rp. {barber.pendapatan[2]},-")
    print("----------------------------\n")

def main():
    barber = Barber()
    barber.jumlahAntrian = 0
    barber.pendapatan[0] = 0  # Pendapatan Ganyu
    barber.pendapatan[1] = 0  # Pendapatan Hu Tao
    barber.pendapatan[2] = 0  # Pendapatan Xianling
    barber.pendapatanMitra = 0  # Pendapatan Mitra

    menu = 0
    nama = ""

    while menu != 5:
        os.system('cls')
        tampilkanHeader()
        tampilkanMenu()

        menu = int(input("Masukkan Pilihan: "))
        os.system('cls')

        if menu == 1:
            os.system('cls')
            print("Massukan Nama \n")
            nama = input("Nama : ")
            tambahAntrian(barber, nama)

        elif menu == 2:
            hapusAntrian(barber)

        elif menu == 3:
            daftarTunggu(barber)

        elif menu == 4:
            tampilkanPendapatan(barber)

        elif menu == 5:
            print("Keluar dari program.\n")

        else:
            print("Opsi tidak valid. Silakan masukkan opsi yang benar.\n")

        input("Tekan Enter untuk melanjutkan...")
        os.system('cls')

if __name__ == "__main__":
    import os
    main()
