#!/usr/bin/env python

# Python reverse dns script
# Goes through a list of ip addresses and tries to do a reverse lookup

import socket
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
resolver.namerservers = [dnsserver]
for i in ipfile:
    try:
        i = i.rstrip()
        ip = '.'.join(reversed(i.split("."))) + ".in-addr.arpa"
        myAnswers = resolver.query(ip, "PTR")
        for a in myAnswers:
            print i, " - ",a
    except:
        continue
