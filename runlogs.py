import os
import sys
from subprocess import call

os.chdir("/var/log/")
call('ls')
project = input("which project would you like to go to?\n")
os.chdir(project)
call('ls')
open("output.log")
os.system('tail -100f output.log')
os.system('cat')