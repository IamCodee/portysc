import socket
from IPy import IP
import colorama
from colorama import Fore
colorama.init()


print(Fore.RED + """

  ____                   _                        
 |  _ \    ___    _ __  | |_   _   _   ___    ___ 
 | |_) |  / _ \  | '__| | __| | | | | / __|  / __|
 |  __/  | (_) | | |    | |_  | |_| | \__ \ | (__ 
 |_|      \___/  |_|     \__|  \__, | |___/  \___|
                               |___/              
""" + Fore.RESET)
print("")
print(Fore.YELLOW +"""

> Coded by @IamCodee
> Twitter  @IamCode7
> Github   @IamCodee
> Version 1.0 

""" + Fore.RESET)

while True:
    def scan(target):
        converted_ip = check_ip(target)
        print("")
        port = int(input("Select ur range to scan [eg, 100]: "))
        print("")
        print(Fore.RED + '[Scanning../././.] '+ Fore.WHITE +  str(target))
        print("-----------------------------------------------------------")

        for port in range(0,port):
            scan_port(converted_ip, port)

    def check_ip(ip):
        try:
            IP(ip)
            return(ip)
        except ValueError:
            return socket.gethostbyname(ip)

    def scan_port(ipaddress, port):

        try:
            sock = socket.socket()

            sock.settimeout(0.100)

            sock.connect((ipaddress, port))
    
            print(Fore.GREEN + "[+] Port " + str(port) + Fore.WHITE + " is open")
        except:
            
            pass
    print("")
    targets = input("[0_0] Enter Ip/website[ , for multiple scans]: ")
    if ',' in targets:
        for ip_add in targets.split(','):
            scan(ip_add.strip(' '))
    else:
        scan(targets)


    print("")
  


        