import numpy as np
import random
import time

out = open("out.txt", "w")

board = np.zeros((4,6,3))
goal = np.zeros((4,4))
start = np.array([[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]])
atStart = [0,0,0,0]
die = 0

def initialiseBoard():
    for i in range(len(board)):
        for j in range(len(board[i])):
            for k in range(len(board[i][j])):
                board[i][j][k] = 0
    for i in range(len(goal)):
        for j in range(len(goal[i])):
            goal[i][j] = 0
    for i in range(1,5):
        for j in range(4):
            start[i-1][j] = i
    for i in range(4):
        atStart[i] = 0

def printboard():
    text = ""
    text += "      "
    for i in range(3):
        text += str(int(board[1][0][i]))
    text += "      \n"
    text += "      "
    for i in range(3):
        text += str(int(board[1][1][i]))
    text += "      \n"
    text += "  "
    for i in range(2):
        text += str(int(start[0][i]))
    text += "  "
    for i in range(3):
        text += str(int(board[1][2][i]))
    text += "  "
    for i in range(2):
        text += str(int(start[1][i]))
    text += "  \n"
    text += "  "
    for i in range(2):
        text += str(int(start[0][i+2]))
    text += "  "
    for i in range(3):
        text += str(int(board[1][3][i]))
    text += "  "
    for i in range(2):
        text += str(int(start[1][i+2]))
    text += "  \n"
    text += "      "
    for i in range(3):
        text += str(int(board[1][4][i]))
    text += "      \n"
    text += "      "
    for i in range(3):
        text += str(int(board[1][5][i]))
    text += "      \n"
    for i in range(6):
        text += str(int(board[0][i][2]))
    text += "   "
    for i in range(6):
        text += str(int(board[2][5-i][0]))
    text += "\n"
    for i in range(6):
        text += str(int(board[0][i][1]))
    text += "   "
    for i in range(6):
        text += str(int(board[2][5-i][1]))
    text += "\n"
    for i in range(6):
        text += str(int(board[0][i][0]))
    text += "   "
    for i in range(6):
        text += str(int(board[2][5-i][2]))
    text += "\n"
    text += "      "
    for i in range(3):
        text += str(int(board[3][5][2-i]))
    text += "      \n"
    text += "      "
    for i in range(3):
        text += str(int(board[3][4][2-i]))
    text += "      \n"
    text += "  "
    for i in range(2):
        text += str(int(start[3][i]))
    text += "  "
    for i in range(3):
        text += str(int(board[3][3][2-i]))
    text += "  "
    for i in range(2):
        text += str(int(start[2][i]))
    text += "  \n"
    text += "  "
    for i in range(2):
        text += str(int(start[3][i+2]))
    text += "  "
    for i in range(3):
        text += str(int(board[3][2][2-i]))
    text += "  "
    for i in range(2):
        text += str(int(start[2][i+2]))
    text += "  \n"
    text += "      "
    for i in range(3):
        text += str(int(board[3][1][2-i]))
    text += "      \n"
    text += "      "
    for i in range(3):
        text += str(int(board[3][0][2-i]))
    text += "      \n\n"
    print(text)
    out.write("Goal:")
    out.write(str(goal))

def rolldie():
    return random.randint(1,6)

def findplace(i):
    k = i - 1
    while i not in board[k]:
        if k == 0:
            k = 3
        else:
            k -= 1
    g = 2
    while i not in board[k,:,g]:
        g -= 1
    j = 5
    while board[k][j][g] != i:
        j -= 1
    return k, j, g

def newmove(k, j, g, die, i):
    new_g = g
    new_j = j
    new_k = k
    if g == 0:
        move = j - die
        if move < 0:
            index = die - j
            if index > 1:
                if k == i-1:
                    index -= 1
                    new_j = index
                    new_g = 1
                elif index > 2:
                    index -= 2
                    new_j = index
                    new_g = 2
                else:
                    index -= 1
                    new_j = 0
                    new_g = 1
            else:
                new_j = 0
                new_g = index
        else:
            new_j = move
    elif g == 1:
        if k == i-1:
            if j + die <= 5:
                new_j = j + die
            else:
                t = 0
                while goal[i-1][t] == i:
                    t += 1
                goal[i-1][t] = int(i)
                new_g = 8
                new_j = 8
                new_k = 8
        else:
            if die > 1:
                moves = die - 1
                new_g = 2
                new_j = moves
            else:
                new_j = 0
                new_g = 2
    else:
        moves = j + die
        if moves > 5:
            index = moves - 6
            if k == 3:
                new_k = 0
            else:
                new_k = k + 1
            new_g = 0
            new_j = 5 - index
        else:
            new_j = moves
    return new_k, new_j, new_g

def kick(k, j, g, i, die, old_k, old_j, old_g):
    kicked = int(board[k][j][g])
    if kicked == k + 1 and j == 1 and g == 2:
        index = 0
        while start[i-1][index] != 0:
            index += 1
        start[i-1][index] = i
        board[old_k, old_j, old_g] = 0
    elif kicked == i:
        new_k, new_j, new_g = newmove(k,j,g,die,i)
        if board[new_k][new_j][new_g] != 0:
            kick(new_k, new_j, new_g, i, die, k, j, g)
        else:
            board[k][j][g] = 0
            board[new_k][new_j][new_g] = i
    else:
        index = 0
        while start[kicked-1][index] != 0:
            index += 1
        start[kicked-1][index] = kicked
        board[old_k, old_j, old_g] = 0
        board[k][j][g] = i

def moveboard(i, die):
    if i in board:
        k, j, g = findplace(i)
        new_k, new_j, new_g = newmove(k,j,g,die,i)
        if new_k != 8:
            if board[new_k][new_j][new_g] != 0:
                kick(new_k, new_j, new_g, i, die, k, j, g)
            else:
                board[k][j][g] = 0
                board[new_k][new_j][new_g] = i
        else:
            board[k][j][g] = 0

    out.write(f"{atStart}\n")
    if atStart[i-1] != 0:
        if board[i-1][1][2] == 0:
            atStart[i-1] -= 1
            if atStart[i-1] != 0:
                board[i-1][1][2] = i

def makemove(i):
    out.write(f"Rolling for {i}\n")
    die = rolldie()
    out.write(f"Rolled {die}\n")
    if die == 6:
        if i in start:
            j = 0
            while start[i-1][j] != i:
                j += 1
            start[i-1][j] = 0
            if board[i-1][1][2] != 0 and board[i-1][1][2] != i:
                kicked = int(board[i-1][1][2])
                index = 0
                while start[kicked-1][index] != 0:
                    index += 1
                start[kicked-1][index] = kicked
            board[i-1][1][2] = i
            atStart[i-1] += 1
            printboard()
        else:
            moveboard(i, die)
            printboard()
        input()
        makemove(i)
    else:
        moveboard(i, die)
        printboard()
winners = {1:0,2:0,3:0,4:0}

def play():
    won = False
    initialiseBoard()
    printboard()
    while won == False:
    #for i in range(85):
        i = 1
        while i < 5:
            makemove(i)
            if 0 not in goal[i-1]:
                won = True
                winners[i] += 1
                i = 5
            printboard()
            i += 1
            input()

for i in range(1):
    play()
#print("End")
print(f"{winners}")
