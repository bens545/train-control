"""


file: control.py
author: Ben Shaner
created: April 2017
"""

import coms
import loco
import time

def setup(num):
	ser = coms.trackSerial("/dev/ttyUSB0")
	train = loco.loco(num, ser.ser)
	return train

def main():
	train = setup(5504)
	print("headlight on")
	train.headlightOn()
	train.forward(25)
	time.sleep(2)
	print("headlight off")
	train.forward(0)
	train.headlightOff()

main()