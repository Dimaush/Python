w = 600
h = 0
r = 14
#d = (r + 15) ** 2

from tkinter import *
import time
root = Tk()
canv = Canvas (root, width = w, height = w, bg = 'black')
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
    x += vx
    y += vy

def move_Blinky ():
    global xB, yB, x, y, vxB, vyB
    #if x == xC: vxC = 0
    #if y == yC: vyC = 0
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
    canv.create_rectangle (xG - 8, yG - 6, xG - 4, yG - 2, fill = 'blue', outline = 'blue', tag = 'Ghost')
    canv.create_rectangle (xG + 2, yG - 8, xG + 10, yG - 2, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG + 4, yG - 10, xG + 8, yG - 8, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG + 4, yG - 2, xG + 8, yG, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG + 4, yG - 6, xG + 8, yG - 2, fill = 'blue', outline = 'blue', tag = 'Ghost')

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

def draw_Blinky ():
    global xB, yB
    draw_body (xB, yB, 'red')
    if vxB == 0 and vyB == 0:
        draw_stop (xB, yB)
    else:
        if x >= xB:
            draw_right (xB, yB)
            if y >= yB:
                canv.create_rectangle (xB - 4, yB - 6, xB, yB - 2, fill = 'blue', outline = 'blue', tag = 'Ghost')
                canv.create_rectangle (xB + 8, yB - 6, xB + 12, yB - 2, fill = 'blue', outline = 'blue', tag = 'Ghost')
            else:
                canv.create_rectangle (xB - 4, yB - 8, xB, yB - 4, fill = 'blue', outline = 'blue', tag = 'Ghost')
                canv.create_rectangle (xB + 8, yB - 8, xB + 12, yB - 4, fill = 'blue', outline = 'blue', tag = 'Ghost')
        else:
            draw_left (xB, yB)
            if y >= yB:
                canv.create_rectangle (xB - 12, yB - 6, xB - 8, yB - 2, fill = 'blue', outline = 'blue', tag = 'Ghost')
                canv.create_rectangle (xB, yB - 6, xB + 4, yB - 2, fill = 'blue', outline = 'blue', tag = 'Ghost')
            else:
                canv.create_rectangle (xB - 12, yB - 8, xB - 8, yB - 4, fill = 'blue', outline = 'blue', tag = 'Ghost')
                canv.create_rectangle (xB, yB - 8, xB + 4, yB - 4, fill = 'blue', outline = 'blue', tag = 'Ghost')
    move_Blinky ()

def draw_Pinky ():
    global xP, yP
    draw_body (xP, yP, 'deep pink')
    if vxP == 0 and vyP == 0:
        draw_stop (xP, yP)
    else:
        if x >= xP:
            draw_right (xP, yP)
            if y >= yP:
                canv.create_rectangle (xP - 4, yP - 6, xP, yP - 2, fill = 'blue', outline = 'blue', tag = 'Ghost')
                canv.create_rectangle (xP + 8, yP - 6, xP + 12, yP - 2, fill = 'blue', outline = 'blue', tag = 'Ghost')
            else:
                canv.create_rectangle (xP - 4, yP - 8, xP, yP - 4, fill = 'blue', outline = 'blue', tag = 'Ghost')
                canv.create_rectangle (xP + 8, yP - 8, xP + 12, yP - 4, fill = 'blue', outline = 'blue', tag = 'Ghost')
        else:
            draw_left (xP, yP)
            if y >= yP:
                canv.create_rectangle (xP - 12, yP - 6, xP - 8, yP - 2, fill = 'blue', outline = 'blue', tag = 'Ghost')
                canv.create_rectangle (xP, yP - 6, xP + 4, yP - 2, fill = 'blue', outline = 'blue', tag = 'Ghost')
            else:
                canv.create_rectangle (xP - 12, yP - 8, xP - 8, yP - 4, fill = 'blue', outline = 'blue', tag = 'Ghost')
                canv.create_rectangle (xP, yP - 8, xP + 4, yP - 4, fill = 'blue', outline = 'blue', tag = 'Ghost')
    move_Pinky ()

def draw_Inky ():
    global xI, yI
    draw_body (xI, yI, 'cyan')
    if vxI == 0 and vyI == 0:
        draw_stop (xI, yI)
    else:
        if x >= xI:
            draw_right (xI, yI)
            if y >= yI:
                canv.create_rectangle (xI - 4, yI - 6, xI, yI - 2, fill = 'blue', outline = 'blue', tag = 'Ghost')
                canv.create_rectangle (xI + 8, yI - 6, xI + 12, yI - 2, fill = 'blue', outline = 'blue', tag = 'Ghost')
            else:
                canv.create_rectangle (xI - 4, yI - 8, xI, yI - 4, fill = 'blue', outline = 'blue', tag = 'Ghost')
                canv.create_rectangle (xI + 8, yI - 8, xI + 12, yI - 4, fill = 'blue', outline = 'blue', tag = 'Ghost')
        else:
            draw_left (xI, yI)
            if y >= yI:
                canv.create_rectangle (xI - 12, yI - 6, xI - 8, yI - 2, fill = 'blue', outline = 'blue', tag = 'Ghost')
                canv.create_rectangle (xI, yI - 6, xI + 4, yI - 2, fill = 'blue', outline = 'blue', tag = 'Ghost')
            else:
                canv.create_rectangle (xI - 12, yI - 8, xI - 8, yI - 4, fill = 'blue', outline = 'blue', tag = 'Ghost')
                canv.create_rectangle (xI, yI - 8, xI + 4, yI - 4, fill = 'blue', outline = 'blue', tag = 'Ghost')
    move_Inky ()

def draw_Clyde ():
    global xC, yC
    draw_body (xC, yC, 'orange')
    if vxC == 0 and vyC == 0:
        draw_stop (xC, yC)
    else:
        if x >= xC:
            draw_right (xC, yC)
            if y >= yC:
                canv.create_rectangle (xC - 4, yC - 6, xC, yC - 2, fill = 'blue', outline = 'blue', tag = 'Ghost')
                canv.create_rectangle (xC + 8, yC - 6, xC + 12, yC - 2, fill = 'blue', outline = 'blue', tag = 'Ghost')
            else:
                canv.create_rectangle (xC - 4, yC - 8, xC, yC - 4, fill = 'blue', outline = 'blue', tag = 'Ghost')
                canv.create_rectangle (xC + 8, yC - 8, xC + 12, yC - 4, fill = 'blue', outline = 'blue', tag = 'Ghost')
        else:
            draw_left (xC, yC)
            if y >= yC:
                canv.create_rectangle (xC - 12, yC - 6, xC - 8, yC - 2, fill = 'blue', outline = 'blue', tag = 'Ghost')
                canv.create_rectangle (xC, yC - 6, xC + 4, yC - 2, fill = 'blue', outline = 'blue', tag = 'Ghost')
            else:
                canv.create_rectangle (xC - 12, yC - 8, xC - 8, yC - 4, fill = 'blue', outline = 'blue', tag = 'Ghost')
                canv.create_rectangle (xC, yC - 8, xC + 4, yC - 4, fill = 'blue', outline = 'blue', tag = 'Ghost')
    move_Clyde ()

def draw_walls ():
    global A
    for i in range (len (A)):
        canv.create_rectangle (h + A [i][0], h + A [i][1], h + A [i][2], h + A [i][3], fill = 'blue', outline = 'blue', tag = 'wall')

def draw_lives (n):
    for i in range (n):
        canv.create_arc (2 * r * i + 15, w - (15 + 2 * r), 2 * r * i + 15 + 2 * r, w - 15, start = 45, extent = 270, fill = 'yellow', outline = 'yellow', tag = 'live')

def scan_pac (P):
    global x, y, vx, vy, h, r
    #for i in range (len (A)):
    #if x - r >= Wx [0] and x - r <= Wx [1] or x + r >= Wx [0] and x + r <= Wx [1]:
        #if y - r >= Wy [0] and y - r <= Wy [1] or y + r >= Wy [0] and y + r <= Wy [1]:
            #if vx > 0:
                #vx = 0
                #x -= 2
            #elif vx < 0:
                #vx = 0
                #x += 2
            #if vy > 0:
                #vy = 0
                #y -= 2
            #elif vy < 0:
                #vy = 0
                #y += 2
        #else:
            #if Wx [0] >= x - r and Wx [0] <= x + r or Wx [1] >= x - r and Wx [1] <= x + r:
                #if Wy [0] >= y - r and Wy [0] <= y + r or Wy [1] >= y - r and Wy [1] <= y + r:
                    #vx = -vx
                    #vy = -vy
                    #if vx > 0:
                        #vx = 0
                        #x -= 2
                    #elif vx < 0:
                        #vx = 0
                        #x += 2
                    #if vy > 0:
                        #vy = 0
                        #y -= 2
                    #elif vy < 0:
                        #vy = 0
                        #y += 2
    #else:
        #if Wx [0] >= x - r and Wx [0] <= x + r or Wx [1] >= x - r and Wx [1] <= x + r:
            #if Wy [0] >= y - r and Wy [0] <= y + r or Wy [1] >= y - r and Wy [1] <= y + r:
                #if vx > 0:
                    #vx = 0
                    #x -= 2
                #elif vx < 0:
                    #vx = 0
                    #x += 2
                #if vy > 0:
                    #vy = 0
                    #y -= 2
                #elif vy < 0:
                    #vy = 0
                    #y += 2
    if ((x - r) - (P [2] + h)) * ((x + r) - (P [0] + h)) <= 0:
        if ((y - r) - (P [3] + h)) * ((y + r) - (P [1] + h)) <= 0:
            print (x, y)
            #vx = 0
            #vy = 0
            if x < P [0]:
                x -= 2
                vx = 0
            if x > P [2]:
                x += 2
                vx = 0
            if y < P [1]:
                y -= 2
                vy = 0
            if y > P [3]:
                y += 2
                vy = 0
            #if vx > 0:
                #vx = 0
                #x -= 2
            #elif vx < 0:
                #vx = 0
                #x += 2
            #elif vy > 0:
                #vy = 0
                #y -= 2
            #elif vy < 0:
                #vy = 0
                #y += 2

def check_ghosts ():
    global rB, rP, rI, rC, r, w
    if rB <= (r + 15) ** 2 or rP <= (r + 15) ** 2 or rI <= (r + 15) ** 2 or rC <= (r + 15) ** 2:
        l -= 1
        canv.create_rectangle (2 * r * l + 15, w - (15 + 2 * r), 2 * r * l + 15 + 2 * r, w - 15, fill = 'black')
        canv.update ()
        time.sleep (2)
        start ()

def draw ():
    global l1
    canv.delete ('Pac', 'Ghost')
    draw_pac ()
    draw_Blinky ()
    draw_Pinky ()
    draw_Inky ()
    draw_Clyde ()
    if l1 != l:
        draw_lives (l)
        l1 = l

def start ():
    global x, y, xB, yB, xP, yP, xI, yI, xC, yC
    global vx, vy, vxB, vyB, vxP, vyP, vxI, vyI, vxC, vyC
    global w, a, f
    global rB, rP, rI, rC
    x, y = w // 2, w // 2
    xB, yB = w // 4, w // 4
    xP, yP = 3 * w // 4, w // 4
    xI, yI = w // 4, 3 * w // 4
    xC, yC = 3 * w // 4, 3 * w // 4
    vx, vy = 0, 0
    vxB, vyB = 0, 0
    vxP, vyP = 0, 0
    vxI, vyI = 0, 0
    vxC, vyC = 0, 0
    a, f = 0, 1
    rB = ((w // 2 - w // 4) ** 2) * 2
    rP, rI, rC = rB, rB, rB
l = 3
l1 = l
s = 0

root.bind ('<Left>', moveleft)
root.bind ('<Right>', moveright)
root.bind ('<Up>', moveup)
root.bind ('<Down>', movedown)

#A = [[60, 60, 150, 120], [180, 60, 300, 120], [330, 30, 360, 120], [390, 60, 510, 120], [540, 60, 630, 120], [60, 150, 150, 180], [180, 150, 210, 300], [240, 150, 390, 180]]
#A = [[60, 60, 105, 90], [135, 60, 195, 90], [225, 30, 240, 90], [270, 60, 330, 90], [360, 60, 405, 90], [60, 120, 105, 135], [135, 120, 150, 225], [180, 120, 285, 135], [315, 120, 330, 225], [360, 120, 405, 135], [225, 135, 240, 180], [150, 165, 195, 180]]

v = [1, 0.5]
A = [[40, 40, 100, 80], [140, 40, 220, 80], [260, 0, 280, 80], [320, 40, 400, 80], [440, 40, 500, 80], [40, 120, 100, 140], [140, 120, 160, 260], [200, 120, 340, 140], [380, 120, 400, 260], [440, 120, 500, 140], [260, 140, 280, 200], [160, 180, 220, 200], [320, 180, 380, 200]]
draw_walls ()
draw_lives (l)
start ()

while l > 0:
    move_pac ()
    xB += vxB
    yB += vyB
    xP += vxP
    yP += vyP
    xI += vxI
    yI += vyI
    xC += vxC
    yC += vyC
    if x < r + 2:
        x = r + 2
        vx = 0
    if y < r + 2:
        y = r + 2
        vy = 0
    if x > w - (r + 2):
        x = w - (r + 2)
        vx = 0
    if y > w - (r + 2):
        y = w - (r + 2)
        vy = 0
    time.sleep (0.01)
    draw ()
    canv.update ()
    a += 3 * f
    if a == 0: f = 1
    elif a == 45: f = -1
    for i in range (len (A)):
        scan_pac (A [i])
    #scan_pac ()
    rB = (x - xB) ** 2 + (y - yB) ** 2
    rP = (x - xP) ** 2 + (y - yP) ** 2
    rI = (x - xI) ** 2 + (y - yI) ** 2
    rC = (x - xC) ** 2 + (y - yC) ** 2
    if rB <= (r + 14) ** 2 or rP <= (r + 14) ** 2 or rI <= (r + 14) ** 2 or rC <= (r + 14) ** 2:
        l -= 1
        canv.create_rectangle (2 * r * l + 15, w - (15 + 2 * r), 2 * r * l + 15 + 2 * r, w - 15, fill = 'black')
        canv.update ()
        time.sleep (2)
        x, y = w // 2, w // 2
        xB, yB = w // 4, w // 4
        xP, yP = 3 * w // 4, w // 4
        xI, yI = w // 4, 3 * w // 4
        xC, yC = 3 * w // 4, 3 * w // 4
        vx, vy = 0, 0
        if l> 0:
            draw ()
            canv.update ()
            time.sleep (2)

canv.create_text (w // 2, w // 2, text = 'GAME OVER', font = 'Times 72', justify = CENTER, fill = 'dark red')
canv.update ()

root.mainloop()