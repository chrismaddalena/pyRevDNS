# pyRevDNS
Python reverse DNS script to obtain the hostnames from ips in a list :). Allows you to specify the DNS server IP. 

Usage:

`./rev.py iplist.txt dnsserver`

Install necessary libs: 

`pip install -r requirements.txt`

Output:

```
./rev.py ips.txt 8.8.8.8
216.239.32.10  -  ns1.google.com.
216.239.34.10  -  ns2.google.com.
```
