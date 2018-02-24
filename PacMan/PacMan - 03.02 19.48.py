h = 60 #Расстояние от края до поля
r = 12 #Радиус PACMANа
#d = (r + 15) ** 2 Квадрат допустимого расстояния от PACMANа до привидений

from tkinter import *
import time
root = Tk()
canv = Canvas (root, width = 540 + 2 * h, height = 600 + 2 * h, bg = 'black')
canv.pack()

def draw_pac ():
    global x, y, vx, vy
    if vx == 0 and vy == 0: canv.create_oval (x - r, y - r, x + r, y + r, fill = 'yellow', outline = 'yellow', tag = 'Pac')
    elif vx < 0: canv.create_arc (x - r, y - r, x + r, y + r, start = 226 - a, extent = 268 + 2 * a, fill = 'yellow', outline = 'yellow', tag = 'Pac')
    elif vx > 0: canv.create_arc (x - r, y - r, x + r, y + r, start = 46 - a, extent = 268 + 2 * a, fill = 'yellow', outline = 'yellow', tag = 'Pac')
    elif vy < 0: canv.create_arc (x - r, y - r, x + r, y + r, start = 136 - a, extent = 268 + 2 * a, fill = 'yellow', outline = 'yellow', tag = 'Pac')
    elif vy > 0: canv.create_arc (x - r, y - r, x + r, y + r, start = 316 - a, extent = 268 + 2 * a, fill = 'yellow', outline = 'yellow', tag = 'Pac')

def moveleft (event):
    global vx, vy
    vx = -2
    vy = 0

def moveright (event):
    global vx, vy
    vx = 2
    vy = 0

def moveup (event):
    global vx, vy
    vx = 0
    vy = -2

def movedown (event):
    global vx, vy
    vx = 0
    vy = 2

def move_pac ():
    global x, y, vx, vy
    x = (x + vx - (h - 20)) % (540 + h - 20) + (h - 20)
    y = y + vy

def move_Blinky ():
    global xB, yB, x, y, vxB, vyB
    #if x == xB: vxB = 0
    #if y == yB: vyB = 0
    if abs (x - xB) >= abs (y - yB):
        if x != xB:
            if x - xB > 0: vxB = v [s]
            else: vxB = -v [s]
        vyB = 0
    else:
        if y != yB:
            if y - yB > 0: vyB = v [s]
            else: vyB = -v [s]
        vxB = 0

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
    canv.create_rectangle (xG - 14, yG - 4, xG + 14, yG + 8, fill = c, outline = c, tag = 'Ghost')
    canv.create_rectangle (xG - 12, yG - 10, xG + 12, yG - 4, fill = c, outline = c, tag = 'Ghost')
    canv.create_rectangle (xG - 10, yG - 12, xG + 10, yG - 10, fill = c, outline = c, tag = 'Ghost')
    canv.create_rectangle (xG - 8, yG - 14, xG + 8, yG - 12, fill = c, outline = c, tag = 'Ghost')
    canv.create_rectangle (xG - 4, yG - 16, xG + 4, yG - 14, fill = c, outline = c, tag = 'Ghost')
    canv.create_rectangle (xG - 14, yG + 8, xG - 6, yG + 10, fill = c, outline = c, tag = 'Ghost')
    canv.create_rectangle (xG - 12, yG + 10, xG - 8, yG + 12, fill = c, outline = c, tag = 'Ghost')
    canv.create_rectangle (xG - 4, yG + 8, xG + 4, yG + 10, fill = c, outline = c, tag = 'Ghost')
    canv.create_rectangle (xG - 2, yG + 10, xG + 2, yG + 12, fill = c, outline = c, tag = 'Ghost')
    canv.create_rectangle (xG + 6, yG + 8, xG + 14, yG + 10, fill = c, outline = c, tag = 'Ghost')
    canv.create_rectangle (xG + 8, yG + 10, xG + 12, yG + 12, fill = c, outline = c, tag = 'Ghost')

def draw_stop (xG, yG):
    canv.create_rectangle (xG - 10, yG - 8, xG - 2, yG - 2, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG - 8, yG - 10, xG - 4, yG - 8, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG - 8, yG - 2, xG - 4, yG, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG + 2, yG - 8, xG + 10, yG - 2, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG + 4, yG - 10, xG + 8, yG - 8, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG + 4, yG - 2, xG + 8, yG, fill = 'white', outline = 'white', tag = 'Ghost')

def draw_right (xG, yG):
    canv.create_rectangle (xG - 8, yG - 8, xG, yG - 2, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG - 6, yG - 10, xG - 2, yG - 8, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG - 6, yG - 2, xG - 2, yG, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG + 4, yG - 8, xG + 12, yG - 2, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG + 6, yG - 10, xG + 10, yG - 8, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG + 6, yG - 2, xG + 10, yG, fill = 'white', outline = 'white', tag = 'Ghost')

def draw_left (xG, yG):
    canv.create_rectangle (xG - 12, yG - 8, xG - 4, yG - 2, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG - 10, yG - 10, xG - 6, yG - 8, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG - 10, yG - 2, xG - 6, yG, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG, yG - 8, xG + 8, yG - 2, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG + 2, yG - 10, xG + 6, yG - 8, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG + 2, yG - 2, xG + 6, yG, fill = 'white', outline = 'white', tag = 'Ghost')

def draw_1 (xG, yG):
    canv.create_rectangle (xG - 8, yG - 6, xG - 4, yG - 2, fill = 'blue', outline = 'blue', tag = 'Ghost')
    canv.create_rectangle (xG + 4, yG - 6, xG + 8, yG - 2, fill = 'blue', outline = 'blue', tag = 'Ghost')
def draw_2 (xG, yG):
    canv.create_rectangle (xG - 8, yG - 4, xG - 4, yG, fill = 'blue', outline = 'blue', tag = 'Ghost')
    canv.create_rectangle (xG + 4, yG - 4, xG + 8, yG, fill = 'blue', outline = 'blue', tag = 'Ghost')
def draw_3 (xG, yG):
    canv.create_rectangle (xG - 8, yG - 10, xG - 4, yG - 6, fill = 'blue', outline = 'blue', tag = 'Ghost')
    canv.create_rectangle (xG + 4, yG - 10, xG + 8, yG - 6, fill = 'blue', outline = 'blue', tag = 'Ghost')
def draw_4 (xG, yG):
    canv.create_rectangle (xG - 4, yG - 6, xG, yG - 2, fill = 'blue', outline = 'blue', tag = 'Ghost')
    canv.create_rectangle (xG + 8, yG - 6, xG + 12, yG - 2, fill = 'blue', outline = 'blue', tag = 'Ghost')
def draw_6 (xG, yG):
    canv.create_rectangle (xG - 12, yG - 6, xG - 8, yG - 2, fill = 'blue', outline = 'blue', tag = 'Ghost')
    canv.create_rectangle (xG, yG - 6, xG + 4, yG - 2, fill = 'blue', outline = 'blue', tag = 'Ghost')    

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
            draw_6 (xG, yG)         
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

def draw_walls ():
    global A
    for i in range (len (A)):
        canv.create_rectangle (h + A [i][0], h + A [i][1], h + A [i][2], h + A [i][3], fill = 'blue', outline = 'blue', tag = 'wall')

def draw_lives (n):
    for i in range (n):
        canv.create_arc (2 * r * i + 15, 15 + 2 * r, 2 * r * i + 15 + 2 * r, 15, start = 45, extent = 270, fill = 'yellow', outline = 'yellow', tag = 'live')

def scan_pac (P):
    global x, y, vx, vy, h, r
    if x - r > P [0] + h and x - r < P [2] + h or x + r > P [0] + h and x + r < P [2] + h or P [0] + h > x - r and P [0] + h < x + r or P [2] + h > x - r and P [2] + h < x + r:
        if y - r > P [1] + h and y - r < P [3] + h or y + r > P [1] + h and y + r < P [3] + h or P [1] + h > y - r and P [1] + h < y + r or P [3] + h > y - r and P [3] + h < y + r:
            if x < P [0] + h:
                x -= 2
                vx = 0
            if x > P [2] + h:
                x += 2
                vx = 0
            if y < P [1] + h:
                y -= 2
                vy = 0
            if y > P [3] + h:
                y += 2
                vy = 0

def scan_pac_f (P):
    global x, y, vx, vy, h, r
    if x + vx - (r + 2) > P [0] + h and x + vx - (r + 2) < P [2] + h or x + vx + (r + 2) > P [0] + h and x + vx + (r + 2) < P [2] + h or P [0] + h > x + vx - (r + 2) and P [0] + h < x + vx + (r + 2) or P [2] + h > x + vx - (r + 2) and P [2] + h < x + vx + r:
        if y + vy - (r + 2) > P [1] + h and y + vy - (r + 2) < P [3] + h or y + vy + (r + 2) > P [1] + h and y + vy + (r + 2) < P [3] + h or P [1] + h > y + vy - (r + 2) and P [1] + h < y + vy + (r + 2) or P [3] + h > y + vy - (r + 2) and P [3] + h < y + vy + r:
            vx = 0
            vy = 0

def scan_pac_f_1 (P):
    global x, y, vx, vy, h, r
    if ((x + vx - 20) - (P [2] + h)) * ((x + vx + 20) - (P [0] + h)) <= 0 and ((y + vy - 20) - (P [3] + h)) * ((y + vy + 20) - (P [1] + h)) <= 0:
        vx = 0
        vy = 0


def check_lives ():
    global rB, rP, rI, rC, r, w, l
    if rB <= (r + 15) ** 2 or rP <= (r + 15) ** 2 or rI <= (r + 15) ** 2 or rC <= (r + 15) ** 2:
        l -= 1
        canv.create_rectangle (2 * r * l + 15, 15 + 2 * r, 2 * r * l + 15 + 2 * r, 15, fill = 'black')
        canv.update ()
        time.sleep (2)
        if l >= 0:
            start ()
            draw ()
            canv.update ()

def draw ():
    global l1
    canv.delete ('Pac', 'Ghost')
    draw_pac ()
    draw_Blinky (xB, yB, vxB, vyB)
    draw_Pinky (xP, yP, vxP, vyP)
    draw_Inky (xI, yI, vxI, vyI)
    draw_Clyde (xC, yC, vxC, vyC)
    if l1 != l:
        draw_lives (l)
        l1 = l

def start ():
    global x, y, xB, yB, xP, yP, xI, yI, xC, yC
    global vx, vy, vxB, vyB, vxP, vyP, vxI, vyI, vxC, vyC
    global w, a, f
    global rB, rP, rI, rC
    x, y = 270 + h, 460 + h
    xB, yB = 270 + h, 240 + h
    xP, yP = 270 + h, 300 + h
    xI, yI = 230 + h, 300 + h
    xC, yC = 310 + h, 300 + h
    vx, vy = 0, 0
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
A = [[40, 40, 100, 80], [140, 40, 220, 80], [260, 0, 280, 80], [320, 40, 400, 80], [440, 40, 500, 80], [40, 120, 100, 140], [140, 120, 160, 260], [200, 120, 340, 140], [380, 120, 400, 260], [440, 120, 500, 140], [260, 140, 280, 200], [160, 180, 220, 200], [320, 180, 380, 200], [140, 300, 160, 380], [380, 300, 400, 380], [200, 360, 340, 380], [260, 380, 280, 440], [40, 420, 100, 440], [140, 420, 220, 440], [320, 420, 400, 440], [440, 420, 500, 440], [80, 440, 100, 500], [440, 440, 460, 500], [0, 480, 40, 500], [200, 480, 340, 500], [500, 480, 540, 500], [140, 480, 160, 540], [380, 480, 400, 540], [260, 500, 280, 560], [40, 540, 220, 560], [320, 540, 500, 560], [-20, -20, 560, 0], [-20, 600, 560, 620], [-20, 0, 0, 180], [-20, 180, 100, 200], [80, 200, 100, 240], [-20, 240, 100, 260], [-20, 300, 100, 320], [80, 320, 100, 360], [-20, 360, 100, 380], [-20, 380, 0, 600], [540, 0, 560, 180], [440, 180, 560, 200], [440, 200, 460, 240], [440, 240, 560, 260], [440, 300, 560, 320], [440, 320, 460, 360], [440, 360, 560, 380], [540, 380, 560, 600]]
draw_walls ()
draw_lives (l)
start ()

while l >= 0:
    for i in range (len (A)):
        scan_pac_f (A [i])
    move_pac ()
    xB += vxB
    yB += vyB
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
    rB = (x - xB) ** 2 + (y - yB) ** 2
    rP = (x - xP) ** 2 + (y - yP) ** 2
    rI = (x - xI) ** 2 + (y - yI) ** 2
    rC = (x - xC) ** 2 + (y - yC) ** 2
    check_lives ()

canv.create_text ((540 + 2 * h) // 2, (600 + 2 * h) // 2, text = 'GAME OVER', font = 'Times 72', justify = CENTER, fill = 'dark red')
canv.update ()

root.mainloop()