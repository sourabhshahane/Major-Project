
from tkinter import filedialog
from tkinter import *


root = Tk()
root.title("chessGame")
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

    with open(r'%s' % (pathf)+"\demo.txt", "w") as o:
        for a in range(len(Nval)):
            o.write('[%s "%s"]\n' % (Nval[a], vald[a]))

        o.write('%s\n\n' % (Game))
        o.close()

    for i in range(len(val)):
        val[i].delete(0, "end")

    label = Label(root, text="Data saved sucessfully!", fg="red", pady=5)
    label.grid(row=11, column=0, columnspan=2, padx=15, pady=25)

    return 0


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


root.mainloop()
