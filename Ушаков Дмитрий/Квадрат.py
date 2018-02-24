from tkinter import *
import time
root = Tk()
canv = Canvas (root, width = 600, height = 600)
canv.pack()

from math import *
import time

f = 0
R = 50
R1 = R * (2 ** 0.5)
R2 = R * 2
#R12 = 40
#R34 = 40 * 3 ** 0.5 / 2 ** 0.5
g = 0
a = 0

def rotateleft (event):
    global g
    g += 1
def rotateright (event):
    global g
    g -= 1

root.bind ('<Left>', rotateright)
root.bind ('<Right>', rotateleft)

canv.create_oval (299, 299, 301, 301)

while True:
    r = g / 180 * pi
    x = 100
    u1 = 45
    u2 = 30
    #u34 = asin (R12 *  sin (u12) / R34)
    #u34 = u34 / pi * 180
    #a = R12 ** 2 * sin (u12) ** 2
    #b = R34 ** 2 - R12 ** 2 * sin (u12) ** 2
    #u34 = atan ((a / b) ** 0.5)
    canv.create_polygon (300 + R1 * cos (r + u1), 300 + R1 * sin (r + u1), 300 + R1 * cos (r - u1), 300 + R1 * sin (r - u1), 300 + R1 * cos (r - u1-u2), 300 + R1 * sin (r - u1),tag = 'square')

    #canv.create_rectangle (300 + R * cos (r), 300 + R * sin (r), 300 + R * cos (r), 300 + R * sin (r))
    time.sleep (0.01)
    canv.update ()
    canv.delete ('square')

root.mainloop ()