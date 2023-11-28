import time

'''uang = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,0]

for value in uang :
    print(f"uang {value}")'''

'''nama = ["ilham, kurniawan, kon, tol, lo, don, sella, hutao, furina, ganyu"]

# Memisahkan string menjadi nama-nama terpisah dengan menggunakan koma sebagai pembatas
nama_array = nama[0].split(', ')

# Mengulang melalui setiap nama dan mencetak setiap karakter bersama nomor absen dari 1 hingga 10
for i, nama_individual in enumerate(nama_array, start=1):
    print(f"absen {i} : {nama_individual}")'''

'''uang = 10000
harga = 1000

sisa = []

for _ in range(10):
    uang -= harga 
    sisa.append(uang) 

print(sisa)'''

a = [10]

user_input = int(input("Masukkan integer: "))
a.append(user_input)  # Use append to add the user input as the second element

print(a)
