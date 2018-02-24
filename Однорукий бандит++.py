from tkinter import *
import random
root = Tk ()
canvas = Canvas (root, width=500, height=500)
canvas.pack ()
A = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range (3):
    for j in range (3):
        A[i][j] = random.randint (1, 6)
canvas.create_rectangle (100, 100, 400, 400)
canvas.create_line (100, 200, 400, 200)
canvas.create_line (100, 300, 400, 300)
canvas.create_line (200, 100, 200, 400)
canvas.create_line (300, 100, 300, 400)
for i in range (3):
    for j in range (3):
        if A[i][j] == 1:
            canvas.create_arc (150 + i * 100, 120 + j * 100, 140 + i * 100, 160 + j * 100, start = 270, extent = 180, style = ARC, outline = "green", width = 3)
            canvas.create_arc (125 + i * 100, 120 + j * 100, 165 + i * 100, 160 + j * 100, start = 0, extent = 90, style = ARC, outline = "green", width = 3)
            canvas.create_oval (140 + i * 100, 160 + j * 100, 155 + i * 100, 175 + j * 100, fill = "red")
            canvas.create_oval (160 + i * 100, 140 + j * 100, 175 + i * 100, 155 + j * 100, fill = "red")
        if A[i][j] == 2:
            canvas.create_oval (135 + i * 100, 130 + j * 100, 175 + i * 100, 170 + j * 100, fill = "yellow")
            canvas.create_arc (125 + i * 100, 130 + j * 100, 175 + i * 100, 180 + j * 100, start = 180, extent = 180, fill = "yellow", width = 1)
        if A[i][j] == 3:
            canvas.create_rectangle (110 + i * 100, 130 + j * 100, 190 + i * 100, 170 + j * 100, width = 4)
            canvas.create_text (150 + i * 100, 150 + j * 100, text = "BAR", fill = "black", font = ("Helvectica", "20"))
        if A[i][j] == 4:
            canvas.create_text (150 + i * 100, 150 + j * 100, text = "7", fill = "red", font = ("Helvectica", "60"))
        if A[i][j] == 5:
            canvas.create_oval (125 + i * 100, 125 + j * 100, 175 + i * 100, 175 + j * 100, fill = "red")
            canvas.create_arc (135 + i * 100, 115 + j * 100, 150 + i * 100, 135 + j * 100, start = 330, extent = 120, style = ARC, outline = "green", width = 3)
        if A[i][j] == 6:
            canvas.create_arc (130 + i * 100, 130 + j * 100, 190 + i * 100, 170 + j * 100, start = 90, extent = 180, style = CHORD, fill = "green")
            canvas.create_oval (145 + i * 100, 130 + j * 100, 170 + i * 100, 170 + j * 100, fill = "red")
if A[0][0] == A[0][1] == A[0][2]:
    canvas.create_text (250, 450, text = "YOU WIN!!!", fill = "blue", font = ("Helvectica", "60"))
elif A[1][0] == A[1][1] == A[1][2]:
    canvas.create_text (250, 450, text = "YOU WIN!!!", fill = "blue", font = ("Helvectica", "60"))
elif A[2][0] == A[2][1] == A[2][2]:
    canvas.create_text (250, 450, text = "YOU WIN!!!", fill = "blue", font = ("Helvectica", "60"))
elif A[0][0] == A[0][1] == A[0][2]:
    canvas.create_text (250, 450, text = "YOU WIN!!!", fill = "blue", font = ("Helvectica", "60"))
elif A[0][1] == A[1][1] == A[2][1]:
    canvas.create_text (250, 450, text = "YOU WIN!!!", fill = "blue", font = ("Helvectica", "60"))
elif A[0][2] == A[1][2] == A[2][2]:
    canvas.create_text (250, 450, text = "YOU WIN!!!", fill = "blue", font = ("Helvectica", "60"))
elif A[0][0] == A[1][1] == A[2][2]:
    canvas.create_text (250, 450, text = "YOU WIN!!!", fill = "blue", font = ("Helvectica", "60"))
elif A[2][0] == A[1][1] == A[0][2]:
    canvas.create_text (250, 450, text = "YOU WIN!!!", fill = "blue", font = ("Helvectica", "60"))

else:
    canvas.create_text (250, 450, text = "YOU LOSE...", fill = "blue", font = ("Helvectica", "60"))
root.mainloop ()