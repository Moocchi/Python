def tukar_nilai(a, b):
    temp = a
    a = b
    b = temp
    return a, b

def bagi_kelas(jumlah_kelas, jumlah_data, data_list):
    jumlah_data //= 2
    hasil_penjumlahan = [0] * jumlah_data
    i, j = 0, 0

    for i in range(0, jumlah_data * 2, 2):
        hasil_penjumlahan[j] = data_list[i] + data_list[i + 1]
        j += 1

    for i in range(jumlah_data - 1):
        for j in range(jumlah_data - i - 1):
            if hasil_penjumlahan[j] < hasil_penjumlahan[j + 1]:
                hasil_penjumlahan[j], hasil_penjumlahan[j + 1] = tukar_nilai(hasil_penjumlahan[j], hasil_penjumlahan[j + 1])
                data_list[j * 2], data_list[(j + 1) * 2] = tukar_nilai(data_list[j * 2], data_list[(j + 1) * 2])
                data_list[j * 2 + 1], data_list[(j + 1) * 2 + 1] = tukar_nilai(data_list[j * 2 + 1], data_list[(j + 1) * 2 + 1])

    for i in range(jumlah_kelas):
        print(f"Kelas X-{i + 1} :")
        for j in range(i, jumlah_data, jumlah_kelas):
            if j < jumlah_data:
                print(f"{data_list[j * 2]} | {data_list[j * 2 + 1]}")
            else:
                print("0 | 0")
        print("------------------------")

def main():
    jumlah_kelas = int(input("Masukkan Banyak Kelas: "))
    jumlah_data = int(input("Masukkan Banyak Data: "))
    
    jumlah_data *= 2
    data = [0] * jumlah_data

    print(f"Masukkan {jumlah_data // 2} pasang data:")
    for i in range(jumlah_data):
        x1 = int(input(f"data ke {i + 1} : "))
        data[i] = x1

    bagi_kelas(jumlah_kelas, jumlah_data, data)

if __name__ == "__main__":
    main()
