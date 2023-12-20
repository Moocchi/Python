import os
import random
import time
from colorama import init, Fore, Style
import Player
from game_rajegh_warrior import menu_player
h_name = "Hilichurl"
h_lvl = 5
h_atk = 10
h_hp = 30

def reset_hilichurl_health():
    global h_hp
    h_hp = 30
    
def print_Hilichurl():
    print(f"{Fore.YELLOW}=" * 50)
    print("++++++++++++++++++ ENEMY INFO ++++++++++++++++++++")
    print(f"=" * 50)
    print(f"Name  : {h_name:<20}\t\tLvl   : {h_lvl}")
    print(f"Atk   : {h_atk}{Style.RESET_ALL}")
    print(f"{Fore.RED}HP    : [{'=' * int(h_hp / 3):<10}] {h_hp}{Style.RESET_ALL}")

def player_turn():
    global h_hp
    print("\nPlayer's Turn:")
    print("1. Attack")
    print("2. Defend")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        damage = random.randint(5, Player.atk)
        h_hp -= damage
        os.system('cls')
        print(f"You attacked the Hilichurl and dealt {damage} damage!")
        time.sleep(2)
    elif choice == "2":
        os.system('cls')
        print("You chose to defend. You take reduced damage on the Hilichurl's turn.")
        time.sleep(2)
    else:
        os.system('cls')
        print("Invalid choice. You missed your turn.")
        time.sleep(2)

def hilichurl_turn():
    print("Hilichurl's Turn:")
    time.sleep(1)
    attack_multiplier = random.uniform(0.8, 1.2)
    player_defense = 0

    
    if random.choice([True, False]):
        player_defense = random.randint(2, 8)
        print(f"The Hilichurl attacked, but you defended and took only {player_defense} damage!")
        time.sleep(1)

    player_damage = max(0, int(h_atk * attack_multiplier) - player_defense)
    Player.hp -= player_damage
    print(f"The Hilichurl attacked and dealt {player_damage} damage!")
    time.sleep(1)

def Hilichurl():
    global h_hp
    while Player.hp > 0 and h_hp > 0:
        os.system('cls')
        Player.print_stats()
        print_Hilichurl()

        player_turn()
        hilichurl_turn()

        if h_hp <= 0:
            print("\nCongratulations! You defeated the Hilichurl!")
            print("Reward:")
            print("Mora 50")
            Player.mora += 50
            time.sleep(2)
            menu_player()
            time.sleep(2)
            reset_hilichurl_health()
            break

        if Player.hp <= 0:
            os.system('cls')
            print("You were defeated by the Hilichurl. Game over.")
            time.sleep(1)
            reset_hilichurl_health()
            break