import os
import time
from colorama import init, Fore, Style
import loading
import game_rajegh_warrior
import Hilichurl_




def Hilichurl_camp():
    os.system("cls")
    time.sleep(1)
    print("You Entering Hillichurl Camp....")
    time.sleep(1)
    attack = input("Ecounter a Hilichurl. Attack it ? (y/n) : ").strip()

    if attack.lower() == "y":
        os.system("cls")
        time.sleep(1)
        print("Entering Battle field !!!")
        loading.progress_bar()
        time.sleep(1)
        Hilichurl_.Hilichurl()
    elif attack.lower() == "n":
        os.system("cls")
        time.sleep(1)
        print("Running")
        print("Returning to Main menu")
        loading.progress_bar()
        time.sleep(1)
        game_rajegh_warrior.menu_player()
    else:
        print("Invalid Option")

    Hilichurl_.reset_hilichurl_health()


def Mitachurl_camp():
    os.system("cls")
    time.sleep(1)
    print("You Entering Mitachurl Camp....")
    time.sleep(1)
    attack = input("Ecounter a Mitachurl. Attack it ? (y/n) : ")

    if attack.lower() == "y":
        os.system("cls")
        time.sleep(1)
        print("Entering Battle field !!!")
        loading.progress_bar()
    else:
        os.system("cls")
        time.sleep(1)
        print("Running")
        print("Returning to Main menu")
        loading.progress_bar()
        time.sleep(1)
        game_rajegh_warrior.menu_player()


def Fatui_camp():
    os.system("cls")
    time.sleep(1)
    print("You Entering Fatui Camp....")
    time.sleep(1)
    attack = input("Ecounter a Fatui. Attack it ? (y/n) : ")

    if attack.lower() == "y":
        os.system("cls")
        time.sleep(1)
        print("Entering Battle field !!!")
        loading.progress_bar()
    else:
        os.system("cls")
        time.sleep(1)
        print("Running")
        print("Returning to Main menu")
        loading.progress_bar()
        time.sleep(1)
        game_rajegh_warrior.menu_player()


def Abbys():
    os.system("cls")
    time.sleep(1)
    print(f"{Fore.RED}Caution you Are Entering Dangerous zone")
    time.sleep(1)
    print("You Entering The Abbys !!!")
    time.sleep(1)
    attack = input("Ecounter a Dark Abbys Creature. Attack it ? (y/n) : ")

    if attack.lower() == "y":
        os.system("cls")
        time.sleep(1)
        print("Entering Battle field !!!")
        loading.progress_bar()
    else:
        os.system("cls")
        time.sleep(1)
        print("Running")
        print("Returning to Main menu")
        loading.progress_bar()
        time.sleep(1)
        game_rajegh_warrior.menu_player()

