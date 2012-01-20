#!/usr/bin/env python
import serial
import time

ser = serial.Serial(port="/dev/ttyUSB0")
ser.flush()
ser.setDTR()
ser.setDTR(False)
ser.close()

