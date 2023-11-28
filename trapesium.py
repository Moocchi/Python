def main():
    c = int(input("Input Angka yang Diinginkan: "))
    
    for b in range(1, c):
        for a in range(c - 2, b - 1, -1):
            print("  ", end="")
        for a in range(b + 1):
            print(" *", end="")
        for a in range(c, 0, -1):
            print(" ^", end="")
        for a in range(b + 1):
            print(" *", end="")
        print()

if __name__ == "__main__":
    main()
