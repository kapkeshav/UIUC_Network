import socket
import time
import math
import pymysql

import pyvisa as visa
from ThorlabsPM100 import ThorlabsPM100, USBTMC

inst = USBTMC(device="/dev/ttyp4")
inst1 = USBTMC(device="/dev/ttyp5")
powermeter = ThorlabsPM100(inst=inst)
powermeter1 = ThorlabsPM100(inst=inst1)

values = [0,0,0]
values1 = [0,0,0]
i = 0

while True:
    try:
        values[0] = i
        values[1] = str(time.ctime())
        values[2] = powermeter.read
        print(values)
        values1[0] = i
        values1[1] = str(time.ctime())
        values1[2] = powermeter1.read
        print(values1)
        i += 1
    except KeyboardInterrupt:
        print("")
        print("quit")
        break
