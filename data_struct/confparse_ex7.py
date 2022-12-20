import yaml
from os import path
from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse
from pprint import pprint

if __name__ == "__main__":
    home_dir = path.expanduser("~")
    filename = path.join(home_dir, ".netmiko.yml")

    #with open(filename) as f:
    #    yaml_out = yaml.safe_load(f)

    bgp_config = """
    router bgp 44
     bgp router-id 10.220.88.38
     address-family ipv4 unicast
     !
     neighbor 10.220.88.20
      remote-as 42
      description pynet-rtr1
      address-family ipv4 unicast
      route-policy ALLOW in
      route-policy ALLOW out
      !
     !
     neighbor 10.220.88.32
      remote-as 43
      address-family ipv4 unicast
      route-policy ALLOW in
      route-policy ALLOW out
    """
    #device = yaml_out["cisco3"]
    #net_connect = ConnectHandler(**device)
    #show_run = net_connect.send_command("show run")

    # When feeding config directly - CiscoConfParse requires a list
    bgp_obj = CiscoConfParse(bgp_config.splitlines())
    bgp_peers = []
    neighbors = bgp_obj.find_objects_w_parents(
        parentspec=r"router bgp", childspec=r"neighbor"
    )
    for neighbor in neighbors:
        _, neighbor_ip = neighbor.text.split()
        for child in neighbor.children:
            if "remote-as" in child.text:
                _, remote_as = child.text.split()
        bgp_peers.append((neighbor_ip, remote_as))
    print()
    print("BGP Peers: ")
    pprint(bgp_peers)
    print()