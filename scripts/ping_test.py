import os
from getpass import getpass
from netmiko import ConnectHandler


password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

device = {
    "device_type": "cisco_ios",
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password
}

net_connect = ConnectHandler(**device)

commands = net_connect.send_command_timing(
    "ping", strip_prompt=False, strip_command=False
)
commands += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
commands += net_connect.send_command_timing(
    "8.8.8.8", strip_prompt=False, strip_command=False
)
commands += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
commands += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
commands += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
commands += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
commands += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
net_connect.disconnect()

print(commands)
