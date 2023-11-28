import os

def main():
    os.system("cls")
    c = int(input("Input Angka yang Diinginkan : "))

    for b in range(1, c):
        for a in range(c - 1, b, -1):
            print("_", end="")
        for a in range(b + 1):
            print("*", end="")
        for a in range(c, 0, -1):
            print("_", end="")
        for a in range(b + 1):
            print("*", end="")
        print()

    for b in range(2):
        for a in range(c + b):
            print("_", end="")
        for a in range(c - b * 2):
            print("*", end="")
        print()


if __name__ == "__main__":
    main()
