import random
import time
from tkinter import *
root = Tk ()
canv = Canvas (root, width = 600, height = 500)
canv.pack ()

A = [0] * 100
for i in range (len (A)):
    A[i] = random.randint (1, 100)
for n in range(len (A)):
    for i in range (len (A) - n - 1):
        if A[i] > A[i + 1]:
            A[i], A[i + 1] = A[i + 1], A[i]
for k in range (0, len(A)):
    canv.create_rectangle (k * 5 + 50, 400, k * 5 + 53, 400 - 3 * A[k])
    
root.mainloop ()