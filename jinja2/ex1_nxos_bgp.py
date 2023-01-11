from jinja2 import Template

bgp_config = """
router bgp {{ local_as }}
  neighbor {{ peer1 }} remote-as {{ peer1_as }}
    update-source loopback99
    ebgp-multihop 2
    address-family ipv4 unicast
  neighbor {{ peer2}} remote-as {{ peer2_as }}
    address-family ipv4 unicast
"""
bgp_vars ={
    "local_as": 10,
    "peer1": "10.1.20.2",
    "peer1_as": 20,
    "peer2": "10.1.30.2",
    "peer1_as": 30,
}

bgp_template = bgp_config
j2_template = Template(bgp_template)
output = j2_template.render(**bgp_vars)
print(output)