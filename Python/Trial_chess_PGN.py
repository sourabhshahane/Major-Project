Game = '''1.e4 e6 2.d4 d5 3.Nd2 Nf6 4.e5 Nfd7 5.f4 c5 6.c3 Nc6 7.Ndf3 cxd4 8.cxd4 f6
9.Bd3 Bb4+ 10.Bd2 Qb6 11.Ne2 fxe5 12.fxe5 O-O 13.a3 Be7 14.Qc2 Rxf3 15.gxf3 Nxd4
16.Nxd4 Qxd4 17.O-O-O Nxe5 18.Bxh7+ Kh8 19.Kb1 Qh4 20.Bc3 Bf6 21.f4 Nc4 22.Bxf6 Qxf6
23.Bd3 b5 24.Qe2 Bd7 25.Rhg1 Be8 26.Rde1 Bf7 27.Rg3 Rc8 28.Reg1 Nd6 29.Rxg7 Nf5
30.R7g5 Rc7 31.Bxf5 exf5 32.Rh5+  1-0'''

Event = input("Enter Event: ")
Site = input("Enter Site: ")
Date = input("Enter Date: ")
Round = input("Enter Round: ")
White = input("Enter White: ")
Black = input("Enter Black: ")
Result = input("Enter Result: ")
WhiteElo = input("Enter WhiteElO: ")
BlackElo = input("Enter BlackElO: ")
ECO = input("Enter ECO: ")

with open("demo.pgn", "w") as o:

    o.write('[Event "%s"]\n' %(Event))
    o.write('[Site "%s"]\n' %(Site))
    o.write('[Date "%s"]\n' %(Date))
    o.write('[Round "%s"]\n' %(Round))
    o.write('[White "%s"]\n' %(White))
    o.write('[Black "%s"]\n'%(Black))
    o.write('[Result "%s"]\n' %(Result))
    o.write('[WhiteElo "%s"]\n' %(WhiteElo))
    o.write('[BlackElo "%s"]\n' %(BlackElo))
    o.write('[ECO "%s"]\n\n' %(ECO))
    o.write('%s\n\n' %(Game))

#To delete all data from file
#o = open("C:\\Users\\SANIKA\\Desktop\\8th sem\\Subjects\\Major Project\\Major-Project\\Python\\demo.txt", "a+")
#o.truncate(0)
