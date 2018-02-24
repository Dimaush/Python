from tkinter import *
import time
root = Tk()
canv = Canvas (root, width = 600, height = 600)
canv.pack()

from math import *
import time

f = 0
R = 100
g = 0

while True:
    g += 0.05
    r = g / 360 * 2 * pi
    x = 1000
    canv.create_rectangle (300 + (R * sin (x * r)) * cos (r), 300 + (R * cos (x * r)) * sin (r), 300 + (R * sin (x * r)) * cos (r), 300 + (R * cos (x * r)) * sin (r))
    time.sleep (0.01)
    canv.update ()
    #canv.delete ('all')

root.mainloop ()