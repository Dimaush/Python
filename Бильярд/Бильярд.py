from math import *
import time

from tkinter import *
root = Tk ()
canv = Canvas (root, width = 900, height = 500)
canv.pack ()

canv.create_rectangle (100, 100, 800, 400, fill = 'darkgreen')

def sign (alpha):
    if alpha < 0: x = -1
    elif alpha > 0: x = 1
    else: x = 0
    return x

def draw_ball (x, y):
    canv.create_oval (x - 10, y - 10, x + 10, y + 10, fill = 'white', tag = 'ball')

def mouse (event):
    global vx, vy
    x1 = event.x
    y1 = event.y
    vx = (x - x1) / 30
    vy = (y - y1) / 30
    
    canv.delete ('kee')
    canv.create_line (x, y, x1, y1, tag = 'kee')

def skor (v1, v2):
    v = (v1 ** 2 + v2 ** 2) ** 0.5
    co = v1 / max (v, 0.0001)
    si = v2 / max (v, 0.0001)
    v = v - 0.01 * v ** 1
    v1 = co * v
    v2 = si * v
    if abs (v1) < 0.1: v1 = 0
    if abs (v2) < 0.1: v2 = 0
    return v1, v2

def draw_holes ():
    for i in range (6):
        canv.create_oval (H [i][0] - 15, H [i][1] - 15, H [i][0] + 15, H [i][1] + 15, fill = 'black')

H = [[100, 100], [450, 100], [800, 100], [100, 400], [450, 400], [800, 400]]
draw_holes ()

flag = 0
x, y = 250, 250
vx, vy = 0, 0
#f, a = map (int, input ().split ())
#alpha = a / 180 * pi
#vx = f * cos (alpha)
#vy = -f * sin (alpha)

root.bind ('<1>', mouse)

while flag == 0:
    x += vx
    y += vy
    #vx = abs (vx) * 0.99 * sign (vx)
    #vy = abs (vy) * 0.99 * sign (vy)
    #vx, vy = skor (vx), skor (vy)
    vx, vy = skor (vx, vy)
    
    canv.delete ('ball')
    draw_ball (x, y)
    canv.update ()
    time.sleep (0.01)
    #alpha = a / 180 * pi
    #vx = f * cos (alpha)
    #vy = -f * sin (alpha)
    if x <= 110 or x >= 790: vx = -vx
    if y <= 110 or y >= 390: vy = -vy
    for i in range (6):
        if (x - H [i][0]) ** 2 + (y - H [i][1]) ** 2 <= 225:
            flag = 1
            canv.delete ('ball')
            canv.update ()

root.mainloop ()