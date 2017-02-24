import serial
import time
# COM port to use. That can take any of the following forms:
# COM8 for Python Windows, /dev/com8 or /dev/ttyS7 for Cygwin, /dev/ttyS2 for Linux
COM = "/dev/ttyUSB0"
LOCO = 3358
LOCO_H = 0xC0 + (LOCO >> 8)
LOCO_L = LOCO & 0xFF
SER = serial.Serial(port=COM, baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=None)

def addrH(addr):
    return 0xC0 + (addr >> 8)

def addrL(addr):
    return addr & 0xFF

def headlightOn():
    SER.write(bytearray([0xA2, LOCO_H, LOCO_L, 0x07, 0x10]))
    time.sleep(2)

def headlightOff():
    SER.write(bytearray([0xA2, 205, 30, 0x07, 0x00]))
    time.sleep(2)

def forward(speed, loco):
    # NCE USB 0xA2 <adr H/L> 04 0..7F (forward 128) and 06 00 (estop forward), reply 1 byte status
    SER.write(bytearray([0xA2, addrH(loco), addrL(loco), 0x04, speed]))
    time.sleep(2)

def nomralTurnout(turnout):
    SER.write(bytearray([0xAD, addrH(turnout), addrL(turnout), 0x03, 0]))
    print(SER.read)
    time.sleep(2)

def reverseTurnout(turnout):
    SER.write(bytearray([0xAD, addrH(turnout), addrL(turnout), 0x04, 0]))
    print(SER.read)
    time.sleep(2)

def stop(loco):
    SER.write(bytearray([0xA2, addrH(loco), addrL(loco), 0x04, 0x00]))

def main():
    pass

main()
