import time
from colorama import init, Fore, Style

init()

def progress_bar(total=50):
    for i in range(1, total + 1):
        progress = "[" + "=" * i + " " * (total - i) + "]"
        print(f"\r{Fore.BLUE}{progress}", end="")

        # Adjust sleep duration to reverse from fast to slow
        sleep_duration = max(0, 0.1 - ((total - i) / (total * 10)))
        time.sleep(sleep_duration)

    print("\nLoading complete!")