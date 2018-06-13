#!/usr/bin/python 
import socket
import fcntl
import struct
import os

def play_book ( pb, inv ):
  "run playbook"
  book = "ansible-playbook " + pb +  " -i " +  inv
  os.system(book)
  return

def hosts():
   "slcli"
   slcli = "slcli vs list | awk '{ print $3 }' > ./ip-hosts.txt" 
   os.system(slcli)
   return

hosts()
play_book( "./create-hosts.yml", "./ip-hosts.txt" )

