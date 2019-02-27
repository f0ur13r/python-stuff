#!/usr/bin/env python3

import subprocess

def ping(hostname):
        p = subprocess.Popen(["ping6", "-c", "2", hostname], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, err = p.communicate()
        result = p.returncode
        print("Pinging host", hostname, end=' ')
        if result == 0:
          print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
        elif result ==1:
          print('\x1b[6;30;41m' + 'Not reachable!' + '\x1b[0m')
        else:
          print('\x1b[6;30;43m' + 'Unknown error!' + '\x1b[0m')

#main
print("### Ping multiple hosts ### by kunalija")
print("######################################")
print("Reading hostnames from hostnames.txt...")

#read hostnames from file hostnames.txt
hostnames=[]
with open('hostnames.txt','r') as f:
         #hostnames = [line.strip() for line in f]
         for line in f:
           #ignore comments
           if line.startswith("#"):
             continue
           else:
             hostnames.append(line.strip())
 
for hostname in hostnames:
         ping(hostname)
