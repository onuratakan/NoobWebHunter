import sys
import ipapi
from colorama import Fore, init

init()


def __start__():
    print(Fore.RED+"\n [!] Enter IP Address")
    print(Fore.RED+"\n [/] Or Press The Enter Key To see Your IP:) \n")

    site = input(Fore.RED+" ┌─["+Fore.LIGHTBLUE_EX+"NoobWebHunter"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"IP-Location"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"✠ ")

    source = ipapi.location(ip=site, key=None)
    try:
        print(Fore.GREEN+" [!]"+Fore.RED+" See your info")
        print(Fore.GREEN+" [!]"+Fore.BLUE+" IP = "+ source["ip"])
        print(Fore.GREEN+" [!]"+Fore.BLUE+" City = " + source["city"])
        print(Fore.GREEN+" [!]"+Fore.BLUE+" Region = "+ source["region"])
        print(Fore.GREEN+" [!]"+Fore.BLUE+" Id Country = "+source["country"])
        print(Fore.GREEN+" [!]"+Fore.BLUE+" Country = "+ source["country_name"])
        print(Fore.GREEN+" [!]"+Fore.BLUE+" Calling Code = "+source["country_calling_code"])
        print(Fore.GREEN+" [!]"+Fore.BLUE+" Languages = "+source["languages"])
        print(Fore.GREEN+" [!]"+Fore.BLUE+" Org = "+ source["org"])
        try:
            input(Fore.RED+" [!] "+Fore.GREEN+"Back To Menu (Press Enter...) ")
        except:
            print("")
            sys.exit()  
    except:
        print(Fore.RED+"Sorry Please Enter IP Address")

