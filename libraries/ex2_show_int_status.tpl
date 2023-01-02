Value PORT_NAME (\S+)
Value PORT_STATUS (\S+)
Value PORT_VLAN (\d+)
Value PORT_DUPLEX (\S+)
Value PORT_SPEED (\S+)
Value PORT_TYPE (\S+)

Start
  ^Port.*Type\s*$$ -> ShowIntTable

ShowIntTable
  ^${PORT_NAME}\s+${PORT_STATUS}\s+${PORT_VLAN}\s+${PORT_DUPLEX}\s+${PORT_SPEED}\s+${PORT_TYPE}$$ -> Record


# Port      Name               Status       Vlan       Duplex  Speed Type 
# Gi0/1/0                      notconnect   1            auto   auto 10/100/1000BaseTX
# Gi0/1/1                      notconnect   1            auto   auto 10/100/1000BaseTX
# Gi0/1/2                      notconnect   1            auto   auto 10/100/1000BaseTX
# Gi0/1/3                      notconnect   1            auto   auto 10/100/1000BaseTX