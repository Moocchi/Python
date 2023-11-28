import msvcrt
import os

def wait_for_key():
    print("Press any key to continue...")
    msvcrt.getch()

while True:
    menu = int(input("=================================\n"
                     "+       Belajar Menggambar      +\n"
                     "=================================\n\n"
                     "Menu :\n"
                     "1. Trapesium\n"
                     "2. Gambar M\n"
                     "3. Keluar\n\n"
                     "Pilihan : "))

    if menu == 1:
        os.system('cls')
        print("===================================")
        print("+       Menggambar Trapesium      +")
        print("===================================")
        c = int(input("Input Angka yang Diinginkan: "))
        pattern = ""
        for b in range(1, c):
            for a in range(c - 2, b - 1, -1):
                pattern += "   "
            for a in range(b + 1):
                pattern += " * "
            for a in range(c, 0, -1):
                pattern += " ^ "
            for a in range(b + 1):
                pattern += " * "
            pattern += "\n"
        
        print(pattern)
        wait_for_key()
    
    
    elif menu == 2:
        os.system('cls')
        print("=================================")
        print("+       Menggambar Huruf M      +")
        print("=================================")
        tinggi = int(input("Masukkan tinggi huruf M: "))
        pattern = ""
        for i in range(tinggi):
            for j in range(tinggi * 2 - 1):
                if j == 0 or j == tinggi * 2 - 2 or (i == j and j <= tinggi - 1) or (j == tinggi * 2 - 2 - i and j >= tinggi):
                    pattern += "*"
                else:
                    pattern += " "
            pattern += "\n"

        print(pattern)
        wait_for_key()
    
    elif menu == 3:
        print("Dadah Gais :)")
        break

    else:
        print("HEHE:3")
