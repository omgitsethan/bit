from consolemenu import *
from consolemenu.items import *
from pyfiglet import Figlet as f
from colorama import Fore, Back, Style
from colorama.ansi import clear_screen
from colorama import init as i
from libs import data
import requests,os,sys

def init():
    i(); print("\033[H\033[J", end="")
    print(Fore.BLUE + f(font="small").renderText("b i t ."))
    print(Fore.WHITE + "welcome to bit, git but " + Style.BRIGHT + "better." + Style.RESET_ALL)
    select(input("? " + Fore.BLUE))

def gb():
    input(); init()
def select(s):
    if s == "exit":
        sys.exit()
    elif s == "projects":
        username,pat = data.get_login()[0]
        headers = {"Authorization": f"Bearer {pat}", "Accept": "application/json"}
        res = requests.get(f"https://api.github.com/users/{username}/repos", headers=headers)
        for repo in res.json():
            print(Fore.WHITE + "• " + Fore.BLUE + repo["name"])
    elif s == "bit":
        print("bit.")
    else:
        init()
    gb()