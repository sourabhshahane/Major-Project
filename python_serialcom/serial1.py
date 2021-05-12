
# Code written assuming println() function in arduino

import serial
import serial.tools.list_ports
connection = False

port = list(serial.tools.list_ports.comports())


def checkconnection():
    global connection
    for p in port:
        if "Arduino" in p.manufacturer:
            com = p.name
            connection = True

    if connection:
        arduino = serial.Serial(port=com, baudrate=9600)
        data = arduino.readline()
        return (data[:-2])

    else:
        return ('CONNECTION FAILED!!')


data = checkconnection()
print(data)
