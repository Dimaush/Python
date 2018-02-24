h = 0
r = 7

from tkinter import *
import time
root = Tk()
canv = Canvas (root, width = 560 + 2 * h, height = 620 + 2 * h, bg = 'black')
canv.pack()

def sign (x):
    if x > 0: return 1
    if x < 0: return -1
    else: return 0

def draw_pac ():
    global x, y, vx, vy
    if vx == 0 and vy == 0: canv.create_oval (x - r, y - r, x + r, y + r, fill = 'yellow', outline = 'yellow', tag = 'Pac')
    elif vx < 0: canv.create_arc (x - r, y - r, x + r, y + r, start = 226 - a, extent = 268 + 2 * a, fill = 'yellow', outline = 'yellow', tag = 'Pac')
    elif vx > 0: canv.create_arc (x - r, y - r, x + r, y + r, start = 46 - a, extent = 268 + 2 * a, fill = 'yellow', outline = 'yellow', tag = 'Pac')
    elif vy < 0: canv.create_arc (x - r, y - r, x + r, y + r, start = 136 - a, extent = 268 + 2 * a, fill = 'yellow', outline = 'yellow', tag = 'Pac')
    elif vy > 0: canv.create_arc (x - r, y - r, x + r, y + r, start = 316 - a, extent = 268 + 2 * a, fill = 'yellow', outline = 'yellow', tag = 'Pac')

def moveleft (event):
    global newvx, newvy
    newvx = -2
    newvy = 0

def moveright (event):
    global newvx, newvy
    newvx = 2
    newvy = 0

def moveup (event):
    global newvx, newvy
    newvx = 0
    newvy = -2

def movedown (event):
    global newvx, newvy
    newvx = 0
    newvy = 2

def move_pac ():
    global x, y, vx, vy
    x = (x + vx - h) % (560 + h) + h
    y = (y + vy - h) % (600 + h) + h

def move_Blinky ():
    global xB, yB, vxB, vyB, x, y, level, newvxB, newvyB
    A = [0] * 31
    for i in range (31): A [i] = [-2] * 28
    xPA, yPA = x // 20, y // 20
    A [yPA][xPA] = 0
    q = [(yPA, xPA)]
    while len (q) > 0:
        i, j = q.pop (0)
        m = i % 31
        m1 = (i - 1) % 31
        m2 = (i + 1) % 31
        n = j % 28
        n1 = (j - 1) % 28
        n2 = (j + 1) % 28
        if A [i][n1] == -2 and level [i][n1] != 9:
            A [i][n1] = A [i][j] + 1
            q += [(i, n1)]
        if A [i][n2] == -2 and level [i][n2] != 9:
            A [i][n2] = A [i][j] + 1
            q += [(i, n2)]
        if A [m1][j] == -2 and level [m1][j] != 9:
                A [m1][j] = A [i][j] + 1
                q += [(m1, j)]
        if A [m2][j] == -2 and level [m2][j] != 9:
            A [m2][j] = A [i][j] + 1
            q += [(m2, j)]
    xBt, yBt = xB // 20, yB // 20
    m = yBt % 31
    m1 = (yBt - 1) % 31
    m2 = (yBt + 1) % 31
    n = xBt % 28
    n1 = (xBt - 1) % 28
    n2 = (xBt + 1) % 28
    if A [m][n1] < A [m][n] and level [m][n1] != 9:
        newvxB = -1
        newvyB = 0
    if A [m][n2] < A [m][n] and level [m][n2] != 9:
        newvxB = 1
        newvyB = 0
    if A [m1][n] < A [m][n] and level [m1][n] != 9:
        newvyB = -1
        newvxB = 0
    if A [m2][n] < A [m][n] and level [m2][n] != 9:
        newvyB = 1
        newvxB = 0

def move_Pinky ():
    global xP, yP, x, y, vxP, vyP
    if abs (x - xP) >= abs (y - yP):
        if x != xP:
            if x - xP > 0: vxP = v [s]
            else: vxP = -v [s]
        vyP = 0
    else:
        if y != yP:
            if y - yP > 0: vyP = v [s]
            else: vyP = -v [s]
        vxP = 0

def move_Inky ():
    global xI, yI, x, y, vxI, vyI
    if abs (x - xI) >= abs (y - yI):
        if x != xI:
            if x - xI > 0: vxI = v [s]
            else: vxI = -v [s]
        vyI = 0
    else:
        if y != yI:
            if y - yI > 0: vyI = v [s]
            else: vyI = -v [s]
        vxI = 0

def move_Clyde ():
    global xC, yC, x, y, vxC, vyC
    if abs (x - xC) >= abs (y - yC):
        if x != xC:
            if x - xC > 0: vxC = v [s]
            else: vxC = -v [s]
        vyC = 0
    else:
        if y != yC:
            if y - yC > 0: vyC = v [s]
            else: vyC = -v [s]
        vxC = 0

def draw_body (xG, yG, c):
    canv.create_rectangle (xG - 7, yG - 2, xG + 7, yG + 4, fill = c, outline = c, tag = 'Ghost')
    canv.create_rectangle (xG - 6, yG - 5, xG + 6, yG - 2, fill = c, outline = c, tag = 'Ghost')
    canv.create_rectangle (xG - 5, yG - 6, xG + 5, yG - 5, fill = c, outline = c, tag = 'Ghost')
    canv.create_rectangle (xG - 4, yG - 7, xG + 4, yG - 6, fill = c, outline = c, tag = 'Ghost')
    canv.create_rectangle (xG - 2, yG - 8, xG + 2, yG - 7, fill = c, outline = c, tag = 'Ghost')
    canv.create_rectangle (xG - 7, yG + 4, xG - 3, yG + 5, fill = c, outline = c, tag = 'Ghost')
    canv.create_rectangle (xG - 6, yG + 5, xG - 4, yG + 6, fill = c, outline = c, tag = 'Ghost')
    canv.create_rectangle (xG - 2, yG + 4, xG + 2, yG + 5, fill = c, outline = c, tag = 'Ghost')
    canv.create_rectangle (xG - 1, yG + 5, xG + 1, yG + 6, fill = c, outline = c, tag = 'Ghost')
    canv.create_rectangle (xG + 3, yG + 4, xG + 7, yG + 5, fill = c, outline = c, tag = 'Ghost')
    canv.create_rectangle (xG + 4, yG + 5, xG + 6, yG + 6, fill = c, outline = c, tag = 'Ghost')

def draw_stop (xG, yG):
    canv.create_rectangle (xG - 5, yG - 4, xG - 1, yG - 1, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG - 4, yG - 5, xG - 2, yG - 4, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG - 4, yG - 1, xG - 2, yG, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG + 1, yG - 4, xG + 5, yG - 1, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG + 2, yG - 5, xG + 4, yG - 4, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG + 2, yG - 1, xG + 4, yG, fill = 'white', outline = 'white', tag = 'Ghost')

def draw_right (xG, yG):
    canv.create_rectangle (xG - 4, yG - 4, xG, yG - 1, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG - 3, yG - 5, xG - 1, yG - 4, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG - 5, yG - 1, xG - 1, yG, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG + 2, yG - 4, xG + 6, yG - 1, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG + 3, yG - 5, xG + 5, yG - 4, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG + 3, yG - 1, xG + 5, yG, fill = 'white', outline = 'white', tag = 'Ghost')

def draw_left (xG, yG):
    canv.create_rectangle (xG - 6, yG - 4, xG - 2, yG - 1, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG - 5, yG - 5, xG - 3, yG - 4, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG - 5, yG - 1, xG - 3, yG, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG, yG - 4, xG + 4, yG - 1, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG + 1, yG - 5, xG + 3, yG - 4, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG + 1, yG - 1, xG + 3, yG, fill = 'white', outline = 'white', tag = 'Ghost')

def draw_1 (xG, yG):
    canv.create_rectangle (xG - 4, yG - 3, xG - 2, yG - 1, fill = 'blue', outline = 'blue', tag = 'Ghost')
    canv.create_rectangle (xG + 2, yG - 3, xG + 4, yG - 1, fill = 'blue', outline = 'blue', tag = 'Ghost')
def draw_2 (xG, yG):
    canv.create_rectangle (xG - 4, yG - 2, xG - 2, yG, fill = 'blue', outline = 'blue', tag = 'Ghost')
    canv.create_rectangle (xG + 2, yG - 2, xG + 4, yG, fill = 'blue', outline = 'blue', tag = 'Ghost')
def draw_3 (xG, yG):
    canv.create_rectangle (xG - 4, yG - 5, xG - 2, yG - 3, fill = 'blue', outline = 'blue', tag = 'Ghost')
    canv.create_rectangle (xG + 2, yG - 5, xG + 4, yG - 3, fill = 'blue', outline = 'blue', tag = 'Ghost')
def draw_4 (xG, yG):
    canv.create_rectangle (xG - 2, yG - 3, xG, yG - 1, fill = 'blue', outline = 'blue', tag = 'Ghost')
    canv.create_rectangle (xG + 4, yG - 3, xG + 6, yG - 1, fill = 'blue', outline = 'blue', tag = 'Ghost')
def draw_5 (xG, yG):
    canv.create_rectangle (xG - 6, yG - 3, xG - 4, yG - 1, fill = 'blue', outline = 'blue', tag = 'Ghost')
    canv.create_rectangle (xG, yG - 3, xG + 2, yG - 1, fill = 'blue', outline = 'blue', tag = 'Ghost') 

def draw_ghost (xG, yG, vxG, vyG, c):
    global x, y
    draw_body (xG, yG, c)
    if vxG == 0 and vyG == 0:
        draw_stop (xG, yG)
        draw_1 (xG, yG)
    else:
        if vxG > 0:
            draw_right (xG, yG)
            draw_4 (xG, yG)
        elif vxG < 0:
            draw_left (xG, yG)
            draw_5 (xG, yG)         
        elif vyG > 0:
            draw_stop (xG, yG)
            draw_2 (xG, yG)           
        else:
            draw_stop (xG, yG)
            draw_3 (xG, yG)

def draw_Blinky (xB, yB, vxB, vyB):
    draw_ghost (xB, yB, vxB, vyB, 'red')
    move_Blinky ()

def draw_Pinky (xP, yP, vxP, vyP):
    draw_ghost (xP, yP, vxP, vyP, 'deep pink')
    move_Pinky ()

def draw_Inky (xI, yI, vxI, vyI):
    draw_ghost (xI, yI, vxI, vyI, 'cyan')
    move_Inky ()

def draw_Clyde (xB, yB, vxB, vyB):
    draw_ghost (xB, yB, vxB, vyB, 'orange')
    move_Clyde ()

def draw_lives (n):
    for i in range (n):
        canv.create_arc (2 * r * i + 15, 15 + 2 * r, 2 * r * i + 15 + 2 * r, 15, start = 45, extent = 270, fill = 'yellow', outline = 'yellow', tag = 'live')

def check_lives ():
    global rB, rP, rI, rC, r, w, l
    if flag == 1:
        l -= 1
        canv.delete ('live')
        draw_lives (l)
        canv.update ()
        time.sleep (2)
        if l >= 0:
            start ()
            draw ()
            canv.update ()

def draw_level (level):
    for i in range (len (level)):
        for j in range (len (level [i])):
            x = level [i][j]
            if x == 9:
                canv.create_rectangle (h + j * 20, h + i * 20, h + (j + 1) * 20, h + (i + 1) * 20, fill = 'blue', outline = 'blue', tag = 'level')
            elif x == 1:
                canv.create_oval (h + j * 20 + 8, h + i * 20 + 8, h + (j + 1) * 20 - 8, h + (i + 1) * 20 - 8, fill = 'yellow', tag = 'point')
            elif x == 2:
                canv.create_oval (h + j * 20 + 4, h + i * 20 + 4, h + (j + 1) * 20 - 4, h + (i + 1) * 20 - 4, fill = 'yellow', tag = 'point')
    canv.update ()

def draw ():
    global l1
    canv.delete ('Pac', 'Ghost')
    draw_pac ()
    draw_Blinky (xB, yB, vxB, vyB)
    if l1 != l:
        draw_lives (l)
        l1 = l

def start ():
    global x, y, xB, yB, xP, yP, xI, yI, xC, yC
    global vx, vy, vxB, vyB, vxP, vyP, vxI, vyI, vxC, vyC
    global w, a, f
    global rB, rP, rI, rC
    x, y = 270 + h, 470 + h
    xB, yB = 270 + h, 230 + h
    xP, yP = 270 + h, 300 + h
    xI, yI = 230 + h, 300 + h
    xC, yC = 310 + h, 300 + h
    vx, vy = 0, 0
    newvx, newvy = 0, 0
    newvxB, newvyB = 0, 0
    vxB, vyB = 0, 0
    vxP, vyP = 0, 0
    vxI, vyI = 0, 0
    vxC, vyC = 0, 0
    a, f = 0, 1
    draw ()
    canv.update ()
    time.sleep (2)

l = 2
l1 = l
s = 0

root.bind ('<Left>', moveleft)
root.bind ('<Right>', moveright)
root.bind ('<Up>', moveup)
root.bind ('<Down>', movedown)

v = [1, 0.5]

fi = open ('1 level.txt')
level = []
for line in fi:
    level.append (list (map (int, list (line [:-1]))))
fi.close()

draw_level (level)
newvx, newvy = 0, 0
newvxB, newvyB = 0, 0
draw_lives (l)
start ()

while l >= 0:
    flag = 0
    if x % 20 == 10 and y % 20 == 10:
        if level [(y // 20 + sign (newvy)) % 31][(x // 20 + sign (newvx)) % 28] != 9:
            vx, vy = newvx, newvy
        elif level [(y // 20 + sign (vy)) % 31][(x // 20 + sign (vx)) % 28] == 9:
            vx, vy = 0, 0
    
    if xB % 20 == 10 and yB % 20 == 10:
        if level [(yB // 20 + sign (newvyB)) % 31][(xB // 20 + sign (newvxB)) % 28] != 9:
            vxB, vyB = newvxB, newvyB
        elif level [(yB // 20 + sign (vyB)) % 31][(xB // 20 + sign (vxB)) % 28] == 9:
            vxB, vyB = 0, 0
    move_pac ()
    xB += vxB
    yB += vyB
    xB, yB = xB % (560 + 2 * h), yB % (620 + 2 * h)
    xP += vxP
    yP += vyP
    xI += vxI
    yI += vyI
    xC += vxC
    yC += vyC
    time.sleep (0.01)
    draw ()
    canv.update ()
    a += 3 * f
    if a == 0: f = 1
    elif a == 45: f = -1
    xt = x // 20
    yt = y // 20
    xBt = xB // 20
    yBt = yB // 20
    xPt = yP // 20
    yPt = yP // 20
    xIt = yI // 20
    yIt = yI // 20
    xCt = yC // 20
    yCt = yC // 20
    if xt == xBt and yt == yBt or xt == xPt and yt == yPt or xt == xIt and yt == yIt or xt == xCt and yt == yCt:
        flag = 1
    check_lives ()

canv.create_text ((560 + 2 * h) // 2, (620 + 2 * h) // 2, text = 'GAME OVER', font = 'Times 70', justify = CENTER, fill = 'dark red')
canv.update ()

root.mainloop()