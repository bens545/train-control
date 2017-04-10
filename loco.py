"""


file: loco.py
author: Ben Shaner
created: April 2017

"""
import time

def addrH(addr):
	return 0xC0 + (addr >> 8)

def addrL(addr):
	return addr & 0xFF

class loco(object):
	def __init__(self, num, serial):
		self.locoH = addrH(num)
		self.locoL = addrL(num)
		self.serial = serial
		self.speed = 0

	def sleepTime(self):
		return 2

	def headlightOn(self):
		self.serial.write(bytearray([0xA2, self.locoH, self.locoL, 0x07, 0x10]))
		time.sleep(self.sleepTime())

	def headlightOff(self):
		self.serial.write(bytearray([0xA2, self.locoH, self.locoL, 0x07, 0x00]))
		time.sleep(self.sleepTime())

	def horn(self):
		self.serial.write(bytearray([0xA2, self.locoH, self.locoL, 0x07, 0x01]))
		time.sleep(self.sleepTime())

	def forward(self, speed):
		self.serial.write(bytearray([0xA2, self.locoH, self.locoL, 0x04, speed]))
		self.speed = speed
		time.sleep(self.sleepTime())

	def reverse(self, speed):
		self.serial.write(bytearray([0xA2, self.locoH, self.locoL, 0x03, speed]))
		self.speed = -1 * speed
		time.sleep(self.sleepTime())