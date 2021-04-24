import tkinter as tk

# Creating window
root = tk.Tk()
root.title("chessGame")
root.geometry('500x500')

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


root.mainloop()
