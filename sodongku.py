import os

def print_sudoku(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                print("*", end=" ")
            else:
                print(board[i][j], end=" ")
        print()

sudoku = [
    [1, 0, 0, 0],
    [0, 3, 0, 0],
    [4, 0, 0, 0],
    [0, 2, 0, 4]
]

correct_solution = [
    [1, 4, 2, 3],
    [2, 3, 4, 1],
    [4, 1, 3, 2],
    [3, 2, 1, 4]
]

print("=========== Selamat datang di gem sodongku ===========\n")
print("Permainan Sudoku ini Ber (basis) Matrix 4x4 kalau jago selesain ya EUE XD\n")
input("Press Enter to Continue")

os.system('cls')

while True:
    user_solution = [
        [1, 0, 0, 0],
        [0, 3, 0, 0],
        [4, 0, 0, 0],
        [0, 2, 0, 4]
    ]

    print("Game Sudoku")
    print("===========")
    print("\n")
    print_sudoku(sudoku)
    print("\nSilakan menjawab ya qaqa 30E")
    print("-------------------------------")

    for i in range(4):
        for j in range(4):
            if sudoku[i][j] == 0:
                user_input = int(input(f"Masukkan Angka Baris {i + 1} Kolom {j + 1}: "))
                user_solution[i][j] = user_input

    print("\nSoal Asli\n")
    print_sudoku(sudoku)
    print("\nJawaban Anda\n")
    print_sudoku(user_solution)

    if user_solution == correct_solution:
        print("\nSelamat! Anda menyelesaikan Sudoku dengan benar.")
        print("YIIIPEE")
        break
    else:
        print("\nMaaf, jawaban Anda tidak benar. Coba lagi.")
        p =input("\nPress Enter untuk main lagi atau q untuk Exit : ")
        if p.lower() == "q":
            exit()
        os.system('cls')
