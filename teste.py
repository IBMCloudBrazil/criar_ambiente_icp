#!/usr/bin/python 
import os
import subprocess

def sl_ready( vs ):
   "slcli"
   output = subprocess.check_output("slcli vs ready " + vs, shell=True)
   return (output)

sl_ready("icp01-jmbarros").rstrip()
