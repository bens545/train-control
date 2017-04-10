"""


file: serial.py
author: Ben Shaner
created: April 2017

Portions of this file may be copied from other works written and submitted by the author.
"""

import serial

class trackSerial(object):
	def __init__(self, port):
		self.com = port
		self.ser = serial.Serial(port=self.com, baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=None)