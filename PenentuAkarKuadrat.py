from math import sqrt
import os

while True:
    os.system('cls')
    try:
        
        print("##Program Pencari Akar Kuadrat Gais##\n")

        print("Format Persamaan ax^2 + bx + c = 0 \n")
        a = int(input("Input Nilai a: "))
        b = int(input("Input Nilai b: "))
        c = int(input("Input Nilai c: "))
        break

    except ValueError:
        os.system('cls')
        print("pelis lah bang")

D = (b * b) - (4 * a * c)
print("\nDiskriminan = ", D)

if D == 0:
    print("(Akar Real dan sama)")

    if a != 0:
        x1 = x2 = (-b + sqrt(D)) / (2 * a)

        print("x1 = ", x1)
        print("x2 = ", x2)
    else:
        print("Akar tidak dapat dihitung karena a = 0")

elif D > 0:
    print("(Akar Real dan berbeda)\n")

    X1 = (-b + sqrt(D)) / (2 * a)
    X2 = (-b - sqrt(D)) / (2 * a)

    print("x1 = ", X1)
    print("x2 = ", X2)

else:
    print("(Akar tidak real / imajiner)\n")
