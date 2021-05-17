from tkinter import *
import serial
from serial.serialutil import PortNotOpenError
import serial.tools.list_ports
from tkinter import filedialog


root=Tk()
root.title("chessgame")
root.geometry("500x500")

location={"wRl":0,"wNl":1,"wBl":2,"wQ":3,"wK":4,"wBr":5,"wNr":6,"wRr":7,"wP1":8,"wP2":9,"wP3":10,"wP4":11,"wP5":12,"wP6":13,"wP7":14,"wP8":15,"bP1":48,"bP2":49,"bP3":50,"bP4":51,"bP5":52,"bP6":53,"bP7":54,"bP8":55,"bRl":56,"bNl":57,"bBl":58,"bQ":59,"bK":60,"bBr":61,"bNr":62,"bRr":63}



arduino= serial.Serial("COM5",9600)

def read(status=True):
    global id
    if (status==True):
        tdata=""
        tdata=arduino.readline().decode("ascii")
        # while(len(tdata)!=5):
        #     data=arduino.read(1).decode('ascii')
        #     tdata+=data
        id=root.after(250,read)
        # eval(tdata)    
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
    return 0

but=Button(text="inter",command=inter)
but.pack()
root.mainloop()