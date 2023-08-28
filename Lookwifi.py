#!/user/bin/env python3
from colorama import init, Fore, Style, Back
import os
from time import sleep
init()
os.system("clear")
print(Fore.YELLOW+Style.BRIGHT+"""

    '##::::::::'#######:::'#######::'##:::'##:
     ##::::::::'##.... ##:'##.... ##: ##::'##::
     ##::::::: ##:::: ##: ##:::: ##: ##:'##:::
     ##::::::: ##:::: ##: ##:::: ##: #####::::
     ##::::::: ##:::: ##: ##:::: ##: ##. ##:::
     ##::::::: ##:::: ##: ##:::: ##: ##:. ##::
     ########:. #######::. #######:: ##::. ##:
    ........:::.......::::.......:::..::::..::
            '##:::::'##:'####:'########:'####:        
             ##:'##: ##:. ##:: ##.....::. ##::        
             ##: ##: ##:: ##:: ##:::::::: ##::        
             ##: ##: ##:: ##:: ######:::: ##::        
             ##: ##: ##:: ##:: ##...::::: ##::        
             ##: ##: ##:: ##:: ##:::::::: ##::        
            . ###. ###::'####: ##::::::::'####:        
            :...::...:::....::..:::::::::....::        

""")
title = """
         - Created by: 1LugarParaProgramar
         
         - Author Hans Saldias
         
         - Script para ver aparatos conectados a tu wifi
         -                    --- v1 ----- 

"""
for i in title:
    print(i, end='', flush=True)
    sleep(0.1)
cuestions = input("Deseas intalar lookwifi? (y/n): ")
print("Intalando nmap.... ")
sleep(3)
install = ("apt install nmap")
os.system(install)
print("Intalando net-tools")
sleep(3)
tools = ("apt install net-tools")
os.system(tools)

print("Consultando tu ip la cual debes ingresar (copiar y pegar) \n")
sleep(3)
os.system("ifconfig")

print("ingresa los dijitos donde dise inet xxxxxxxx")
sleep(3)

ip = input("Ingrese su ip:  ")

os.system(f"nmap -sP {ip}/24")

sleep(3)
print("Estas son las ips conectadas a tu red wifi la primera es del router las siguientes cada equipo conectadas a ellas\n\n ")
print("Gracias .... ")
