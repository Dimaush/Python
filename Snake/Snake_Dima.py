import random

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
            #for k in range (abs (i [1] - j [1]) + 1): X [i [0]][s + k] = '—'
            for k in range (abs (i [1] - j [1]) + 1): WALLS += [[i [0], s + k]]
            #X [i [0]][s + k] = '0'
        elif i [1] == j [1]:
            s = min (i [0], j [0])
            for k in range (abs (i [0] - j [0]) + 1): WALLS += [[s + k, i [1]]]
            #X [s + k][i [1]] = '0'
    return WALLS

for i in range (5): print ('*')
print ('Приветствую, игрок! Управление: wasd.')
print ('Введите сторону поля, от 3 до 16:', end = ' ')
t = input ()
U = ('3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16')
flag = 0
while flag == 0:
    if t in U: flag = 1
    else:
        for i in range (18): print ('7')
        print ('Попробуйте ещё раз. Число от 3 до 16:', end = ' ')
        t = input ()
t = int (t) + 2

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
            for i in range (18): print ('8')
            print ('Попробуйте ещё раз. Y/N:', end = ' ')
            ans = input ()
else: hard = 0

if hard == 1:
    S = []
    u = min (max (0, q [0] - 2), t - 5)
    v = min (max (0, q [1] - 2), t - 5)
    for i in range (5): S.append (X [u + i][v:v + 5])
    for i in range (6): print ('(')
    for i in range (5): print (*S [i])
    for i in range (7): print (')')
else:
    for i in range (9 - t // 2 - t % 2): print ('0')
    for i in range (t): print (*X [i])
    for i in range (9 - t // 2): print ('9')

o = t ** 2 - len (WALLS)

while lose == 0 and len (P) < o:
    print ('Введите новое направление:', end = ' ')
    di1 = input ()
    if hard == 1:
        for i in range (6): print (':')
    else:
        for i in range (9 - t // 2 - t % 2): print (':')
    flag = 0
    while flag == 0:
        if di1 != 'w' and di1 != 'a' and di1 != 's' and di1 != 'd':
            if hard == 1:
                for i in range (5): print (*S [i])
                for i in range (7): print ('!')
            else:
                for i in range (t): print (*X [i])
                for i in range (9 - t // 2): print ('!')
            print ('Попробуйте ещё раз:', end = ' ')
            di1 = input ()
            if hard == 1:
                for i in range (6): print ('?')
            else:
                for i in range (9 - t // 2 - t % 2): print ('?')
        elif di1 == 's' and di != 'w': flag = 1
        elif di1 == 'a' and di != 'd': flag = 1
        elif di1 == 'd' and di != 'a': flag = 1
        elif di1 == 'w' and di != 's': flag = 1
        else:
            if len (P) != 1:
                lose = 1
            flag = 1
            
            #for i in range (len (X)): print (*X [i])
            #for i in range (9 - t // 2 - t % 2): print ()
            #print ('В этом случае Вы проиграете! Уверены? Y/N ', end = '')
            #ans = input ()
            #for i in range (10 - t // 2): print ()
            #if ans == 'Y':
                #flag = 1
                #lose = 1
            #else:
                #for i in range (len (X)): print (*X [i])
                #for i in range (9 - t // 2 - t % 2): print ()
                #print ('Введите новое направление:', end = ' ')
                #di1 = input ()
                #for i in range (10 - t // 2): print ()
            
    di = di1
    if di == 'w': q = [P [-1][0] - 1, P [-1][1]]
    elif di == 's': q = [P [-1][0] + 1, P [-1][1]]
    elif di == 'a': q = [P [-1][0], P [-1][1] - 1]
    else: q = [P [-1][0], P [-1][1] + 1]
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
    else: P = P [1:]
    X [F [0]][F [1]] = '$'
    
    for i in range (len (P)):
        if X [P [i][0]][P [i][1]] != '@' and X [P [i][0]][P [i][1]] != '#': X [P [i][0]][P [i][1]] = '@'
        else: lose = 1
    
    if hard == 1:
        S = []
        u = min (max (0, q [0] - 2), t - 5)
        v = min (max (0, q [1] - 2), t - 5)
        for i in range (5): S.append (X [u + i][v:v + 5])
    
        if lose == 0:
            for i in range (5): print (*S [i])
            for i in range (7): print ('_')
        else:
            for i in range (1): print ('_')
    else:
        if lose == 0:
            for i in range (t): print (*X [i])
            for i in range (9 - t // 2): print ('-')
        else:
            for i in range (1 + t % 2): print ('-')

for i in range (t // 2 - 2): print ('+')
if len (P) < t ** 2 - len (WALLS):
    print ('Вы проиграли! Ваша длина:', end = ' ')
    print (len (P), end = '.')
else: print ('Поздравляю! Вы заняли всё поле и выиграли!')
for i in range (7): print ('&')