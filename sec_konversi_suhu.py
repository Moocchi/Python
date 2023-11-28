import os

def C_ke_F():
    while True:
        try:
            celsius = float(input("Masukkan Suhu Dalam Celsius (°C) : "))
            break
        except ValueError: 
            os.system("cls")
            print("Masukkan harus berupa angka. Coba lagi.")

    farenheit = (celsius * 9 / 5) + 32
    print(f"{celsius}°C Sama Dengan {farenheit}F")

def C_ke_R():
    while True :
        try :
            celsius = float(input("Massukan Suhu Dalam Celsius (°C) : "))
            break
        except ValueError:
            os.system("cls")
            print("Masukkan harus berupa angka. Coba lagi.")
    
    reamur = celsius*4/5
    print(f"{celsius}°C Sama Dengan {reamur} Re")

def C_ke_k():
    while True :
        try :
            celsius = float(input("Massukan Suhu Dalam Celsius (°C) : "))
            break
        except ValueError:
            os.system("cls")
            print("Masukkan harus berupa angka. Coba lagi.")

    kelvin = celsius + 273.15
    print(f"{celsius}°C Sama Dengan {kelvin}K")

