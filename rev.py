#!/usr/bin/env python

# Python reverse dns script
# Goes through a list of ip addresses and tries to do a reverse lookup
import sys
import dns.resolver,dns.reversename
import re
from netaddr import *
from time import sleep

if len(sys.argv) < 3:
    print "Usage: ./rev.py iplist.txt dnsserver"
    exit()
else:
    pass

delay = raw_input("Delay in seconds (default = 0): ")
if delay == "" or delay == "0":
    delay = 0
else:
    delay = int(delay)
ipfile = open(sys.argv[1],"r").readlines()
dnsserver = sys.argv[2]
resolver = dns.resolver.Resolver()
# Set DNS Server
resolver.namerservers = [dnsserver]
for i in ipfile:
    try:
        # Match if the IP address is a range using CIDR
        if re.match('^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\/([0-9]|[1-2][0-9]|3[0-2]))$',i):
            for ip in IPNetwork(i):
                ip = str(ip).rstrip()
                # Format the ip in reverse
                ipaddr = '.'.join(reversed(ip.split("."))) + ".in-addr.arpa"
                answer = resolver.query(ipaddr, "PTR")
                for a in answer:
                    print ip, " - ",a
                # Sleep for specified amount of time
                sleep(delay)
        # If it's not a CIDR range, proceed with resolving
        else:
            i = i.rstrip()
            # Format the ip in reverse
            ip = '.'.join(reversed(i.split("."))) + ".in-addr.arpa"
            answer = resolver.query(ip, "PTR")
            for a in answer:
                print i, " - ",a
            # Sleep for specified amount of time
            sleep(delay)
    except:
        continue
