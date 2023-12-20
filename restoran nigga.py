import os

nama_makanan = []
harga = []

def Sort_name():
    for i in range(len(nama_makanan)):
        for j in range(0, len(nama_makanan)-i-1):
            if nama_makanan[j] > nama_makanan[j+1]:
                nama_makanan[j], nama_makanan[j+1] = nama_makanan[j+1], nama_makanan[j]
                harga[j], harga[j+1] = harga[j+1], harga[j]
def Sort_harga(): 
    for i in range(len(harga)):
        min_index = i
        for j in range(i+1, len(harga)):
            if harga[j] < harga[min_index]:
                min_index = j
                harga[i], harga[min_index] = harga[min_index], harga[i]
                nama_makanan[i], nama_makanan[min_index] = nama_makanan[min_index], nama_makanan[i]
def binary_search(item):
    low = 0
    high = len(nama_makanan) - 1

    while low <= high:
        mid = (low + high) // 2
        if nama_makanan[mid] == item:
            return mid
        elif nama_makanan[mid] < item:
            low = mid + 1
        else:
            high = mid - 1

    return -1
def display_menu():
    os.system('cls')
    print("\t     Restaurant Nzz")
    print("="*45)
    print("No\t     Nama Barang\tHarga")
    print("="*45)
    for i in range(len(nama_makanan)):
        print(f"{i+1}\t     {nama_makanan[i]}\t\tRp.{harga[i]}")
    print("="*45)
def search_menu():
    os.system('cls')
    search_item = input("Masukkan nama makanan yang ingin dicari: ")
    Sort_name()
    result1 = 1
    result = binary_search(search_item)

    if result != -1:
        print("="*30)
        print(f"{search_item} ditemukan pada indeks {result+result1}")
        print("="*30)
        input("Enter to continue")
    else:
        print("="*30)
        print(f"{search_item} tidak ditemukan")
        print("="*30)
        input("Enter to continue")
def add_new_menu():
    os.system('cls')
    print("="*17)
    print("=Tambah Makanan=")
    print("="*17)
    nama = input("Masukkan Nama makanan: ")
    harga_makanan = int(input("Masukkan Harga Makanan: "))
    nama_makanan.append(nama)
    harga.append(harga_makanan)


def main():
    while True:
        display_menu()
        print("\n1. Add new menu\n2. Sort menu by name (Bubble Sort)\n3. Sort menu by price (Selection Sort)\n4. Search menu (Binary Search)\n5. Exit")
        pilihan = int(input("\nMasukkan pilihan: "))

        if pilihan == 1:
            add_new_menu()
        elif pilihan == 2:
           Sort_name()
        elif pilihan == 3:
           Sort_harga()
        elif pilihan == 4:
            search_menu()
        elif pilihan == 5:
            print("Dadah :>")
            exit()

main()