from tkinter import *
import tkinter.font as font
import serial
from serial.serialutil import PortNotOpenError
import serial.tools.list_ports
from tkinter import filedialog


root = Tk()
root.title("chessgame")
root.geometry('550x550')

location = {"wRl": 0, "wNl": 1, "wBl": 2, "wQ": 3, "wK": 4, "wBr": 5, "wNr": 6, "wRr": 7, "wP1": 8, "wP2": 9, "wP3": 10, "wP4": 11, "wP5": 12, "wP6": 13, "wP7": 14, "wP8": 15,
            "bP1": 48, "bP2": 49, "bP3": 50, "bP4": 51, "bP5": 52, "bP6": 53, "bP7": 54, "bP8": 55, "bRl": 56, "bNl": 57, "bBl": 58, "bQ": 59, "bK": 60, "bBr": 61, "bNr": 62, "bRr": 63}

# var used in position name
col = ["a", "b", "c", "d", "e", "f", "g", "h"]

# var used in  Eval
id = None
oldstr = ""
firstcome = 1


# var Used in change
temp1 = None
temp2 = None
firststore = False
secondstore = False
cassnewposi = []
a = 0

# var used in movename
pawnpromotion = False
storemove = []  # store moves


# Gamestore
no = 0
Game = ""

# Game = '''1.e4 e6 2.d4 d5 3.Nd2 Nf6 4.e5 Nfd7 5.f4 c5 6.c3 Nc6 7.Ndf3 cxd4 8.cxd4 f6
# 9.Bd3 Bb4+ 10.Bd2 Qb6 11.Ne2 fxe5 12.fxe5 O-O 13.a3 Be7 14.Qc2 Rxf3 15.gxf3 Nxd4
# 16.Nxd4 Qxd4 17.O-O-O Nxe5 18.Bxh7+ Kh8 19.Kb1 Qh4 20.Bc3 Bf6 21.f4 Nc4 22.Bxf6 Qxf6
# 23.Bd3 b5 24.Qe2 Bd7 25.Rhg1 Be8 26.Rde1 Bf7 27.Rg3 Rc8 28.Reg1 Nd6 29.Rxg7 Nf5
# 30.R7g5 Rc7 31.Bxf5 exf5 32.Rh5+  1-0'''


# -----input box names----
val = ["event", "site", "date",
       "round",
       "wp",
       "bp"
       ]

# ------sotre data form input box---
vald = []

# -------label names------
Lname = ["Enter Event :", "Enter site :", "Enter Date :", "Enter Round :",
         "White Player :", "Black Player :"]

# ----variable names to display pgn file---
Nval = ["Event", "Site", "Date",
        "Round",
        "White",
        "Black",
        "Result"
        ]

connection = False
msg = ""
connectiontry = False
arduino = None


# -----------moves storing in game variable
def gamestore(win):
    global no
    global Game
    global storemove
    for b in range(len(storemove)):
        if(((b+1) % 2) != 0):
            no += 1
            p1 = str(no)+"."+storemove[b]
            int(no)
        else:
            p1 = storemove[b]
        Game = Game+p1+" "
    Game = Game+win
    print(Game)


# --------------select path to save the file----
def path():
    filename = filedialog.askdirectory()
    print(filename)
    pathf = filename.replace("/", "\\")
    return pathf

# -----------on click erase date box-------


def erase(event):
    val[2].delete(0, "end")
    return 0

# ------------final data submission--------


def submit():
    pathf = path()
    for i in range(len(val)):
        vald.insert(i, val[i].get())

    vald.append(win)
    gamestore(win)

    with open(r'%s' % (pathf)+"\\" + '%s' % (vald[0]) + "_" + '%s' % (vald[3]) + ".pgn", "w") as o:
        for a in range(len(Nval)):
            o.write('[%s "%s"]\n' % (Nval[a], vald[a]))

        o.write('%s\n\n' % (Game))
        o.close()

    # for i in range(len(val)):
    #     val[i].delete(0, "end")

    label = Label(root, text="Data saved sucessfully!", fg="red", pady=5)
    label.grid(row=11, column=0, columnspan=2, padx=15, pady=25)

    return 0


def isChecked():
    global win
    win = ""
    if w.get() == 1:
        win = "1-0"
    elif w.get() == 2:
        win = "0-1"
    elif w.get() == 3:
        win = "1/2-1/2"
    return 0


def positionname(position):
    row = str((position//8)+1)
    ncol = col[(position % 8)]
    posiname = ncol+row
    return posiname


def intersect(piece, oppositename):
    oldposi = positionname(location[piece])
    othersposi = positionname(location[oppositename])
    # check if they are not in same column
    if(oldposi[0] != othersposi[0]):
        start = piece[1] + oldposi[0]

    # if column true check for row
    elif(oldposi[1] != othersposi[1]):
        start = piece[1] + oldposi[1]

    # if both are true write whole position
    else:
        start = piece[1] + oldposi
    return start


root = Tk()
root.title("chessgame")
root.geometry('550x550')

location = {"wRl": 0, "wNl": 1, "wBl": 2, "wQ": 3, "wK": 4, "wBr": 5, "wNr": 6, "wRr": 7, "wP1": 8, "wP2": 9, "wP3": 10, "wP4": 11, "wP5": 12, "wP6": 13, "wP7": 14, "wP8": 15,
            "bP1": 48, "bP2": 49, "bP3": 50, "bP4": 51, "bP5": 52, "bP6": 53, "bP7": 54, "bP8": 55, "bRl": 56, "bNl": 57, "bBl": 58, "bQ": 59, "bK": 60, "bBr": 61, "bNr": 62, "bRr": 63}

# var used in position name
col = ["a", "b", "c", "d", "e", "f", "g", "h"]

# var used in  Eval
id = None
oldstr = ""
firstcome = 1


# var Used in change
temp1 = None
temp2 = None
firststore = False
secondstore = False
cassnewposi = []
a = 0

# var used in movename
pawnpromotion = False
storemove = []  # store moves


# Gamestore
no = 0
Game = ""

# Game = '''1.e4 e6 2.d4 d5 3.Nd2 Nf6 4.e5 Nfd7 5.f4 c5 6.c3 Nc6 7.Ndf3 cxd4 8.cxd4 f6
# 9.Bd3 Bb4+ 10.Bd2 Qb6 11.Ne2 fxe5 12.fxe5 O-O 13.a3 Be7 14.Qc2 Rxf3 15.gxf3 Nxd4
# 16.Nxd4 Qxd4 17.O-O-O Nxe5 18.Bxh7+ Kh8 19.Kb1 Qh4 20.Bc3 Bf6 21.f4 Nc4 22.Bxf6 Qxf6
# 23.Bd3 b5 24.Qe2 Bd7 25.Rhg1 Be8 26.Rde1 Bf7 27.Rg3 Rc8 28.Reg1 Nd6 29.Rxg7 Nf5
# 30.R7g5 Rc7 31.Bxf5 exf5 32.Rh5+  1-0'''


# -----input box names----
val = ["event", "site", "date",
       "round",
       "wp",
       "bp"
       ]

# ------sotre data form input box---
vald = []

# -------label names------
Lname = ["Enter Event :", "Enter site :", "Enter Date :", "Enter Round :",
         "White Player :", "Black Player :"]

# ----variable names to display pgn file---
Nval = ["Event", "Site", "Date",
        "Round",
        "White",
        "Black",
        "Result"
        ]

connection = False
msg = ""
connectiontry = False
arduino = None


# -----------moves storing in game variable
def gamestore(win):
    global no
    global Game
    global storemove
    for b in range(len(storemove)):
        if(((b+1) % 2) != 0):
            no += 1
            p1 = str(no)+"."+storemove[b]
            int(no)
        else:
            p1 = storemove[b]
        Game = Game+p1+" "
    Game = Game+win
    print(Game)


# --------------select path to save the file----
def path():
    filename = filedialog.askdirectory()
    print(filename)
    pathf = filename.replace("/", "\\")
    return pathf

# -----------on click erase date box-------


def erase(event):
    val[2].delete(0, "end")
    return 0

# ------------final data submission--------


def submit():
    pathf = path()
    for i in range(len(val)):
        vald.insert(i, val[i].get())

    vald.append(win)
    gamestore(win)

    with open(r'%s' % (pathf)+"\\" + '%s' % (vald[0]) + "_" + '%s' % (vald[3]) + ".pgn", "w") as o:
        for a in range(len(Nval)):
            o.write('[%s "%s"]\n' % (Nval[a], vald[a]))

        o.write('%s\n\n' % (Game))
        o.close()

    # for i in range(len(val)):
    #     val[i].delete(0, "end")

    label = Label(root, text="Data saved sucessfully!", fg="red", pady=5)
    label.grid(row=11, column=0, columnspan=2, padx=15, pady=25)

    return 0


def isChecked():
    global win
    win = ""
    if w.get() == 1:
        win = "1-0"
    elif w.get() == 2:
        win = "0-1"
    elif w.get() == 3:
        win = "1/2-1/2"
    return 0


def positionname(position):
    row = str((position//8)+1)
    ncol = col[(position % 8)]
    posiname = ncol+row
    return posiname


def intersect(piece, oppositename):
    oldposi = positionname(location[piece])
    othersposi = positionname(location[oppositename])
    # check if they are not in same column
    if(oldposi[0] != othersposi[0]):
        start = piece[1] + oldposi[0]

    # if column true check for row
    elif(oldposi[1] != othersposi[1]):
        start = piece[1] + oldposi[1]

    # if both are true write whole position
    else:
        start = piece[1] + oldposi
    return start


def rookpath(cposi, piece):
    # get changed postion and name of rook
    a = 1
    b = 1
    c = 1
    d = 1
    arr = []
    found = False
    pfound = False
    empty = True

    # finding other Rook position
    if(piece[2] == "r"):
        oppositename = piece[0:2]+"l"
        if oppositename in location.keys():
            found = True

    else:
        oppositename = piece[0:2]+"r"
        if oppositename in location.keys():
            found = True

    if(found):
        pos = location[oppositename]

        # find its row location
        row = ((pos//8)+1)
        # all positions of the same row
        while(((pos+a)//8)+1 == row):
            arr.append(pos+a)
            if((pos+a) == cposi):
                pfound = True
                break
            a += 1

        if(pfound == False):
            arr.clear()

        while((((pos-b)//8)+1 == row) and pfound == False):
            arr.append(pos-b)
            if((pos-b) == cposi):
                pfound = True
            b += 1

        if(pfound == False):
            arr.clear()

        # add all postions of the same column
        while((pos+(8*c) < 64) and pfound == False):
            arr.append(pos+(8*c))
            if((pos+(8*c)) == cposi):
                pfound = True
            c += 1

        if(pfound == False):
            arr.clear()

        while((pos-(8*d) >= 0) and pfound == False):
            arr.append(pos-(8*d))
            if((pos-(8*d)) == cposi):
                pfound = True
            d += 1

        if(pfound == False):
            arr.clear()

    for i in arr:
        if i in location.values():
            empty = False

    # if changed position of first knight is in path of otherkinght
    if pfound and empty:
        start = intersect(piece, oppositename)

    # if not in other Knights position
    # no need to add any suffix
    else:
        start = piece[1]

    return start


def knightpath(cposi, piece):
    # getting the changed position and name of knight
    found = False
    arr = []
    # finding other Kinght position
    if(piece[2] == "r"):
        oppositename = piece[0:2]+"l"
        if oppositename in location.keys():
            pos = location[oppositename]
            found = True
    else:
        oppositename = piece[0:2]+"r"
        if oppositename in location.keys():
            pos = location[oppositename]
            found = True

    # findign all possibel paths of the other knight
    if(found == True):
        row = ((pos//8)+1)
        if(((pos-2)//8)+1 == row):
            if(pos-8 >= 0):
                arr.append(pos-10)
            if(pos+8 < 64):
                arr.append(pos+6)

        if(((pos-1)//8)+1 == row):
            if(pos-16 >= 0):
                arr.append(pos-17)
            if(pos+16 < 64):
                arr.append(pos+15)

        if(((pos+1)//8)+1 == row):
            if(pos-16 >= 0):
                arr.append(pos-15)
            if(pos+16 < 64):
                arr.append(pos+17)

        if(((pos+2)//8)+1 == row):
            if(pos-8 >= 0):
                arr.append(pos-6)
            if(pos+8 < 64):
                arr.append(pos+10)

    # if changed position of first knight is in path of otherkinght
    if cposi in arr:
        start = intersect(piece, oppositename)

    # if not in other Knights position
    # no need to add any suffix
    else:
        start = piece[1]

    return start


def movename(piece, move, cposition):
    # piece name its move and its new or changed location

    global pawnpromotion
    global storemove

    # name of changed postion
    cposiname = positionname(cposition)

    # if normal change is done
    if(move == "change"):
        # for pawn
        if(piece[1] == "P"):
            # By normal change pawn gets promoted
            if(cposition > 55 or cposition < 8):
                # print(cposiname+"=Q")
                storemove.append(cposiname+"=Q")
                print(storemove)
                pawnpromotion = True
                if(piece[0] == "w"):
                    location.update({"wQ1": cposition})
                else:
                    location.update({"bQ1": cposition})

            # else write only changed position name
            else:
                # print(cposiname)
                storemove.append(cposiname)
                print(storemove)

        # for king
        elif(piece[1] == "K"):
            # wirte k nad changed postion name
            # print(piece[1]+cposiname)
            storemove.append(piece[1]+cposiname)
            print(storemove)

        # for Queen
        elif(piece[1] == "Q"):
            # wirte Q nad changed postion name
            # print(piece[1]+cposiname)
            storemove.append(piece[1]+cposiname)
            print(storemove)

        # for bishop
        elif(piece[1] == "B"):
            # wirte B nad changed postion name
            # print(piece[1]+cposiname)
            storemove.append(piece[1]+cposiname)
            print(storemove)

        # for Knight check wheater the changed positon is in other knights path
        elif(piece[1] == "N"):
            # get the prefix depending on condition
            start = knightpath(cposition, piece)
            # final postion
            finalposi = start+cposiname
            # print(finalposi)
            storemove.append(finalposi)
            print(storemove)

        # for Rook
        elif(piece[1] == "R"):
            # get the prefix depending on condition
            start = rookpath(cposition, piece)
            # final postion
            finalposi = start+cposiname
            # print(finalposi)
            storemove.append(finalposi)
            print(storemove)

    elif(move == "killed"):

        if(piece[1] == "P"):
            pawnposi = positionname(location[piece])

            if(cposition > 55 or cposition < 8):
                # print(pawnposi[0]+"x"+cposiname+"=Q")
                storemove.append(pawnposi[0]+"x"+cposiname+"=Q")
                print(storemove)
                pawnpromotion = True
                if(piece[0] == "w"):
                    location.update({"wQ1": cposition})
                else:
                    location.update({"bQ1": cposition})
            else:
                # print(pawnposi[0]+"x"+cposiname)
                storemove.append(pawnposi[0]+"x"+cposiname)
                print(storemove)

        elif(piece[1] == "N"):
            start = knightpath(cposition, piece)
            finalposi = start+"x"+cposiname
            # print(finalposi)
            storemove.append(finalposi)
            print(storemove)

        elif(piece[1] == "R"):
            start = rookpath(cposition, piece)
            finalposi = start+"x"+cposiname
            # print(finalposi)
            storemove.append(finalposi)
            print(storemove)

        # for king
        elif(piece[1] == "K"):
            # wirte k nad changed postion name
            # print(piece[1]+"x"+cposiname)
            storemove.append(piece[1]+"x"+cposiname)
            print(storemove)

        # for Queen
        elif(piece[1] == "Q"):
            # wirte Q nad changed postion name
            # print(piece[1]+"x"+cposiname)
            storemove.append(piece[1]+"x"+cposiname)
            print(storemove)

        # for bishop
        elif(piece[1] == "B"):
            # wirte B nad changed postion name
            # print(piece[1]+"x"+cposiname)
            storemove.append(piece[1]+"x"+cposiname)
            print(storemove)
    return 0


def change(pos):
    global temp1
    global temp2
    global firststore
    global secondstore
    global pawnpromotion
    global cassnewposi
    global storemove

    Found = False

    # print(firststore,secondstore)
    for key, val in location.items():
        if (val == pos):
            Found = True
            # first variable has value
            if(firststore == True):
                temp2 = key
                firststore = False
                if(temp1 == temp2):
                    break
                secondstore = True

            # both variable has value and kill operation (third in data base)
            elif (secondstore == True):
                secondstore = False

                # findout who killed who
                if(location[temp2] == pos):
                    movename(temp1, "killed", location[temp2])
                    location[temp1] = location[temp2]
                    del location[temp2]

                    if(pawnpromotion == True):
                        del location[temp1]
                        pawnpromotion = False

                elif(location[temp1] == pos):
                    movename(temp2, "killed", location[temp1])
                    location[temp2] = location[temp1]
                    del location[temp1]

                    if(pawnpromotion == True):
                        del location[temp1]
                        pawnpromotion = False

            # fist variable is empty
            else:
                firststore = True
                temp1 = key

            break

    if(not Found):
        if(firststore == False and secondstore == True):
            cassnewposi.append(pos)
            if(len(cassnewposi) == 2):
                # movename(temp1,"casseled",temp2)
                if(temp1.find("R") != -1):
                    (temp1, temp2) = (temp2, temp1)

                if(temp2[2] == "l"):
                    if cassnewposi[0] < cassnewposi[1]:
                        location[temp1] = cassnewposi[0]
                        location[temp2] = cassnewposi[1]
                    else:
                        location[temp1] = cassnewposi[1]
                        location[temp2] = cassnewposi[0]
                    # print("o-o-o")
                    storemove.append("o-o-o")
                    print(storemove)
                if(temp2[2] == "r"):
                    if cassnewposi[0] > cassnewposi[1]:
                        location[temp1] = cassnewposi[0]
                        location[temp2] = cassnewposi[1]
                    else:
                        location[temp1] = cassnewposi[1]
                        location[temp2] = cassnewposi[0]
                    # print("o-o")
                    storemove.append("o-o")
                    print(storemove)

                cassnewposi.clear()
                secondstore = False

        else:
            movename(temp1, "change", pos)
            location[temp1] = pos
            firststore = False
            if(pawnpromotion == True):
                del location[temp1]
                pawnpromotion = False

    return 0


def eval(inputdata):
    global oldstr
    global firstcome
    newstr = inputdata
    pos = []

    if(firstcome == 2):
        pos = [i for i in range(len(newstr))if oldstr[i] != newstr[i]]
        if(len(pos) != 0):
            change(pos[0])

    # putnewstr into oldstr
    oldstr = newstr
    firstcome = 2

    return 0


def read(status=True):
    global id
    if (status == True):
        tdata = ""
        tdata = arduino.readline().decode("ascii")
        # while(len(tdata)!=64):
        #     data=arduino.read(1).decode('ascii')
        #     tdata+=data
        id = root.after(10, read)
        # print(tdata)
        # eval(tdata)

        if len(tdata) == 65:
            print(tdata)
            eval(tdata)
    else:
        print("stopped")
        root.after_cancel(id)

    return 0

# This function is integrated in results
# def stopread():
#     read(False)
#     return 0
# -------------save results-----


def results():
    read(False)
    global w
    w = IntVar()
    c1 = Radiobutton(root, text="White", variable=w,
                     value=1, command=lambda: isChecked())
    c1.grid(row=3, column=1, padx=15, pady=10)
    c2 = Radiobutton(root, text="Black", variable=w,
                     value=2, command=lambda: isChecked())
    c2.grid(row=4, column=1, padx=15, pady=10)
    c3 = Radiobutton(root, text="Draw", variable=w,
                     value=3, command=lambda: isChecked())
    c3.grid(row=5, column=1, padx=15, pady=10)

    mybutton = Button(root, text="Save",
                      padx=5, pady=5, activebackground='red', bd=3, command=submit)
    mybutton.grid(row=4, column=0, padx=15, pady=25)
    return 0
# --------------third page---------


def thirdpage():
    for q in range(len(Lname)):
        Lname[q].grid_forget()
        val[q].grid_forget()
    global mybutton
    mybutton.grid_forget()

    recordmsg = Label(root, text="Game being recorded",
                      font=("Arial Bold", 18), fg='red')
    recordmsg.grid(row=0, column=1, padx=15, pady=25)

    # end game
    mybutton = Button(root, text="Game Ended",
                      padx=5, pady=5, command=results)
    mybutton.grid(row=2, column=1, padx=15, pady=25)
    read()

    return 0

# -------second page------


def secondpage():
    name.grid_forget()
    name1.grid_forget()
    name2.grid_forget()
    name3.grid_forget()

    global mybutton

    # creatin label
    for q in range(len(Lname)):
        Lname[q] = Label(root, text="%s" % (Lname[q]))
        Lname[q].grid(row=q, column=0, padx=10, pady=10)
        val[q] = Entry(root, width=20, borderwidth=2)
        val[q].grid(row=q, column=1, padx=10, pady=10)

    val[2].insert(0, "dd.mm.yyyy")
    val[2].bind("<Button-1>", erase)

    # Button
    mybutton = Button(root, text="Start the game",
                      padx=5, pady=5, activebackground='red', bd=3, command=thirdpage)
    mybutton.grid(row=10, column=0, padx=15, pady=25)

    return 0
# ----------port scanning ---------


def portscan():
    global connection
    global msg
    global connectiontry
    global arduino

    if (connectiontry):
        name2.grid_forget()

    ports = list(serial.tools.list_ports.comports())
    for p in ports:

        if ("Arduino" in p.description) or ("USB Serial Device" in p.description):
            portno = p.name
            connection = True

    if connection == True:
        arduino = serial.Serial(portno, 9600)
        msg = "Connection is OK"
        connectiontry = True
    else:
        msg = "Try Again"
        connectiontry = True

    return connection

# --------check and display status----


def checkconnection():
    connect = portscan()
    global name2
    global name3

    name2 = Label(root, text="%s" % (msg), font=("Arial Bold", 16), fg='blue')
    name2.grid(row=2, column=1, padx=15, pady=25, )

    if (connect == True):
        name3 = Button(root, text="next",
                       padx=5, pady=5, activebackground='yellow', bd=3, command=secondpage, font=font.Font(family='Courier', size=14, weight='bold'))
        name3.grid(row=3, column=1, padx=15, pady=25)
    return 0


# -------------first page ---------------------------
name = Label(root, text="Welcome !!!", font=("Arial Bold", 18), fg='red')
name.grid(row=0, column=1, padx=15, pady=25)

name1 = Button(root, text="Check Connection",
               padx=5, pady=5, activebackground='green', bd=3, command=checkconnection, font=font.Font(family='Helvetica', size=14, weight='bold'))
name1.grid(row=1, column=1, padx=15, pady=25)

root.mainloop()


def knightpath(cposi, piece):
    # getting the changed position and name of knight
    found = False
    arr = []
    # finding other Kinght position
    if(piece[2] == "r"):
        oppositename = piece[0:2]+"l"
        if oppositename in location.keys():
            pos = location[oppositename]
            found = True
    else:
        oppositename = piece[0:2]+"r"
        if oppositename in location.keys():
            pos = location[oppositename]
            found = True

    # findign all possibel paths of the other knight
    if(found == True):
        row = ((pos//8)+1)
        if(((pos-2)//8)+1 == row):
            if(pos-8 >= 0):
                arr.append(pos-10)
            if(pos+8 < 64):
                arr.append(pos+6)

        if(((pos-1)//8)+1 == row):
            if(pos-16 >= 0):
                arr.append(pos-17)
            if(pos+16 < 64):
                arr.append(pos+15)

        if(((pos+1)//8)+1 == row):
            if(pos-16 >= 0):
                arr.append(pos-15)
            if(pos+16 < 64):
                arr.append(pos+17)

        if(((pos+2)//8)+1 == row):
            if(pos-8 >= 0):
                arr.append(pos-6)
            if(pos+8 < 64):
                arr.append(pos+10)

    # if changed position of first knight is in path of otherkinght
    if cposi in arr:
        start = intersect(piece, oppositename)

    # if not in other Knights position
    # no need to add any suffix
    else:
        start = piece[1]

    return start


def movename(piece, move, cposition):
    # piece name its move and its new or changed location

    global pawnpromotion
    global storemove

    # name of changed postion
    cposiname = positionname(cposition)

    # if normal change is done
    if(move == "change"):
        # for pawn
        if(piece[1] == "P"):
            # By normal change pawn gets promoted
            if(cposition > 55 or cposition < 8):
                # print(cposiname+"=Q")
                storemove.append(cposiname+"=Q")
                print(storemove)
                pawnpromotion = True
                if(piece[0] == "w"):
                    location.update({"wQ1": cposition})
                else:
                    location.update({"bQ1": cposition})

            # else write only changed position name
            else:
                # print(cposiname)
                storemove.append(cposiname)
                print(storemove)

        # for king
        elif(piece[1] == "K"):
            # wirte k nad changed postion name
            # print(piece[1]+cposiname)
            storemove.append(piece[1]+cposiname)
            print(storemove)

        # for Queen
        elif(piece[1] == "Q"):
            # wirte Q nad changed postion name
            # print(piece[1]+cposiname)
            storemove.append(piece[1]+cposiname)
            print(storemove)

        # for bishop
        elif(piece[1] == "B"):
            # wirte B nad changed postion name
            # print(piece[1]+cposiname)
            storemove.append(piece[1]+cposiname)
            print(storemove)

        # for Knight check wheater the changed positon is in other knights path
        elif(piece[1] == "N"):
            # get the prefix depending on condition
            start = knightpath(cposition, piece)
            # final postion
            finalposi = start+cposiname
            # print(finalposi)
            storemove.append(finalposi)
            print(storemove)

        # for Rook
        elif(piece[1] == "R"):
            # get the prefix depending on condition
            start = rookpath(cposition, piece)
            # final postion
            finalposi = start+cposiname
            # print(finalposi)
            storemove.append(finalposi)
            print(storemove)

    elif(move == "killed"):

        if(piece[1] == "P"):
            pawnposi = positionname(location[piece])

            if(cposition > 55 or cposition < 8):
                # print(pawnposi[0]+"x"+cposiname+"=Q")
                storemove.append(pawnposi[0]+"x"+cposiname+"=Q")
                print(storemove)
                pawnpromotion = True
                if(piece[0] == "w"):
                    location.update({"wQ1": cposition})
                else:
                    location.update({"bQ1": cposition})
            else:
                # print(pawnposi[0]+"x"+cposiname)
                storemove.append(pawnposi[0]+"x"+cposiname)
                print(storemove)

        elif(piece[1] == "N"):
            start = knightpath(cposition, piece)
            finalposi = start+"x"+cposiname
            # print(finalposi)
            storemove.append(finalposi)
            print(storemove)

        elif(piece[1] == "R"):
            start = rookpath(cposition, piece)
            finalposi = start+"x"+cposiname
            # print(finalposi)
            storemove.append(finalposi)
            print(storemove)

        # for king
        elif(piece[1] == "K"):
            # wirte k nad changed postion name
            # print(piece[1]+"x"+cposiname)
            storemove.append(piece[1]+"x"+cposiname)
            print(storemove)

        # for Queen
        elif(piece[1] == "Q"):
            # wirte Q nad changed postion name
            # print(piece[1]+"x"+cposiname)
            storemove.append(piece[1]+"x"+cposiname)
            print(storemove)

        # for bishop
        elif(piece[1] == "B"):
            # wirte B nad changed postion name
            # print(piece[1]+"x"+cposiname)
            storemove.append(piece[1]+"x"+cposiname)
            print(storemove)
    return 0


def change(pos):
    global temp1
    global temp2
    global firststore
    global secondstore
    global pawnpromotion
    global cassnewposi
    global storemove

    Found = False

    # print(firststore,secondstore)
    for key, val in location.items():
        if (val == pos):
            Found = True
            # first variable has value
            if(firststore == True):
                temp2 = key
                secondstore = True
                firststore = False

            # both variable has value and kill operation (third in data base)
            elif (secondstore == True):
                secondstore = False

                # findout who killed who
                if(location[temp2] == pos):
                    movename(temp1, "killed", location[temp2])
                    location[temp1] = location[temp2]
                    del location[temp2]

                    if(pawnpromotion == True):
                        del location[temp1]
                        pawnpromotion = False

                elif(location[temp1] == pos):
                    movename(temp2, "killed", location[temp1])
                    location[temp2] = location[temp1]
                    del location[temp1]

                    if(pawnpromotion == True):
                        del location[temp1]
                        pawnpromotion = False

            # fist variable is empty
            else:
                firststore = True
                temp1 = key

            break

    if(not Found):
        if(firststore == False and secondstore == True):
            cassnewposi.append(pos)
            if(len(cassnewposi) == 2):
                # movename(temp1,"casseled",temp2)
                if(temp1.find("R") != -1):
                    (temp1, temp2) = (temp2, temp1)

                if(temp2[2] == "l"):
                    if cassnewposi[0] < cassnewposi[1]:
                        location[temp1] = cassnewposi[0]
                        location[temp2] = cassnewposi[1]
                    else:
                        location[temp1] = cassnewposi[1]
                        location[temp2] = cassnewposi[0]
                    # print("o-o-o")
                    storemove.append("o-o-o")
                    print(storemove)
                if(temp2[2] == "r"):
                    if cassnewposi[0] > cassnewposi[1]:
                        location[temp1] = cassnewposi[0]
                        location[temp2] = cassnewposi[1]
                    else:
                        location[temp1] = cassnewposi[1]
                        location[temp2] = cassnewposi[0]
                    # print("o-o")
                    storemove.append("o-o")
                    print(storemove)

                cassnewposi.clear()
                secondstore = False

        else:
            movename(temp1, "change", pos)
            location[temp1] = pos
            firststore = False
            if(pawnpromotion == True):
                del location[temp1]
                pawnpromotion = False

    return 0


def eval(inputdata):
    global oldstr
    global firstcome
    newstr = inputdata
    pos = []

    if(firstcome == 2):
        pos = [i for i in range(len(newstr))if oldstr[i] != newstr[i]]
        if(len(pos) != 0):
            change(pos[0])

    # putnewstr into oldstr
    oldstr = newstr
    firstcome = 2

    return 0


def read(status=True):
    global id
    if (status == True):
        tdata = ""
        tdata = arduino.readline().decode("ascii")
        # while(len(tdata)!=64):
        #     data=arduino.read(1).decode('ascii')
        #     tdata+=data
        id = root.after(10, read)
        # print(tdata)
        # eval(tdata)

        if len(tdata) == 65:
            print(tdata)
            eval(tdata)
    else:
        print("stopped")
        root.after_cancel(id)

    return 0

# This function is integrated in results
# def stopread():
#     read(False)
#     return 0
# -------------save results-----


def results():
    read(False)
    global w
    w = IntVar()
    c1 = Radiobutton(root, text="White", variable=w,
                     value=1, command=lambda: isChecked())
    c1.grid(row=3, column=1, padx=15, pady=10)
    c2 = Radiobutton(root, text="Black", variable=w,
                     value=2, command=lambda: isChecked())
    c2.grid(row=4, column=1, padx=15, pady=10)
    c3 = Radiobutton(root, text="Draw", variable=w,
                     value=3, command=lambda: isChecked())
    c3.grid(row=5, column=1, padx=15, pady=10)

    mybutton = Button(root, text="Save",
                      padx=5, pady=5, activebackground='red', bd=3, command=submit)
    mybutton.grid(row=4, column=0, padx=15, pady=25)
    return 0
# --------------third page---------


def thirdpage():
    for q in range(len(Lname)):
        Lname[q].grid_forget()
        val[q].grid_forget()
    global mybutton
    mybutton.grid_forget()

    recordmsg = Label(root, text="Game being recorded",
                      font=("Arial Bold", 18), fg='red')
    recordmsg.grid(row=0, column=1, padx=15, pady=25)

    # end game
    mybutton = Button(root, text="Game Ended",
                      padx=5, pady=5, command=results)
    mybutton.grid(row=2, column=1, padx=15, pady=25)
    read()

    return 0

# -------second page------


def secondpage():
    name.grid_forget()
    name1.grid_forget()
    name2.grid_forget()
    name3.grid_forget()

    global mybutton

    # creatin label
    for q in range(len(Lname)):
        Lname[q] = Label(root, text="%s" % (Lname[q]))
        Lname[q].grid(row=q, column=0, padx=10, pady=10)
        val[q] = Entry(root, width=20, borderwidth=2)
        val[q].grid(row=q, column=1, padx=10, pady=10)

    val[2].insert(0, "dd.mm.yyyy")
    val[2].bind("<Button-1>", erase)

    # Button
    mybutton = Button(root, text="Start the game",
                      padx=5, pady=5, activebackground='red', bd=3, command=thirdpage)
    mybutton.grid(row=10, column=0, padx=15, pady=25)

    return 0
# ----------port scanning ---------


def portscan():
    global connection
    global msg
    global connectiontry
    global arduino

    if (connectiontry):
        name2.grid_forget()

    ports = list(serial.tools.list_ports.comports())
    for p in ports:

        if ("Arduino" in p.description) or ("USB Serial Device" in p.description):
            portno = p.name
            connection = True

    if connection == True:
        arduino = serial.Serial(portno, 9600)
        msg = "Connection is OK"
        connectiontry = True
    else:
        msg = "Try Again"
        connectiontry = True

    return connection

# --------check and display status----


def checkconnection():
    connect = portscan()
    global name2
    global name3

    name2 = Label(root, text="%s" % (msg), font=("Arial Bold", 16), fg='blue')
    name2.grid(row=2, column=1, padx=15, pady=25, )

    if (connect == True):
        name3 = Button(root, text="next",
                       padx=5, pady=5, activebackground='yellow', bd=3, command=secondpage, font=font.Font(family='Courier', size=14, weight='bold'))
        name3.grid(row=3, column=1, padx=15, pady=25)
    return 0


# -------------first page ---------------------------
name = Label(root, text="Welcome !!!", font=("Arial Bold", 18), fg='red')
name.grid(row=0, column=1, padx=15, pady=25)

name1 = Button(root, text="Check Connection",
               padx=5, pady=5, activebackground='green', bd=3, command=checkconnection, font=font.Font(family='Helvetica', size=14, weight='bold'))
name1.grid(row=1, column=1, padx=15, pady=25)

root.mainloop()
