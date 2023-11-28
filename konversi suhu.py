import sec_konversi_suhu
import os
import time
from colorama import init, Fore, Style
import getpass
init()

def animasi_text(color, text):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(0.01)

def submenu():
    while True:
        try:
            os.system('cls')
            hastag  ="""\n##################"""
            tengah  ="""\n== Menu Pilihan =="""
            submenu ="""\n\n1.Kembali Ke Aplikasi\n2.Keluar"""
            animasi_text(Fore.BLUE,hastag)
            animasi_text(Fore.BLUE,tengah)
            animasi_text(Fore.BLUE,hastag)
            time.sleep(0.5)
            animasi_text(Fore.YELLOW,submenu)
            pilihansubmenu = int(input("\n\nPilihan : "))
            

            if pilihansubmenu == 1:
                os.system("cls")
                return

            elif pilihansubmenu == 2:
                os.system("cls")
                print("Dadah :)")
                exit()
            else:
                os.system("cls")
                print("Masukkan harus berupa angka valid. Coba lagi.")

        except ValueError:
            os.system("cls")
            print("Masukkan harus berupa angka valid. Coba lagi.")
            continue


def menuawal():
    while True:
        try:
            header = """============== ||  Menu Konversi Suhu  || ==============\n"""
            menu_text = """1. Celsius ke Farenheit\n2. Celsius ke Reamur\n3. Celsius ke Kelvin\n4. Keluar Gais\n"""
            animasi_text(Fore.YELLOW, header)
            time.sleep(0.5)
            animasi_text(Style.RESET_ALL, menu_text)
                
            menu = int(input("Pilihan : "))


        except ValueError:
            os.system("cls")
            print(Fore.YELLOW + "Masukkan harus berupa angka valid. Coba lagi.")
            continue

        if menu == 1:
            os.system("cls")
            sec_konversi_suhu.C_ke_F()
            getpass.getpass("Pencet enter untuk lanjut...")
            submenu()

        elif menu == 2:
            os.system("cls")
            sec_konversi_suhu.C_ke_R()
            getpass.getpass("Pencet enter untuk lanjut...")
            submenu()

        elif menu == 3:
            os.system("cls")
            sec_konversi_suhu.C_ke_k()
            getpass.getpass("Pencet enter untuk lanjut...")
            submenu()

        elif menu == 4:
            os.system("cls")
            print("Babay :)")
            exit()

        else:
            os.system("cls")
            print("Masukkan harus berupa angka. Coba lagi.")


if __name__ == "__main__":
    menuawal()
