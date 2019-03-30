#!/usr/bin/python3
import serial
import io

ser = serial.Serial("/dev/ttyUSB0", 9600, timeout=1)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
sio.write(str("A"))
sio.flush()
temperature = sio.read().strip()
print(temperature)
