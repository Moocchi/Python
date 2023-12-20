from colorama import init, Fore, Style

init()

name = ""
role = ""
lvl = 1
atk = 1000
hp = 100
sp = 100
mora = 0
weapon = []

def print_stats():
    print(f"{Fore.MAGENTA}=" * 50)
    print("+++++++++++++++++++++ STATS ++++++++++++++++++++++")
    print(f"=" * 50)
    print(f"{Fore.BLUE}Name  : {name:<20}\t\tLvl   : {lvl}")
    print(f"Role  : {role:<20}\t\tAtk   : {atk}")
    print(f"{Fore.RED}HP    : [{'=' * int(hp / 5):<20}] {hp}")
    print(f"{Fore.YELLOW}SP    : [{'=' * int(sp / 5):<20}] {sp}")
    print(f"{Fore.GREEN}Mora  : {mora}\n")
    
