def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def permutation(n, r):
    if n < r:
        return 0  # Invalid input, n should be greater than or equal to r

    print(f"\nFaktorisasi n dengan nilai {n} :\n")
    print("Rumus Permutasi:")
    print("____n!___")
    print("( n - r ) !")

    # Display the factorization process for n
    print(f"\nFaktorisasi n dengan nilai {n}:\n")
    print("Begin Factorization Process")
    print("---------------------------")

    sum_n = 1

    for i in range(n, 0, -1):
        print(i, end="")
        if i > 1:
            print(" * ", end="")
        sum_n *= i

    print(f" = {sum_n}")
    print("---------------------------")
    print("End Factorization Process\n")

    # Display the factorization process for (n-r)
    print(f"\nFaktorisasi (n-r) dengan nilai {n - r}:\n")
    print("Begin Factorization Process")
    print("---------------------------")

    sum_nr = 1

    for i in range(n - r, 0, -1):
        print(i, end="")
        if i > 1:
            print(" * ", end="")
        sum_nr *= i

    print(f" = {sum_nr}")
    print("---------------------------")
    print("End Factorization Process\n")

    # Display the final result
    print(f"\nMaka Sama Dengan :\n")
    print(f"{sum_n} / {sum_nr} = {sum_n // sum_nr}")

    return sum_n // sum_nr

def combination(n, r):
    if n < r:
        return 0  # Invalid input, n should be greater than or equal to r

    print("\nRumus Kombinasi:")
    print("____n!____")
    print(" r!(n-r)!")

    # Display the factorization process for n
    print(f"\nFaktorisasi n dengan nilai {n} :\n")
    print("Begin Factorization Process")
    print("---------------------------")

    sum_n = 1

    for i in range(n, 0, -1):
        print(i, end="")
        if i > 1:
            print(" * ", end="")
        sum_n *= i

    print(f" = {sum_n}")
    print("---------------------------")
    print("End Factorization Process\n")

    # Display the factorization process for r
    print(f"\nFaktorisasi r dengan nilai {r} :\n")
    print("Begin Factorization Process")
    print("---------------------------")

    sum_r = 1

    for i in range(r, 0, -1):
        print(i, end="")
        if i > 1:
            print(" * ", end="")
        sum_r *= i

    print(f" = {sum_r}")
    print("---------------------------")
    print("End Factorization Process\n")

    # Display the factorization process for (n-r)
    print(f"\nFaktorisasi (n-r) dengan nilai {n - r} :\n")
    print("Begin Factorization Process")
    print("---------------------------")

    sum_nr = 1

    for i in range(n - r, 0, -1):
        print(i, end="")
        if i > 1:
            print(" * ", end="")
        sum_nr *= i

    print(f" = {sum_nr}")
    print("---------------------------")
    print("End Factorization Process\n")

    # Display the final result
    print(f"\nMaka Sama Dengan :\n")
    print(f"{sum_n} / ({sum_r} * {sum_nr}) = {sum_n // (sum_r * sum_nr)}")

    return sum_n // (sum_r * sum_nr)

# Define a memoization dictionary to store previously calculated Fibonacci values
memo = {}

# Initialize memoization dictionary
def initialize_memoization():
    global memo
    memo = {0: 0, 1: 1}

# Recursive Fibonacci function with memoization
def fibonacci(n):
    if n not in memo:
        memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]

if __name__ == "__main__":
    initialize_memoization()  # Initialize memoization dictionary

    while True:
        print("Aplikasi Rekursif")
        print("-----------------\n")

        print("Menu : ")
        print("[1] Permutasi")
        print("[2] Kombinasi")
        print("[3] Fibonacci")
        print("[4] Keluar\n")

        pilihan = int(input("Masukkan Pilihan [1-4]: "))

        if pilihan == 1:
            print("==============================")
            print("PERMUTASI")
            print("==============================")

            n = int(input("Masukkan Nilai n : "))
            r = int(input("Masukkan Nilai r : "))

            if n < 0 or r < 0 or n < r:
                print("Nilai n dan r harus non-negatif, dan n harus lebih besar atau sama dengan r.")
            else:
                result_permutation = permutation(n, r)
                print(f"\nMaka Hasil Kombinasi dari {n}P{r} adalah {result_permutation}")
                input("\nTekan Enter Untuk Lanjut...")
        elif pilihan == 2:
            print("==============================")
            print("KOMBINASI")
            print("==============================")

            n = int(input("Masukkan Nilai n : "))
            r = int(input("Masukkan Nilai r : "))

            if n < 0 or r < 0 or n < r:
                print("Nilai n dan r harus non-negatif, dan n harus lebih besar atau sama dengan r.")
            else:
                result_combination = combination(n, r)
                print(f"\nMaka Hasil Kombinasi dari {n}C{r} adalah {result_combination}")
                input("\nTekan Enter Untuk Lanjut...")
        elif pilihan == 3:
            print("==============================")
            print("FIBONACI")
            print("==============================")

            n = int(input("Masukkan Nilai n : "))

            if n < 0:
                print("Nilai n harus non-negatif.")
            else:
                result_fibonacci = fibonacci(n)
                print(f"\nBilangan Fibonacci ke {n} adalah {result_fibonacci}")
                input("\nTekan Enter Untuk Lanjut...")
        elif pilihan == 4:
            print("Keluar")
            break
        else:
            print("Pilihan tidak valid.")
