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
    m = A[n]
    for j in range (len(A) - n):
        if A[j + n] > m:
            m = A[j + n]
            x = j + n
    A[n], A[x] = m, A[n]
for k in range (0, len(A)):
    canv.create_rectangle (k * 5 + 50, 400, k * 5 + 53, 400 - 3 * A[k])
    
root.mainloop ()