#!/usr/bin/python
#
# Example eAPI script to pull info from all nodes in the network
#
from jsonrpclib import Server
import ssl

# Ignore SSL connection warnings
try:
  _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
  pass
else:
  ssl._create_default_https_context = _create_unverified_https_context

# Vars

nodes = ["192.168.0.10", 
         "192.168.0.11",
         "192.168.0.14",
         "192.168.0.15",
         "192.168.0.16",
         "192.168.0.17"]

userid = "arista"
password = "arista"


print "\n"
print "Network Node Information"
print "-----------------------------------------------------------------------------------------------------------------------"
print "Node       IP Address      System MAC           Model           Uptime(s)  TotalMem   FreeMem    Version    Neighbors "
print "-----------------------------------------------------------------------------------------------------------------------"

# Loop through each node and gather info

for node in nodes:
   
   # Instantiate switch object
   RESTURL = "https://" + userid + ":" + password + "@" + node + "/command-api"
   switch = Server(RESTURL)

   # run command(s) against switch object
   # list of command output returned in a List (array) or JSON key:value pairs
   response = switch.runCmds(1, ["show hostname",
                                 "show version",
                                 "show ip interface Management1",
                                 "show lldp neighbors"])

   hostname = response[0]["hostname"]
   systemMac = response[1]["systemMacAddress"]
   model = response[1]["modelName"]
   totalMem = response[1]["memTotal"]
   freeMem = response[1]["memFree"]
   eosVersion = response[1]["version"]
   uptime = response[1]["uptime"]
   mgmtip = response[2]["interfaces"]["Management1"]["interfaceAddress"]["primaryIp"]["address"]
   lldpNeighbors = response[3]["lldpNeighbors"]
   numLldpNeighbors = len(lldpNeighbors)

   print ("%-10s %-15s %-20s %-15s %-10s %-10s %-10s %-10s %-10s") % (hostname, mgmtip, systemMac, model, uptime, totalMem, freeMem, eosVersion, numLldpNeighbors)

# end of loop

print "\n"
