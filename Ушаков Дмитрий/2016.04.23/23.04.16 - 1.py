import random
import time
from tkinter import *
root = Tk ()
canv = Canvas (root, width = 600, height = 500)
canv.pack ()

A = [0] * 50
for i in range (len (A)):
    A[i] = random.randint (0, 49)