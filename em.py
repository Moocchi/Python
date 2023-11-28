tinggi = int(input("Masukkan tinggi huruf M: "))

for i in range(tinggi):
    for j in range(tinggi * 2 - 1):
        if j == 0 or j == tinggi * 2 - 2 or (i == j and j <= tinggi - 1) or (j == tinggi * 2 - 2 - i and j >= tinggi):
            print("*", end="")
        else:
            print(" ", end="")
    print()
