import os


os.system("cls")
print("=" * 12)
print("Nilai BLYATT")
print("=" * 12)
nilai = float(input("Massukan nilai : "))

if 90 <= nilai <= 100:
    os.system("cls")
    print("Nilai          :", nilai)
    print("Grade          : A")
    print("Keterangan     : Sangat baik reflek bosku mantap")
    print("Press enter to continue")
    input()
elif 70 <= nilai <= 89:
    os.system("cls")
    print("Nilai          :", nilai)
    print("Grade          : B")
    print("Keterangan     : Baik")
    print("Press enter to continue")
    input()
elif 40 <= nilai <= 69:
    os.system("cls")
    print("Nilai          :", nilai)
    print("Grade          : C")
    print("Keterangan     : Cukup")
    print("Press enter to continue")
    input()
elif 0 <= nilai <= 39:
    os.system("cls")
    print("Nilai          :",  nilai)
    print("Grade          : D")
    print("Keterangan     : YOU STUPID NIGGER")
    print("Press enter to continue")
    input()
else:
    os.system("cls")
    print("Masukan nilai dari 0 sampai 100 :)")
    input(print("Press enter to continue"))

