import os

def main():
    while True:
        os.system("clear")
        print("\n===Selamat Datang===\n\n")
        print("1. Menghitung Rata-Rata Bilangan Genap\n")
        print("2. Menghitung Bintang Angka\n")
        print("3. Menghitung Kardus Keluar\n")
        print("4. Keluar\n")

        menu = int(input("\nMasukkan Pilihan : "))

        if menu == 1:
            os.system('cls')
            print("===========================\n")
            print("Menghitung Rata-Rata Bilangan Genap\n")
            print("===========================\n\n")

            jumlah_bilangan = int(input("Masukkan jumlah bilangan (maksimum 10): "))

            if jumlah_bilangan <= 0 or jumlah_bilangan > 10:
                print("Jumlah bilangan harus lebih dari 0 dan tidak lebih dari 10.")
                input("Press Enter to continue...")
                continue

            sum_genap = 0
            jumlah_genap = 0

            for i in range(jumlah_bilangan):
                bilangan = float(input(f"Bilangan ke-{i + 1}: "))
                if int(bilangan) % 2 == 0:
                    sum_genap += bilangan
                    jumlah_genap += 1

            if jumlah_genap > 0:
                rata_rata = sum_genap / jumlah_genap
                print(f"Rata-rata bilangan genap dari {jumlah_genap} bilangan tersebut adalah: {rata_rata}")
            else:
                print("Tidak ada bilangan genap.")

            pilihan = input("\nKembali ke menu utama (y/n) ? : ")
            if pilihan.lower() != 'y':
                break

        elif menu == 2:
            n = int(input("Masukkan jumlah baris: "))
            total_sum = 0

            for i in range(1, n + 1):
                row_sum = sum(range(1, i + 1))
                total_sum += row_sum
                print(f"{' + '.join(map(str, range(1, i + 1)))} = {row_sum}")

            print(f"\nJumlah keseluruhan: {total_sum}")

            pilihan = input("\nKembali ke menu utama (y/n) ? : ")
            if pilihan.lower() != 'y':
                break

        elif menu == 3:
            os.system("clear")
            print("===Menghitung Kardus keluar pak gehu===\n")

            jumlah_bakwan = int(input("Jumlah bakwan pak engkus        : "))
            jumlah_gehu = int(input("Jumlah gehu pak engkus          : "))
            jumlah_pisgor = int(input("Jumlah pisang goreng pak engkus : "))

            maksimum_bakwan = 20
            maksimum_gehu = 15
            maksimum_pisgor = 25

            kardus_bakwan = (jumlah_bakwan + maksimum_bakwan - 1) // maksimum_bakwan
            kardus_gehu = (jumlah_gehu + maksimum_gehu - 1) // maksimum_gehu
            kardus_pisgor = (jumlah_pisgor + maksimum_pisgor - 1) // maksimum_pisgor

            total_kardus = kardus_bakwan + kardus_gehu + kardus_pisgor

            print("\nTotal kardus yang dibutuhkan:")
            print(f"Bakwan   : {kardus_bakwan} kardus ({jumlah_bakwan} bakwan)")
            print(f"Gehu     : {kardus_gehu} kardus ({jumlah_gehu} gehu)")
            print(f"Pisgor   : {kardus_pisgor} kardus ({jumlah_pisgor} pisgor)")
            print("-------------------")
            print(f"Total    : {total_kardus} kardus")

            pilihan = input("\nKembali ke menu utama (y/n) ? : ")
            if pilihan.lower() != 'y':
                break

        elif menu == 4:
            os.system("clear")
            print("Dadah :)")
            break

if __name__ == "__main__":
    main()
