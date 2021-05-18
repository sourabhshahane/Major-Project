from tkinter import *
import tkinter.font as font
import serial
from serial.serialutil import PortNotOpenError
import serial.tools.list_ports



ports = list(serial.tools.list_ports.comports())
for p in ports:
    print(p.description)