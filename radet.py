import math 

def luas_persegi():
    sisi = int(input("Massukan sisi : "))

    luas = sisi*sisi

    print (f"luasnya adalah : {luas}")

def luas_lingkaran():
    r = float(input('Massukan Jari-Jari : '))

    luas_l = math.pi*r**2

    print(f"Luasnya adalah : {luas_l}")

def luas_persegi_panjang():
    panjang = int(input("Massukan Panjang : "))
    lebar   = int(input("Massukan Lebar   : "))

    luasp = panjang*lebar

    print(f"Luasnya adalah : {luasp}")

print("Aplikasi Rajeg\n")
print("1. Luas Persegi\n2. Luas Lingkaran\n3. Luas persegi panjang\n")
pilihan = int(input("Massukan pilihan : "))

if pilihan == 1:
    luas_persegi()

elif pilihan == 2:
    luas_lingkaran()

elif pilihan == 3:
    luas_persegi_panjang()

else:
    print("Bodat sia pilihanna teh sampe tilu jih !!")
    exit()