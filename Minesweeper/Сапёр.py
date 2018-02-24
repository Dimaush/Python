from tkinter import *
root = Tk ()
canv = Canvas (root, width = 500, height = 500)
canv.pack (fill = BOTH)

import random

def but1 (event):
    x = (event.x - 50) // 20
    y = (event.y - 50) // 20
    draw_mine (x, y)
    
def but3 (event):
    x = (event.x - 50) // 20
    y = (event.y - 50) // 20
    draw_flag (x, y)

def clear (event):
    #canv.create_rectangle (50, 50, 450, 450, fill = 'grey', tag = 'field')
    #for i in range (21):
        #canv.create_line (50, 50 + i * 20, 450, 50 + i * 20)
        #canv.create_line (50 + i * 20, 50, 50 + i * 20, 450)
    for i in range (m):
        for j in range (m):
            i, j = i + 3, j + 3
            canv.create_rectangle (i * 20 - 8, j * 20 - 8, i * 20 + 8, j * 20 + 8, fill = 'grey', outline = 'grey', tag = 'field')
            canv.create_line (i * 20 - 9, j * 20 + 9, i * 20 - 9, j * 20 - 9, i * 20 + 9, j * 20 - 9, width = 2, fill = 'white')
            canv.create_line (i * 20 - 9, j * 20 + 9, i * 20 + 9, j * 20 + 9, i * 20 + 9, j * 20 - 9, width = 2, fill = 'black')
            #canv.crrate_text (i * 20, j * 20, text = 'LOL')
            i, j = i - 3, j - 3

def push (event):
    x = (event.x - 50) // 20
    y = (event.y - 50) // 20
    x, y = x + 3, y + 3
    canv.create_rectangle (x * 20 - 10, y * 20 - 10, x * 20 + 9, y * 20 + 9, fill = 'grey', outline = 'grey', tag = 'field')
    oopen (x, y)
    #canv.create_line (x * 20 - 9, y * 20 + 9, x * 20 - 9, y * 20 - 9, x * 20 + 9, y * 20 - 9, width = 2, fill = 'black')
    #canv.create_line (x * 20 - 9, y * 20 + 9, x * 20 + 9, y * 20 + 9, x * 20 + 9, y * 20 - 9, width = 2, fill = 'white')

def oopen (x, y):
    p = A [y][x]
    if p // 10 % 10 != 1 and x * y * (m - x) * (n - y) != 0:
        A [y][x] -= p // 10 % 10 * 10 + 10
        if p // 100 == 1: finish ()
        elif p % 10 > 0: canv.create_text (x * 20, y * 20, text = p % 10)
        else:
            canv.create_rectangle (x * 20 - 10, x * 20 - 10, x * 20 + 10, x * 20 + 10)
            oopen (x - 1, y - 1)
            oopen (x, y - 1)
            oopen (x + 1, y - 1)
            oopen (x - 1, y)
            oopen (x + 1, y)
            oopen (x - 1, y + 1)
            oopen (x, y + 1)
            oopen (x + 1, y + 1)

def finish ():
    canv.create_text (250, 250, text = 'FINISH HIM', font = 'Times New Roman', size = 72)

def pushsmile (event):
    #canv.create_rectangle (x * 20 - 8, y * 20 - 8, x * 20 + 8, y * 20 + 8, fill = 'grey', outline = 'grey', tag = 'field')
    #canv.create_line (x * 20 - 9, y * 20 + 9, x * 20 - 9, y * 20 - 9, x * 20 + 9, y * 20 - 9, width = 2, fill = 'black')
    #canv.create_line (x * 20 - 9, y * 20 + 9, x * 20 + 9, y * 20 + 9, x * 20 + 9, y * 20 - 9, width = 2, fill = 'white')
    i, j = 12.5, 1.5
    #canv.create_rectangle (240, 20, 260, 40, fill = 'grey', outline = 'grey', tag = 'smile')
    canv.create_line (i * 20 - 9, j * 20 + 9, i * 20 - 9, j * 20 - 9, i * 20 + 9, j * 20 - 9, width = 2, fill = 'black')
    canv.create_line (i * 20 - 9, j * 20 + 9, i * 20 + 9, j * 20 + 9, i * 20 + 9, j * 20 - 9, width = 2, fill = 'white')    

def draw_mine (x, y):
    x = (event.x - 50) // 20
    y = (event.y - 50) // 20
    x, y = x + 3, y + 3
    canv.create_oval (x * 20 - 6, y * 20 - 6, x * 20 + 6, y * 20 + 6, fill = 'black')
    canv.create_rectangle (x * 20 - 1, y * 20 - 8, x * 20 + 1, y * 20 + 8, fill = 'black')
    canv.create_rectangle (x * 20 - 8, y * 20 - 1, x * 20 + 8, y * 20 + 1, fill = 'black')
    canv.create_rectangle (x * 20 - 6, y * 20 - 6, x * 20 - 4, y * 20 - 4, fill = 'black')
    canv.create_rectangle (x * 20 - 6, y * 20 + 6, x * 20 - 4, y * 20 + 4, fill = 'black')
    canv.create_rectangle (x * 20 + 6, y * 20 - 6, x * 20 + 4, y * 20 - 4, fill = 'black')
    canv.create_rectangle (x * 20 + 6, y * 20 + 6, x * 20 + 4, y * 20 + 4, fill = 'black')
    canv.create_rectangle (x * 20 - 4, y * 20 - 4, x * 20 - 1, y * 20 - 1, fill = 'white')

def draw_flag (event):
    x = (event.x - 50) // 20
    y = (event.y - 50) // 20
    x, y = x + 3, y + 3
    canv.create_rectangle (x * 20 - 6, y * 20 + 5, x * 20 + 6, y * 20 + 6, fill = 'black')
    canv.create_rectangle (x * 20, y * 20, x * 20 + 1, y * 20 + 5, fill = 'black')
    canv.create_polygon ([x * 20 + 2, y * 20 + 2], [x * 20 - 5, y * 20 - 3], [x * 20 + 2, y * 20 - 8], fill = 'red')

m, n = 20, 20

#main = canv.create_rectangle (240, 20, 260, 40, fill = 'grey', tag = 'smile')
i, j = 12.5, 1.5
canv.create_rectangle (240, 20, 260, 40, fill = 'grey', outline = 'grey', tag = 'smile')
canv.create_line (i * 20 - 9, j * 20 + 9, i * 20 - 9, j * 20 - 9, i * 20 + 9, j * 20 - 9, width = 2, fill = 'white')
canv.create_line (i * 20 - 9, j * 20 + 9, i * 20 + 9, j * 20 + 9, i * 20 + 9, j * 20 - 9, width = 2, fill = 'black')

#square = canv.create_rectangle (50, 50, 450, 450, fill = 'grey', tag = 'field')
#for i in range (21):
    #canv.create_line (50, 50 + i * 20, 450, 50 + i * 20)
    #canv.create_line (50 + i * 20, 50, 50 + i * 20, 450)
    
for i in range (m):
    for j in range (m):
        i, j = i + 3, j + 3
        canv.create_rectangle (i * 20 - 8, j * 20 - 8, i * 20 + 8, j * 20 + 8, fill = 'grey', outline = 'grey', tag = 'field')
        canv.create_line (i * 20 - 9, j * 20 + 9, i * 20 - 9, j * 20 - 9, i * 20 + 9, j * 20 - 9, width = 2, fill = 'white')
        canv.create_line (i * 20 - 9, j * 20 + 9, i * 20 + 9, j * 20 + 9, i * 20 + 9, j * 20 - 9, width = 2, fill = 'black')
        i, j = i - 3, j - 3

A = [0] * (n + 1)
for i in range (n + 1): A [i] = [0] * (m + 1)
k, l = random.randint (1, m), random.randint (1, n)
for i in range ((m * n) // 5):
    while A [k][l] != 0: k, l = random.randint (1, m - 1), random.randint (1, n - 1)
    A [k][l] = 100
for i in range (1, n):
    for j in range (1, m):
        A [i][j] += (A [i - 1][j - 1] + A [i][j - 1] + A [i + 1][j - 1] + A [i - 1][j] + A [i + 1][j] + A [i - 1][j + 1] + A [i][j + 1] + A [i + 1][j + 1]) // 100
for i in range (1, n):
    for j in range (1, m):
        A [i][j] += 10

canv.tag_bind ('field', '<Button-1>', but1)
canv.tag_bind ('field', '<Button-1>', push)
canv.tag_bind ('field', '<Button-3>', draw_flag)
canv.tag_bind ('smile', '<Button-1>', clear)
#canv.tag_bind ('smile', '<Button-1>', pushsmile)

root.mainloop ()