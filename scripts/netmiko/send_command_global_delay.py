from datetime import datetime
import os
from getpass import getpass
from netmiko import ConnectHandler

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

device = {
    "host": "nxos2.lasthop.io",
    "device_type": "cisco_nxos",
    "username": "pyclass",
    "password": password,
    "global_delay_factor": 2
}
command = "show lldp neighbors details"
net_connect = ConnectHandler(**device)

# use global delay factor
start_time = datetime.now()
output = net_connect.send_command(command)
net_connect.disconnect()
end_time = datetime.now()
print("#" * 80)
print(output)
print("#" * 80)
print("\n\nExecution Time: {}".format(end_time - start_time))
print()

# use local delay factor
start_time = datetime.now()
output = net_connect.send_command(command, delay_factor=8)
net_connect.disconnect()
end_time = datetime.now()
print("#" * 80)
print(output)
print("#" * 80)
print("\n\nExecution Time: {}".format(end_time - start_time))
print()
