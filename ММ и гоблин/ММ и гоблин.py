from tkinter import *

h = 600
r = 250

root = Tk ()
canv = Canvas (root, width = h, height = h)
canv.pack()

def mouse (event):
    x1 = event.x
    y1 = event.y
    
    a = x1 - h // 2
    b = y1 - h // 2
    c = (a ** 2 + b ** 2) ** 0.5
    t = r / c
    a = h // 2 + a * t
    b = h // 2 + b * t
    
    canv.delete ('MM')
    canv.delete ('goblin')
    canv.delete ('line')
    canv.create_oval (x1 - 3, y1 - 3, x1 + 3, y1 + 3, fill = 'black', tag = 'MM')    
    canv.create_oval (a - 5, b - 5, a + 5, b + 5, fill = 'black', tag = 'goblin')
    canv.create_line (h // 2, h // 2, a, b, tag = 'line')
    
canv.create_oval (h // 2 - r, h // 2 - r, h // 2 + r, h // 2 + r)
canv.create_oval (h // 2 - 1, h // 2 - 1, h // 2 + 1, h // 2 + 1, fill = 'black')

root.bind ('<1>', mouse)

root.mainloop()