#!/usr/bin/env python

# Python reverse dns script
# Goes through a list of ip addresses and tries to do a reverse lookup
import sys
import dns.resolver,dns.reversename

if len(sys.argv) < 3:
    print "Usage: ./rev.py iplist.txt dnsserver"
    exit()
else:
    pass

ipfile = open(sys.argv[1],"r").readlines()
dnsserver = sys.argv[2]
resolver = dns.resolver.Resolver()
# Set DNS Server
resolver.namerservers = [dnsserver]
for i in ipfile:
    try:
        i = i.rstrip()
        # Format the ip in reverse
        ip = '.'.join(reversed(i.split("."))) + ".in-addr.arpa"
        answer = resolver.query(ip, "PTR")
        for a in answer:
            print i, " - ",a
    except:
        continue
