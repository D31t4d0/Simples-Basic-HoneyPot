import os
import socket
import time

#File : d3it4dxpot.py
#Description : One Simple Basic Honeypot 

#Socket 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP

#IP
ip = input("\033[1;32mIP \033[1;31m : \033[1;34m")
ssh = int("22")
ftp = int("21")

#Colors
green = "\033[1;32m"
blue = "\033[1;34m"
yellow = "\033[1;33m"
red = "\033[1;31m"
#FTP Honeypot
def ftphoney():
    print(f"{blue} ██╗  ██╗ ██████╗ ███╗   ██╗███████╗██╗   ██╗██████╗  ██████╗ ████████╗██║  ██║██╔═══██╗████╗  ██║██╔════╝╚██╗ ██╔╝██╔══██╗██╔═══██╗╚══██╔══╝███████║██║   ██║██╔██╗ ██║█████╗   ╚████╔╝ ██████╔╝██║   ██║   ██║   ██╔══██║██║   ██║██║╚██╗██║██╔══╝    ╚██╔╝  ██╔═══╝ ██║   ██║   ██║   ██║  ██║╚██████╔╝██║ ╚████║███████╗   ██║   ██║     ╚██████╔╝   ██║   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝      ╚═════╝    ╚═╝   ")
    print(f" {green}By {blue}!     Deitado.pls{yellow}#0001")
    print(f"{green}Listening {blue} {ip}:{ftp}")
    print(f"{green}Method {red} FTP")
    sock.bind((ip, ftp))
    while True:
     sock.listen()
     a, b = sock.accept()
     print(b)

#SSH Honeypot
def sshhoney():
    print(f"{blue} ██╗  ██╗ ██████╗ ███╗   ██╗███████╗██╗   ██╗██████╗  ██████╗ ████████╗██║  ██║██╔═══██╗████╗  ██║██╔════╝╚██╗ ██╔╝██╔══██╗██╔═══██╗╚══██╔══╝███████║██║   ██║██╔██╗ ██║█████╗   ╚████╔╝ ██████╔╝██║   ██║   ██║   ██╔══██║██║   ██║██║╚██╗██║██╔══╝    ╚██╔╝  ██╔═══╝ ██║   ██║   ██║   ██║  ██║╚██████╔╝██║ ╚████║███████╗   ██║   ██║     ╚██████╔╝   ██║   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝      ╚═════╝    ╚═╝   ")
    print(f" {green}By {blue}!     Deitado.pls{yellow}#0001")
    print(f"{green}Listening {blue} {ip}:{ssh}")
    print(f"{green}Method {red} SSH")
    sock.bind((ip, ssh))
    while True:
     sock.listen()
     a, b = sock.accept()
     print(b)
     
    
#Escolha
os.system("clear")
print(f"{blue} ██╗  ██╗ ██████╗ ███╗   ██╗███████╗██╗   ██╗██████╗  ██████╗ ████████╗██║  ██║██╔═══██╗████╗  ██║██╔════╝╚██╗ ██╔╝██╔══██╗██╔═══██╗╚══██╔══╝███████║██║   ██║██╔██╗ ██║█████╗   ╚████╔╝ ██████╔╝██║   ██║   ██║   ██╔══██║██║   ██║██║╚██╗██║██╔══╝    ╚██╔╝  ██╔═══╝ ██║   ██║   ██║   ██║  ██║╚██████╔╝██║ ╚████║███████╗   ██║   ██║     ╚██████╔╝   ██║   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝      ╚═════╝    ╚═╝   ")
print(f" {green}By {blue}!     Deitado.pls{yellow}#0001")
print(f"{red}1 {green} FTP Honeypot")
print(f"{red}2 {green} SSH Honeypot")
options = input(f"{green}Options :{red} ")
if options == "1":
    os.system("clear")
    ftphoney()
elif options == "2":
    os.system("clear")
    sshhoney()
else:
    print(f"{red}Invalid Option")