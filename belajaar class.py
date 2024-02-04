import os


class moocchi:
    def __init__(self, nama, level, duit):
        self.nama = nama
        self.level = level
        self.duit = 0


name = ""
player = moocchi(nama=name, level=1, duit=0)

os.system("cls")
p = input("Massukan nama                :")
player.nama += p

print(f"\nUang saat ini                : {player.duit} ")
f = int(input("Ingin menambah berapa duit ? : "))
player.duit += f

print(f"\n\nNama  : {player.nama}")
print(f"Level : {player.level}")
print(f"Duit  : {player.duit:,.2f} Rp")
