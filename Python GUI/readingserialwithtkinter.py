from tkinter import *
import serial
from serial.serialutil import PortNotOpenError
import serial.tools.list_ports
from tkinter import filedialog


root=Tk()
root.title("chessgame")
root.geometry("500x500")

id = None
oldstr=""
fistcome=True
arduino= serial.Serial("COM5",9600)


def read(status=True):
    global id
    if (status==True):
        tdata=""
        while(len(tdata)!=64):
            data=arduino.read(1).decode('ascii')
            tdata+=data
        id=root.after(200,read)
        print(tdata)
    else:
        print("stopped")
        root.after_cancel(id)

    return 0

def stopread():
    read(False)
    return 0
    
    
def inter():
    name2 = Button(root, text="stop",
                    padx=5, pady=5, command=stopread)                  
    name2.pack()
    read()

but=Button(text="inter",command=inter)
but.pack()
root.mainloop()