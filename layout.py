"""


file: layout.py
author: Ben Shaner
created: April 2017
"""
import time

def normalTurnout(turnout):
    SER.write(bytearray([0xAD, 0x01, 0x2E, 0x03, 0])) #302
    print(SER.read)
    time.sleep(2)

def reverseTurnout(turnout):
    SER.write(bytearray([0xAD, 0x01, 0x2E, 0x04, 0])) #302
    print(SER.read)
    time.sleep(2)

def macro(num):
    n = SER.write(bytearray([0xAD, 0x01, 0x2E, 0x01, num])) #
    print(n)
    print(SER.read)
    time.sleep(2)