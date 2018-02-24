import random
from tkinter import *
root = Tk ()
canv = Canvas (root, width = 500, height = 500)
canv.pack ()

def draw ():
    A = [0] * 100
    for i in range (0, 100):
        A[i] = random.randint (1, 100)
    for i in range (1, 100):
        canv.create_rectangle (i * 5, 450, i * 5 + 3, 400 - 3 * A[i])
    canv.update
draw ()
root.mainloop ()