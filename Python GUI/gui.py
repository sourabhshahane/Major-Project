import tkinter as tk

# Creating window
root = tk.Tk()
root.title("chessGame")
root.geometry('500x500')

Game = '''1.e4 e6 2.d4 d5 3.Nd2 Nf6 4.e5 Nfd7 5.f4 c5 6.c3 Nc6 7.Ndf3 cxd4 8.cxd4 f6
9.Bd3 Bb4+ 10.Bd2 Qb6 11.Ne2 fxe5 12.fxe5 O-O 13.a3 Be7 14.Qc2 Rxf3 15.gxf3 Nxd4
16.Nxd4 Qxd4 17.O-O-O Nxe5 18.Bxh7+ Kh8 19.Kb1 Qh4 20.Bc3 Bf6 21.f4 Nc4 22.Bxf6 Qxf6
23.Bd3 b5 24.Qe2 Bd7 25.Rhg1 Be8 26.Rde1 Bf7 27.Rg3 Rc8 28.Reg1 Nd6 29.Rxg7 Nf5
30.R7g5 Rc7 31.Bxf5 exf5 32.Rh5+  1-0'''


def submit():
    Event = event.get()
    Site = site.get()
    Date = date.get()
    Round = round.get()
    White = wp.get()
    Black = bp.get()
    Result = result.get()
    WhiteElo = welo.get()
    BlackElo = belo.get()
    ECO = eco.get()

    with open("demo.pgn", "w") as o:
        o.write('[Event "%s"]\n' % (Event))
        o.write('[Site "%s"]\n' % (Site))
        o.write('[Date "%s"]\n' % (Date))
        o.write('[Round "%s"]\n' % (Round))
        o.write('[White "%s"]\n' % (White))
        o.write('[Black "%s"]\n' % (Black))
        o.write('[Result "%s"]\n' % (Result))
        o.write('[WhiteElo "%s"]\n' % (WhiteElo))
        o.write('[BlackElo "%s"]\n' % (BlackElo))
        o.write('[ECO "%s"]\n\n' % (ECO))
        o.write('%s\n\n' % (Game))
        o.close()

    # To delete all data from file
    # o = open("C:\\Users\\SANIKA\\Desktop\\8th sem\\Subjects\\Major Project\\Major-Project\\Python\\demo.txt", "a+")
    # o.truncate(0)


# creatin label
# Event
eve = tk.Label(root, text="Enter Event :")
eve.grid(row=0, column=0, padx=5, pady=5)

event = tk.Entry(root, width=20)
event.grid(row=0, column=1, padx=5, pady=5)

# site
st = tk.Label(root, text="Enter site :")
st.grid(row=1, column=0, padx=5, pady=5)

site = tk.Entry(root, width=20)
site.grid(row=1, column=1, padx=5, pady=5)

# Date
dt = tk.Label(root, text="Enter Date :")
dt.grid(row=2, column=0, padx=5, pady=5)

date = tk.Entry(root, width=20)
date.grid(row=2, column=1, padx=5, pady=5)

# Round
rd = tk.Label(root, text="Enter Round :")
rd.grid(row=3, column=0, padx=5, pady=5)

round = tk.Entry(root, width=20)
round.grid(row=3, column=1, padx=5, pady=5)


# White Player
we = tk.Label(root, text="White Player :")
we.grid(row=4, column=0, padx=5, pady=5)

wp = tk.Entry(root, width=20)
wp.grid(row=4, column=1, padx=5, pady=5)

# Black Plyer
bk = tk.Label(root, text="Black Player :")
bk.grid(row=5, column=0, padx=5, pady=5)

bp = tk.Entry(root, width=20)
bp.grid(row=5, column=1, padx=5, pady=5)

# Result
rt = tk.Label(root, text="Result :")
rt.grid(row=6, column=0, padx=5, pady=5)

result = tk.Entry(root, width=20)
result.grid(row=6, column=1, padx=5, pady=5)

# WhiteElo
wo = tk.Label(root, text="WhiteElo :")
wo.grid(row=7, column=0, padx=5, pady=5)

welo = tk.Entry(root, width=20)
welo.grid(row=7, column=1, padx=5, pady=5)

# blackElo
bo = tk.Label(root, text="BlackElo :")
bo.grid(row=8, column=0, padx=5, pady=5)

belo = tk.Entry(root, width=20)
belo.grid(row=8, column=1, padx=5, pady=5)

# ECO
eo = tk.Label(root, text="ECO :")
eo.grid(row=9, column=0, padx=5, pady=5)

eco = tk.Entry(root, width=20)
eco.grid(row=9, column=1, padx=5, pady=5)

# Button
mybutton = tk.Button(root, text="Submit",
                     padx=5, pady=5, command=submit)
mybutton.grid(row=10, column=0, padx=15, pady=25)


root.mainloop()
