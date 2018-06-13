#!/usr/bin/python 
import os
import subprocess
import time

ready = "waiting"

def sl_ready( vs ):
   "slcli"
   output = subprocess.check_output("slcli vs ready " + vs, shell=True)
   return (output)

def sl_ip( host ):
   "slcli"
   output = os.system("slcli vs detail " + host + " | grep public  | awk '{ print $2 }' >> ./ips.txt") 
   return (output)

with open('hosts.txt') as f:
    for line in f:
        print line.rstrip()
        while ready != 'READY':
            try:
                ready = sl_ready(line).rstrip()
               # while ready != 'READY':
                print "Wainting for " + line.rstrip() + " be ready ..."
                time.sleep(5)
                continue
            except:
                print line.rstrip() + " not ready"
                ready = sl_ready(line).rstrip()
                continue
#            else:
#                print line.rstrip() + " not ready"
#                ready = sl_ready(line).rstrip()
#                continue
        if 'str' in line:
            break

with open('hosts.txt') as f:
   for line in f:
       sl_ip(line.rstrip())
       #print line
       if 'str' in line:
          break 