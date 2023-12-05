import os
import pygame
import time

def play_music(file_path):
    pygame.init()
    pygame.mixer.init()

    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        # Add some delay to allow the music to play
        time.sleep(8)  # Adjust the sleep time as needed

    except pygame.error:
        print("Error loading or playing the music.")

    finally:
        pygame.mixer.quit()
        pygame.quit()

#harga makanan
MieGoreng  = 25000;NasiGoreng = 22000;SotoAyam   = 20000
#harga minuman
JusMangga = 10000;Airputih = 1000;Kopi = 5000
#tingkat pedas
SangatPedas ='''Sangat Pedas''';Pedas ='''Pedas''';TidakPedas  ='''Tidak Pedas'''
#jenis minuman
Dingin ='''Dingin''';Panas  ='''Panas''';Hangat ='''Hangat'''
#total
total = 0; total_order_makan = 0; total_order_minum = 0; order = ''; minum_= ''; tipe_makan =''; tipe_minum =''; uang_pelanggan= 0


os.system('cls')
print("==Selamat datang==\n")
nama = str(input("Massukan Nama Pemesan : "))

os.system('cls')
print('''Menu Makanan :\n
1. Mie Goreng\n2. Nasi goreng\n3. Soto ayam\n''')
menu = int(input("Pilihan menu : "))

if menu == 1:
    print("Mie Goreng = 25.000Rp\n")
    jumlahmiegoreng = int(input("\nMasukkan Jumlah Pesanan : "))
    total += MieGoreng*jumlahmiegoreng
    order += "Mie oreng"
    total_order_makan += jumlahmiegoreng
elif menu == 2:
    print("Nasi Goreng = 22.000Rp\n")
    jumlahnasigoreng = int(input("massukan jumlah Pesanan :  "))
    total += NasiGoreng*jumlahnasigoreng
    order += "Nasi Goreng"
    total_order_makan += jumlahnasigoreng

elif menu == 3:
    print("Soto Ayam = 22.000Rp\n")
    jumlahsotoayam = int(input("Massukan jumlah Pesanan : "))
    total += SotoAyam*jumlahsotoayam
    order += "Soto Ayam"
    total_order_makan += jumlahsotoayam

else:
    print("Menu tidak valid :(")

os.system('cls')
print("Menu Minuman :\n")
print('''1. Jus Mangga\n2. Air Putih\n3. Kopi\n''')
minum = int(input("Pilihan : "))

if minum == 1:
    print("Jus Mangga = 10.000Rp\n")
    jumlahjusmangga= int(input("Massukan jumlah Pesanan : "))
    total += JusMangga*jumlahjusmangga
    minum_+= "Jus Mangga"
    total_order_minum += jumlahjusmangga

elif minum == 2:
    print("Air Putih = 1.000Rp\n")
    jumlahairputih= int(input("Massukan jumlah Pesanan : "))
    total += Airputih*jumlahairputih
    minum_+= "Air Putih"
    total_order_minum += jumlahairputih

elif minum == 3:
    print("Kopi = 5.000Rp\n")
    jumlahkopi= int(input("Massukan jumlah Pesanan : "))
    total += Kopi*jumlahkopi
    minum_+= "Kopi"
    total_order_minum += jumlahkopi
    

else: 
    print("Menu Tidak Valid :(")

os.system('cls')
print("Pilih tingkat Kepedasan Makanan :\n")
print("1. Sangat Pedas\n2. Pedas\n3. Tidak Pedas\n")
TingkatPedas =int(input("Massukan Pilihan : "))

if TingkatPedas == 1:
    tipe_makan += 'Sangat Pedas'

elif TingkatPedas == 2:
    tipe_makan += 'Pedas'

elif TingkatPedas == 3:
    tipe_makan += 'Tidak Pedas'

else:
    print("Menu tidak Valid")

os.system('cls')
print("Pilih Jenis Minuman :\n")
print("1. Dingin\n2. Panas\n3. Hangat\n")
jenis_minum =int(input("Massukan Pilihan : "))

if jenis_minum == 1:
    tipe_minum += 'Dingin'

elif jenis_minum == 2:
    tipe_minum += 'Panas'

elif jenis_minum == 3:
    tipe_minum += 'Hangat'


else:
    print("Menu tidak Valid")

os.system('cls')
print(f"Total Pesanan        : {total}")
bayar = int(input("Masukkan uang Bayar  : "))
uang_pelanggan += bayar
kembalian = uang_pelanggan - total

while uang_pelanggan < total:
    os.system('cls')
    formatted_total = "{:,.2f}".format(total)
    formatted_kembalian = "{:,.2f}".format(kembalian)  
    
    print("Maaf, uang bayar kurang.")
    print(f"Total Pesanan  :Rp {formatted_total},-")
    print(f"Uang Anda  :Rp {uang_pelanggan:,.2f},-")
    print(f"Kekurangan  :Rp {total - uang_pelanggan:,.2f},-")
    
    print("\nPilihan:")
    print("1. Tambah uang")
    print("2. Keluar")
    
    pilihan = input("Masukkan pilihan (1/2): ")
    
    if pilihan == "1":
        tambah_uang = int(input("Masukkan jumlah uang tambahan: "))
        uang_pelanggan += tambah_uang
        kembalian = uang_pelanggan - total
        print(f"Uang Anda sekarang: Rp {uang_pelanggan:,.2f},-")
    elif pilihan == "2":
        print("Terima kasih!")
        exit()
    else:
        print("Pilihan tidak valid. Program keluar.")
        exit()


os.system('cls')
formatted_total = "{:,.2f}".format(total)
formatted_kembalian = "{:,.2f}".format(kembalian)  

print(f"Pesanan Atas Nama",nama.upper())
print(f"{total_order_makan} {order} {tipe_makan}")
print(f"{total_order_minum} {minum_} {tipe_minum}")
print(f"Total Pesanan  :Rp {formatted_total},-")
print(f"Uang Pelanggan :Rp {uang_pelanggan:,.2f},-")
print(f"Kembalian      :Rp {formatted_kembalian},-")
print("Terima Kasih !!!")

music_file_path = 'D:\JAREZ\File\python\Python\WhatsApp-Audio-2023-11-10-at-13.52.10_1eb0ddc9.waptt.mp3'  
play_music(music_file_path)