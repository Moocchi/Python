import os

class BankAccount:
    def __init__(self, no_rek, initial_balance=50000):
        self.no_rek = no_rek
        self.balance = initial_balance

def tarik_tunai(account):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=============================")
    print("==========TARIK TUNAI==========")
    print("=============================\n")

    print("Tarik tunai dalam kelipatan 50000\n")

    while True:
        try:
            tarikan = int(input("Masukkan jumlah tarikan: "))
            if tarikan % 50000 == 0 and tarikan > 0:
                if tarikan <= account.balance:
                    account.balance -= tarikan
                    print("\nTarik tunai berhasil !")
                    print(f"---------------------------------------")
                    print(f"Saldo saat ini: {account.balance}")
                else:
                    print("\nSaldo tidak mencukupi untuk tarik tunai.")
                    print(f"saldo anda : {account.balance} ")
            elif tarikan <= 0:
                print("Masukkan jumlah tarikan yang valid (harus lebih dari 0).\n")
            else:
                print("\nJumlah tarikan harus dalam kelipatan 50000.\n")
        except ValueError:
            print("\nMasukkan jumlah tarikan yang valid (angka).")

        print("\n---------------------------------------\n")
        print("Apakah ingin tarik tunai lagi atau kembali ke menu ?")
        konfirmasi = input("\nMasukkan pilihan (Y/N) : ")

        if konfirmasi.lower() == "y":
            os.system('cls')
            print("\n")
            continue
        elif konfirmasi.lower() == "n":
            # Continue with the rest of your program logic here
            break


def nabung(account):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=============================")
    print("============NABUNG===========")
    print("=============================\n")

    try:
        deposit_amount = int(input("Masukkan jumlah yang ingin ditabung: "))
        if deposit_amount > 0:
            account.balance += deposit_amount
            print(f"\nTabungan berhasil!")
            print("---------------------")
            print(f"No. rek       : {account.no_rek}   ")
            print(f"Saldo saat ini: {account.balance}\n")
        else:
            print("Masukkan jumlah yang valid (harus lebih dari 0).")
    except ValueError:
        print("Masukkan jumlah yang valid (angka).")
    
    os.system('pause')

def sumpah():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('"Dengan menyebut nama ALLAH, Saya Muhammad Jarez bersumpah bahwa saya tidak melakukan kecurangan')
    print('Mencontek ataupun memberikan contekan selama UAS Algoritma dan pemrogaman berlangsung, jika pengawas')
    print('menemukan saya melakukan kecurangan maka saya siap mendapatkan nilai 0 pada UAS, dan apabila kecurangan saya tidak diketahui')
    print('oleh pengawas maka saya siap mendapatkan azab dari ALLAH baik di dunia maupun di akhirat kelak"\n')

def transfer(account):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=============================")
    print("===========TRANSFER==========")
    print("=============================\n")
    
    print("Masukkan rekening tujuan serta nominal !\n")

    while True:
        tujuan = input("Masukkan No. Rekening : ")

        if len(tujuan) > 10:
            os.system('cls')
            print("Nomor rekening tidak valid. Harap masukkan nomor rekening dengan maksimal 10 karakter.\n")
        else:
            break

    nominal = int(input("Masukkan nominal      : "))

    # Check if there is enough balance for the transfer
    if nominal > account.balance:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nTransfer di batalkan, Nominal tidak cukup\n")
        print(f"Saldo anda : {account.balance}\n")
        os.system('pause')
        return  # Exit the function without modifying the balance

    account.balance -= nominal

    print("\n------------------------------------------\n")
    print("Konfirmasi : \n")
    print(f"No. Rekening Tujuan : {tujuan}")
    print(f"Nominal             : {nominal}")

    konfirmasi = input("\nKonfirmasi (Y/N) ? : ")

    if konfirmasi.lower() == "y":
        print("------------------------------------")
        print("\nTransfer Berhasil !\n")
        print(f"Saldo saat ini: {account.balance}\n")
        os.system('pause')
    elif konfirmasi.lower() == "n":
        print("\n---------------------------------------\n")
        print("Apakah ingin input ulang atau kembali ke menu ?")
        konfirmasi_1 = input("\nMasukkan pilihan (Y/N) : ")
        
        if konfirmasi_1.lower() == "y":
            # Restore the balance if the transfer is canceled
            account.balance += nominal
            transfer(account)
        elif konfirmasi_1.lower() == "n":
            # Continue with the rest of your program logic here
            pass


def lihat_saldo(account):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=============================")
    print("=========LIHAT SALDO==========")
    print("=============================\n")
    print(f"Saldo saat ini: {account.balance}\n")

# Example usage:
account_number = "1211813272"
account = BankAccount(no_rek=account_number, initial_balance=5000)


while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=======================================")
    print("=========PROGRAM SIMULASI BANK=========")
    print("=======================================")
    print("\nPilih Menu :")
    print("1. Sumpah\n2. Transfer\n3. Nabung\n4. Tarik Tunai\n5. Lihat Saldo\n6. EXIT")
    
    try:
        pilihan = int(input("\nPilihan : "))
    except ValueError:
        print("Masukkan angka sebagai pilihan.")
        continue

    if pilihan == 1:
        sumpah()
        os.system("pause")
    elif pilihan == 2:
        transfer(account)
    elif pilihan == 3:
        nabung(account)
    elif pilihan == 4:
        tarik_tunai(account)
    elif pilihan == 5:
        lihat_saldo(account)
        os.system("pause")
    elif pilihan == 6:
        exit()
    else:
        print("Pilihan tidak valid !")
