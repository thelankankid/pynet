import ConnectHandler from netmiko
import os
import getpass from getpass

device1 = {
    "device_type": "cisco_ios",
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password
}

device2 = {
    "device_type": "cisco_nxos",
    "host": "nxos4.lasthop.io",
    "username": "pyclass",
    "password": password
}

devices = [device1, device2]

commands = net_connect.send_command_timing(
    "ping 8.8.8.8", strip_prompt=False, strip_command=False
)

net_connect = ConnectHandler(**devices)

for device in devices:
