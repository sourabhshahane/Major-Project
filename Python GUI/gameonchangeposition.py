location = {"wRl": 0, "wNl": 1, "wBl": 2, "wQ": 3, "wK": 4, "wBr": 5, "wNr": 6, "wRr": 7, "wP1": 8, "wP2": 9, "wP3": 10, "wP4": 11, "wP5": 12, "wP6": 13, "wP7": 14, "wP8": 15,
            "bP1": 48, "bP2": 49, "bP3": 50, "bP4": 51, "bP5": 52, "bP6": 53, "bP7": 54, "bP8": 55, "bRl": 56, "bNl": 57, "bBl": 58, "bQ": 59, "bK": 60, "bBr": 61, "bNr": 62, "bRr": 63}

# var used in position name
col = ["a", "b", "c", "d", "e", "f", "g", "h"]


# var used in change
temp1 = None
temp2 = None
firststore = False
secondstore = False
a = 0
cassnewposi = []

# var used in movename
pawnpromotion = False
storemove = []  # store moves

# Gamestore
no = 0
game = ""


def gamestore():
    global no
    global game
    global storemove
    for b in range(len(storemove)):
        if(((b+1) % 2) != 0):
            no += 1
            p1 = str(no)+"."+storemove[b]
            int(no)
        else:
            p1 = storemove[b]
        game = game+p1+" "
    print(game)


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

    print(arr)
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
    arr = []
    # finding other Kinght position
    if(piece[2] == "r"):
        oppositename = piece[0:2]+"l"
        pos = location[oppositename]

    else:
        oppositename = piece[0:2]+"r"
        pos = location[oppositename]

    # findign all possibel paths of the other knight
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

                if(temp2[2] == "r"):
                    if cassnewposi[0] > cassnewposi[1]:
                        location[temp1] = cassnewposi[0]
                        location[temp2] = cassnewposi[1]
                    else:
                        location[temp1] = cassnewposi[1]
                        location[temp2] = cassnewposi[0]
                    # print("o-o")
                    storemove.append("o-o")

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


change(8)
change(8)
change(9)
change(17)
change(10)
change(17)
change(17)
change(17)
change(25)
change(25)
change(25)
change(25)
change(8)
change(25)


gamestore()
