# This program is used for telnet particular host
# It is just simple illustration how to use telnet lib to login into routers. We can make it more fruitfull and complex by using loops and reading commands from different files. 
# Snice  telnet is easy to intercept data flow that is why it make simple.


import getpass
import telnetlib

HOST = input("Enter targeted hostname/IP of that device:- ")
user = input("Enter your Username: ")
password = getpass.getpass()

telnethost = telnetlib.Telnet(HOST)

telnethost.read_until(b"Username: ")
telnethost.write(user.encode('ascii') + b"\n")
if password:
    telnethost.read_until(b"Password: ")
    telnethost.write(password.encode('ascii') + b"\n")

telnethost.write(b"\n")
telnethost.write(b"enable\n")
telnethost.write(b"cisco\n")
telnethost.write(b"show ip int brief \n")
telnethost.write(b"conf t \n")
telnethost.write(b"int lo1\n")
telnethost.write(b"ip address 1.1.1.1 255.255.255.255\n")
telnethost.write(b"end\n")
telnethost.write(b"exit\n")

print(telnethost.read_all().decode('ascii'))
