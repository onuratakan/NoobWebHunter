import os
import requests
import json
import sys
from colorama import Fore, init

init()


def __start__ ():

    print (Fore.RED+"\n [!] Enter The Domain/ip\n")

    website = input(Fore.RED+" ┌─["+Fore.LIGHTBLUE_EX+"NoobWebHunter"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Reverse-IP"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"✠ ")

    mysite = {"remoteAddress":website}

    link = requests.post("https://domains.yougetsignal.com/domains.php", mysite)

    source = json.loads(link.content)

    print(source)


    for data in source["domainArray"]:
        print(" "+data[0]+"\n")

    try:

            input(Fore.RED+" [!] "+Fore.GREEN+"Back To Menu (Press Enter...) ")
    except:
            print("")
            sys.exit()