WI, HE = 600, 600
h = 1

from tkinter import *
import time
root = Tk ()
canv = Canvas (root, width = WI, height = HE)
canv.pack ()

a, b, c = map (int, input ().split ())
canv.create_line (0, 300, 600, 300)
canv.create_line (300, 0, 300, 600)
canv.create_line (595 - h, 295, 600 - h, 300)
canv.create_line (595 - h, 305, 600 - h, 300)
canv.create_line (295, 5 + h, 300, h)
canv.create_line (305, 5 + h, 300, h)

x0, y0 = 0, 0
for x in range (WI + 1):
    d = 50
    x = x - WI // 2
    x1 = x / d
    y = a * x1 ** 2 + b * x1 + c
    y1 = HE // 2 - y * d
    x += WI // 2
    x1 = x
    canv.create_line (x0, y0, x1, y1)
    x0 ,y0 = x1, y1
    #canv.create_oval (x - 1, y1 - 1, x + 1, y1 + 1, fill = 'black')

root.mainloop ()