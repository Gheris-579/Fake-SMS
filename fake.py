"""
Author:Gheris :)
"""
from pystyle import Colors, Colorate, Write #pip install pystyle
import requests
import os
from colorama import init, Fore

try:
    os.system("cls")
except:
    os.system("clear")


Write.Print("""
                                        This TOOLS WORKS ONLY ONCE A DAY
                                        
 ▄▄▄      ███▄    █ ▒█████  ███▄    ▓██   ██▓███▄ ▄███▓▒█████  █    ██  ██████      ██████ ███▄ ▄███▓ ██████ 
▒████▄    ██ ▀█   █▒██▒  ██▒██ ▀█   █▒██  ██▓██▒▀█▀ ██▒██▒  ██▒██  ▓██▒██    ▒    ▒██    ▒▓██▒▀█▀ ██▒██    ▒ 
▒██  ▀█▄ ▓██  ▀█ ██▒██░  ██▓██  ▀█ ██▒▒██ ██▓██    ▓██▒██░  ██▓██  ▒██░ ▓██▄      ░ ▓██▄  ▓██    ▓██░ ▓██▄   
░██▄▄▄▄██▓██▒  ▐▌██▒██   ██▓██▒  ▐▌██▒░ ▐██▓▒██    ▒██▒██   ██▓▓█  ░██░ ▒   ██▒     ▒   ██▒██    ▒██  ▒   ██▒
 ▓█   ▓██▒██░   ▓██░ ████▓▒▒██░   ▓██░░ ██▒▓▒██▒   ░██░ ████▓▒▒▒█████▓▒██████▒▒   ▒██████▒▒██▒   ░██▒██████▒▒
 ▒▒   ▓▒█░ ▒░   ▒ ▒░ ▒░▒░▒░░ ▒░   ▒ ▒  ██▒▒▒░ ▒░   ░  ░ ▒░▒░▒░░▒▓▒ ▒ ▒▒ ▒▓▒ ▒ ░   ▒ ▒▓▒ ▒ ░ ▒░   ░  ▒ ▒▓▒ ▒ ░
  ▒   ▒▒ ░ ░░   ░ ▒░ ░ ▒ ▒░░ ░░   ░ ▒▓██ ░▒░░  ░      ░ ░ ▒ ▒░░░▒░ ░ ░░ ░▒  ░ ░   ░ ░▒  ░ ░  ░      ░ ░▒  ░ ░
  ░   ▒     ░   ░ ░░ ░ ░ ▒    ░   ░ ░▒ ▒ ░░ ░      ░  ░ ░ ░ ▒  ░░░ ░ ░░  ░  ░     ░  ░  ░ ░      ░  ░  ░  ░  
      ░  ░        ░    ░ ░          ░░ ░           ░      ░ ░    ░          ░           ░        ░        ░  
                                     ░ ░ 
                       __________________________________              
                      |Author:  Akmenrah :)              |
                      |Instgram: gheris__579_            |
                      |Github: Gheris-579                |
                      |__________________________________|               
\n""",Colors.blue_to_red, interval=0.01)

# some colors
init()
GREEN = Fore.GREEN

def main():
    phone = Write.Input("[*] Enter number of the victim : ",Colors.yellow_to_red)
    print(f">>> {phone}")
    message = Write.Input("[*] ENTER YOUR MSG           :",Colors.blue_to_white)
    print(f">>> {message}")
    resp = requests.post('https://textbelt.com/text', {
    'phone': f'{phone}',
    'message': f'{message}',
    'key': 'textbelt',
    })
    print("\n")
    print(f"{GREEN} {resp.json()}")


if __name__ == "__main__":
    main()