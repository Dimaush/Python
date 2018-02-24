import random
from tkinter import *
root = Tk ()
canv = Canvas (root, width = 500, height = 500)

canv.pack ()

A = [0] * 50
for i in range (len (A)):
    A[i] = random.randint (0, 9)

B = [0] * 10
for j in range (50):
    B[A[j]] += 1

C = ["red", "orange", "yellow", "green", "lightblue", "blue", "purple", "darkred", "darkgreen", "darkblue"]

for k in range (len(A)):
    canv.create_rectangle (k * 8 + 50, 400, k * 8 + 55, 400 - 20 * A[k], fill = C[A[k]])

for d in range (10):
    canv.create_rectangle (d * 8 + 50, 200, d * 8 + 55, 200 - 20 * B[d], fill = C[d])

root.mainloop()