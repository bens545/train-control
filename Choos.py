import serial
#import time

COM = "/dev/ttyUSB0"
SER = serial.Serial(port=COM, baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=None)

def addrH(addr):
    return 0xC0 + (addr >> 8)

def addrL(addr):
    return addr & 0xFF

def headlightOn(loco):
    SER.write(bytearray([0xA2, addrH(loco), addrL(loco), 0x07, 0x10]))
    return

def headlightOff(loco):
    SER.write(bytearray([0xA2, addrH(loco), addrL(loco), 0x07, 0x00]))
    return

def horn(loco):
    SER.write(bytearray([0xA2, addrH(loco), addrL(loco), 0x07, 0x01]))
    return

def forward(loco, speed):
    print(SER.write(bytearray([0xA2, addrH(loco), addrL(loco), 0x04, speed])))
    return

def reverse(loco, speed):
    SER.write(bytearray([0xA2, addrH(loco), addrL(loco), 0x03, speed]))
    return

def normalTurnout(turnout):
    SER.write(bytearray([0xAD, addrH(turnout), addrL(turnout), 0x03, 0]))
    return

def reverseTurnout(turnout):
    SER.write(bytearray([0xAD, addrH(turnout), addrL(turnout), 0x04, 0]))
    return

def macro(num):
    SER.write(bytearray([0xAD, 0, 0, 0x01, num]))
    return

def stop(loco):
    SER.write(bytearray([0xA2, addrH(loco), addrL(loco), 0x04, 0x00]))
    return

def main():
    pass

main()
