import sys
import requests
from colorama import Fore, init

init()


def __start__():

    try:
        print(Fore.RED+" [!] Please Enter The Domain\n")
        inp = input(Fore.RED+" ┌─["+Fore.LIGHTBLUE_EX+"NoobWebHunter"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"NS-Lookup"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"✠ ")
        result = requests.get(
            'https://api.hackertarget.com/dnslookup/?q=' + inp).text
        print(Fore.LIGHTBLUE_EX+result)
        try:
            input(Fore.GREEN+" [*] Back to Menu (Press Enter...) ")
        except:
            print("")
            sys.exit()
    except:
        print("\n Exit :)")
        sys.exit()
