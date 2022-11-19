from getpass import getpass
from netmiko import ConnectHandler


device1 = {
    "host": 'cisco1.lasthop.io', 
    "username": 'pyclass', 
    "password": getpass(),
    "device_type": 'cisco_ios',
    "session_log": 'my_sesion.txt'
}

net_connect = ConnectHandler(**device1)
print(net_connect.send_command("show ip int br"))
