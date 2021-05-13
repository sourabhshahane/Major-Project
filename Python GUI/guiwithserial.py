from tkinter import *
import serial
from serial.serialutil import PortNotOpenError
import serial.tools.list_ports
from tkinter import filedialog


root = Tk()
root.title("chessgame")
root.geometry('500x500')

Game = '''1.e4 e6 2.d4 d5 3.Nd2 Nf6 4.e5 Nfd7 5.f4 c5 6.c3 Nc6 7.Ndf3 cxd4 8.cxd4 f6
9.Bd3 Bb4+ 10.Bd2 Qb6 11.Ne2 fxe5 12.fxe5 O-O 13.a3 Be7 14.Qc2 Rxf3 15.gxf3 Nxd4
16.Nxd4 Qxd4 17.O-O-O Nxe5 18.Bxh7+ Kh8 19.Kb1 Qh4 20.Bc3 Bf6 21.f4 Nc4 22.Bxf6 Qxf6
23.Bd3 b5 24.Qe2 Bd7 25.Rhg1 Be8 26.Rde1 Bf7 27.Rg3 Rc8 28.Reg1 Nd6 29.Rxg7 Nf5
30.R7g5 Rc7 31.Bxf5 exf5 32.Rh5+  1-0'''


val = ["event", "site", "date",
       "round",
       "wp",
       "bp",
       "result",
       "welo",
       "belo", "eco"]

vald = []

Nval = ["Event", "Site", "Date",
        "Round",
        "White",
        "Black",
        "Result",
        "WhiteElo",
        "BlackElo", "ECO"]

connection = False
msg=""

  

def path():
    filename = filedialog.askdirectory()
    print(filename)
    pathf = filename.replace("/", "\\")
    return pathf


def erase(event):
    val[2].delete(0, "end")
    return 0


def submit():
    pathf = path()
    for i in range(len(val)):
        vald.insert(i, val[i].get())

    with open(r'%s' % (pathf)+"\\" + '%s' % (vald[0]) + "_" + '%s' % (vald[3]) + ".pgn", "w") as o:
        for a in range(len(Nval)):
            o.write('[%s "%s"]\n' % (Nval[a], vald[a]))

        o.write('%s\n\n' % (Game))
        o.close()

    for i in range(len(val)):
        val[i].delete(0, "end")

    label = Label(root, text="Data saved sucessfully!", fg="red", pady=5)
    label.grid(row=11, column=0, columnspan=2, padx=15, pady=25)

    return 0

def secondpage():
    name.grid_forget()
    name1.grid_forget()
    name2.grid_forget()
    name3.grid_forget()
    
    # label
    Lname = ["Enter Event :", "Enter site :", "Enter Date :", "Enter Round :",
            "White Player :", "Black Player :", "Result :", "WhiteElo :", "BlackElo :", "ECO :"]

    # creatin label
    for q in range(len(Lname)):
        Lname[q] = Label(root, text="%s" % (Lname[q]))
        Lname[q].grid(row=q, column=0, padx=5, pady=5)

    # Creating input box

    for i in range(len(val)):
        val[i] = Entry(root, width=20)
        val[i].grid(row=i, column=1, padx=5, pady=5)

    val[2].insert(0, "dd.mm.yyyy")
    val[2].bind("<Button-1>", erase)

    # Button
    mybutton = Button(root, text="Submit",
                    padx=5, pady=5, command=submit)
    mybutton.grid(row=10, column=0, padx=15, pady=25)


    return 0

def portscan():
    global connection
    global msg
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if "Arduino" in p.description:
            portno = p.name
            connection = True

    if connection == True:
        ard= serial.Serial(portno,9600)
        msg="connection is ok"

        # data = str(ard.readline())
        # print(data)
        # print(type(ard.readline()))
        # print(type(data))

    else:
        msg="connection failed"
    
    return connection  

def checkconnection():
    connect = portscan()
    global name2
    global name3

    name2= Label(root,text= "%s" % (msg))  
    name2.grid(row=2, column=0, padx=15, pady=25)
    
    if (connect==True):
        name3 = Button(root, text="next",
                  padx=5, pady=5, command=secondpage)
        name3.grid(row=3, column=0, padx=15, pady=25)
    return 0   
 
 
#-------------first page ___________________________
name= Label(root,text="welcome!!")  
name.grid(row=0, column=0, padx=15, pady=25)

name1 = Button(root, text="Check Connection",
                  padx=5, pady=5, command=checkconnection)
name1.grid(row=1, column=0, padx=15, pady=25)

root.mainloop()
