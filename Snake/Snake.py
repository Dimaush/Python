from tkinter import *
import random
import time

def UP_ (event):
    global di
    di = 'w'
def DOWN_ (event):
    global di
    di = 's'
def LEFT_ (event):
    global di
    di = 'a'
def RIGHT_ (event):
    global di
    di = 'd'

def RAND_F ():
    global t, P, X
    flag = 0
    while flag == 0:
        i, j = random.randint (0, t - 1), random.randint (0, t - 1)
        S = [i, j]
        flag = 1
        for k in range (len (P)):
            if P [k] == S: flag = 0
        for k in range (len (WALLS)):
            if WALLS [k] == S: flag = 0
    return S

#def RAND_W ():
    #return m

def WALLS_ ():
    global W, X
    WALLS = []
    for q in range (len (W)):
        i, j = W [q][0], W [q][1]
        if i [0] == j [0]:
            s = min (i [1], j [1])
            #for k in range (abs (i [1] - j [1]) + 1): X [i [0]][s + k] = 'вЂ”'
            for k in range (abs (i [1] - j [1]) + 1): WALLS += [[i [0], s + k]]
            #X [i [0]][s + k] = '0'
        elif i [1] == j [1]:
            s = min (i [0], j [0])
            for k in range (abs (i [0] - j [0]) + 1): WALLS += [[s + k, i [1]]]
            #X [s + k][i [1]] = '0'
    return WALLS



print ('Введите сторону поля, от 3 до 16:', end = ' ')
t = input ()
#U = ('3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16')
#flag = 0
#while flag == 0:
    #if t in U: flag = 1
    #else:
        ##for i in range (18): print ()
        #print ('Попробуйте ещё раз. Число от 3 до 16:', end = ' ')
        #t = input ()
t = int (t) + 2

size = 20
h = 100      

P = [[random.randint (1, t - 2), random.randint (1, t - 2)]]

#W = open ('WALLS.txt')
#W = W.readlines ()

di = 'o'
lose = 0

X = [0] * t
for i in range (t): X [i] = ['.'] * t

W = [[[0, 0], [0, t - 1]], [[t - 1, 0], [t - 1, t - 1]], [[1, 0], [t - 2, 0]], [[1, t - 1], [t - 2, t - 1]]]
WALLS = WALLS_ ()
for i in range (len (WALLS)): X [WALLS [i][0]][WALLS [i][1]] = '#'

fruit = 0
F = RAND_F ()
X [F [0]][F [1]] = '$'
X [P [0][0]][P [0][1]] = '@'
q = P [-1]

if t > 6:
    print ('Включить сложный режим? Y/N:', end = ' ')
    ans = input ()
    flag = 0
    while flag == 0:
        if ans == 'Y':
            hard = 1
            flag = 1
        elif ans == 'N':
            hard = 0
            flag = 1
        else:
            #for i in range (18): print ()
            print ('Попробуйте ещё раз. Y/N:', end = ' ')
            ans = input ()
else: hard = 0

print ('Выберите уровень сложности по шкале от 1 до 10:', end = ' ')
z = input ()
Y = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
flag = 0
while flag == 0:
    if z in Y: flag = 1
    else:
        #for i in range (18): print ()
        print ('Попробуйте ещё раз. Число от 1 до 10:', end = ' ')
        z = input ()
z = int (z)
z = (11 - z) / 50

if hard == 1:
    k = 5
    S = []
    u = min (max (0, q [0] - 2), t - 5)
    v = min (max (0, q [1] - 2), t - 5)
    for i in range (5): S.append (X [u + i][v:v + 5])
    #for i in range (6): print ()
    #for i in range (5): print (*S [i])
    #for i in range (7): print ()
else:
    k = t
    #for i in range (9 - t // 2 - t % 2): print ()
    #for i in range (t): print (*X [i])
    #for i in range (9 - t // 2): print ()

root = Tk ()
canvas = Canvas (root, width = 2 * h + k * size, height = 2 * h + k * size)
canvas.pack ()

root.bind ('<Left>', LEFT_)
root.bind ('<Right>', RIGHT_)
root.bind ('<Up>', UP_)
root.bind ('<Down>', DOWN_)

di = 'o'

while lose == 0 and len (P) < t ** 2 - len (WALLS):
    #if hard == 1:
        #canvas.create_rectangle (h, h, h + 5 * size, h + 5 * size, fill = 'white')
        #for i in range (4): canvas.create_line (h, h + (i + 1) * size, h + 5 * size, h + (i + 1) * size)
        #for i in range (4): canvas.create_line (h + (i + 1) * size, h, h + (i + 1) * size, h + 5 * size)
    #else:
        #canvas.create_rectangle (h, h, h + t * size, h + t * size, fill = 'white')
        #for i in range (t - 1): canvas.create_line (h, (i + 1) * size + h, t * size + h, (i + 1) * size + h)
        #for i in range (t - 1): canvas.create_line ((i + 1) * size + h, h, (i + 1) * size + h, t * size + h)
    
    #di = input ()
    #flag = 0
    #while flag == 0:
        #if di1 != 'w' and di1 != 'a' and di1 != 's' and di1 != 'd':
            #if hard == 1:
                #for i in range (5): print (*S [i])
                #for i in range (7): print ()
            #else:
                #for i in range (t): print (*X [i])
                #for i in range (9 - t // 2): print ()
            #print ('РџРѕРїСЂРѕР±СѓР№С‚Рµ РµС‰С‘ СЂР°Р·:', end = ' ')
            #di1 = input ()
            #if hard == 1:
                #for i in range (6): print ()
            #else:
                #for i in range (9 - t // 2 - t % 2): print ()
        #elif di1 == 's' and di != 'w': flag = 1
        #elif di1 == 'a' and di != 'd': flag = 1
        #elif di1 == 'd' and di != 'a': flag = 1
        #elif di1 == 'w' and di != 's': flag = 1
        #else:
            #if len (P) != 1:
                #lose = 1
            #flag = 1
    
    #di = di1
    
    time.sleep (z)
    
    if di == 'w': q = [P [-1][0] - 1, P [-1][1]]
    elif di == 's': q = [P [-1][0] + 1, P [-1][1]]
    elif di == 'a': q = [P [-1][0], P [-1][1] - 1]
    elif di == 'd': q = [P [-1][0], P [-1][1] + 1]
    P += [q]
    
    #for i in range (len (P)):
        #if P [i][0] < 0: P [i][0] = t - 1
        #if P [i][0] > t - 1: P [i][0] = 0
        #if P [i][1] < 0: P [i][1] = t - 1
        #if P [i][1] > t - 1: P [i][1] = 0
    
    X = [0] * t
    for i in range (t): X [i] = ['.'] * t
    
    for i in range (len (WALLS)): X [WALLS [i][0]][WALLS [i][1]] = '#'
    
    if P [-1] == F: fruit = 1
    #if len (P) < t ** 2 - len (WALLS):
    if fruit == 1 and len (P) < t ** 2 - len (WALLS):
        F = RAND_F ()
        fruit = 0
    elif fruit == 1: fruit = 0
    else:
        l = P [0]
        P = P [1:]
    X [F [0]][F [1]] = '$'
    
    for i in range (len (P)):
        if X [P [i][0]][P [i][1]] != '@' and X [P [i][0]][P [i][1]] != '#': X [P [i][0]][P [i][1]] = '@'
        else: lose = 1
    
    canvas.create_rectangle (h, h, h + k * size, h + k * size, fill = 'white')
    for i in range (k - 1): canvas.create_line (h, h + (i + 1) * size, h + k * size, h + (i + 1) * size)
    for i in range (k - 1): canvas.create_line (h + (i + 1) * size, h, h + (i + 1) * size, h + k * size)
    
    for i in range (len (WALLS)):
        canvas.create_rectangle (h + WALLS [i][1] * size, h + WALLS [i][0] * size, h + (WALLS [i][1] + 1) * size, h + (WALLS [i][0] + 1) * size, fill = 'black')
    
    if hard == 1:
        S = []
        u = min (max (0, q [0] - 2), t - 5)
        v = min (max (0, q [1] - 2), t - 5)
        for i in range (5): S.append (X [u + i][v:v + 5])
    
        if lose == 0:
            #for i in range (5): print (*S [i])
            for i in range (len (P)):
                if abs (P [i][0] - P [-1][0]) < 3 and abs (P [i][1] - P [-1][1]) < 3:
                #if S [i // 5][i % 5] == '@':
                    canvas.create_oval (size // 4 + h + (2 + P [i][1] - P [-1][1]) * size, size // 4 + h + (2 + P [i][0] - P [-1][0]) * size, 3 * size // 4 + h + (2 + P [i][1] - P [-1][1]) * size, 3 * size // 4 + h + (2 + P [i][0] - P [-1][0]) * size)
                    #canvas.create_oval (size // 4 + h + P [i][1] * size, size // 4 + h + P [i][0] * size, 3 * size // 4 + h + P [i][1] * size, 3 * size // 4 + h + P [i][0] * size)
            #for i in range (7): print ()
        #else:
            #for i in range (1): print ()
        
        #for i in range (len (WALLS)):
            #canvas.create_rectangle ()
    else:
        if lose == 0:
            #for i in range (t): print (*X [i])
            canvas.create_oval (size // 4 + h + l [1] * size, size // 4 + h + l [0] * size, 3 * size // 4 + h + l [1] * size, 3 * size // 4 + h + l [0] * size, outline = 'white')
            
            for i in range (len (P)): print (P [i])
            print ()
            
            for i in range (len (P)):
                canvas.create_oval (size // 4 + h + P [i][1] * size, size // 4 + h + P [i][0] * size, 3 * size // 4 + h + P [i][1] * size, 3 * size // 4 + h + P [i][0] * size)
            #for i in range (9 - t // 2): print ()
        #else:
            #for i in range (1 + t % 2): print ()
    
    canvas.create_rectangle (size // 4 + h + F [1] * size, size // 4 + h + F [0] * size, 3 * size // 4 + h + F [1] * size, 3 * size // 4 + h + F [0] * size)
    
    canvas.update ()
    
    #di = input ()

#for i in range (t // 2 - 2): print ()
if len (P) < t ** 2 - len (WALLS):
    print ('Вы проиграли! Ваша длина:', end = ' ')
    print (len (P), end = '.')
else: print ('Поздравляю! Вы заняли всё поле и выиграли!')
#for i in range (7): print ()

root.mainloop ()