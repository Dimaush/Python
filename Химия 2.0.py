def LOL (a, b):
    global A1, B1
    global p
    global K
    if p < len (A1) + len (B1):
        if a == 0:
            for i in range (1, 21):
                K.append (i)
                LOL ()
        else:
            
        p += 1
        b += 1
        if b == len (A1) and a == 0:
            a = 1
            b = 0
    else:
        

print ('Введите исходные вещества и продукты реакции в формате K_(O-H):')
A = input ().split ()
B = input ().split ()
A1, B1 = [], []
for i in range (len (A)):
    A1 += [A [i].split ('_')]
for i in range (len (B)):
    B1 += [B [i].split ('_')]
for i in range (len (A1)):
    for j in range (len (A1 [i])):
        s = A1 [i][j]
        x = -1
        while s [x] >= '0' and s [x] <= '9' and x > -len (s): x -= 1
        if x == -1: A1 [i][j] = [1, s [:len (s)]]
        else: A1 [i][j] = [int (s [x + 1:]), s [:x + 1]]
for i in range (len (B1)):
    for j in range (len (B1 [i])):
        s = B1 [i][j]
        x = -1
        while s [x] >= '0' and s [x] <= '9': x -= 1
        if x == -1: B1 [i][j] = [1, s [:len (s)]]
        else: B1 [i][j] = [int (s [x + 1:]), s [:x + 1]]
for i in range (len (A1)):
    for j in range (len (A1 [i])):
        if A1 [i][j][-1][-1] == ')':
            s = A1 [i][j][-1]
            A1 [i][j] = A1 [i][j][:-1]
            s = s [1:-1]
            s = s.split ('-')
            for k in range (len (s)): A1 [i][j].append (s [k])
for i in range (len (B1)):
    for j in range (len (B1 [i])):
        if B1 [i][j][-1][-1] == ')':
            s = B1 [i][j][-1]
            B1 [i][j] = B1 [i][j][:-1]
            s = s [1:-1]
            s = s.split ('-')
            for k in range (len (s)): B1 [i][j].append (s [k])
for i in range (len (A1)):
    for j in range (len (A1 [i])):
        for k in range (1, len (A1 [i][j])):
            s = A1 [i][j][k]
            if s [-1] >= '1' and s [-1] <= '9':
                l = -1
                while s [l] >= '1' and s [l] <= '9': l -= 1
                A1 [i][j][k] = [s [l + 1:], s [:l + 1]]
for i in range (len (B1)):
    for j in range (len (B1 [i])):
        for k in range (1, len (B1 [i][j])):
            s = B1 [i][j][k]
            if s [-1] >= '1' and s [-1] <= '9':
                l = -1
                while s [l] >= '1' and s [l] <= '9': l -= 1
                B1 [i][j][k] = [s [l + 1:], s [:l + 1]]
print ()
print (A1, B1)
p = 0
K = []
LOL (0, 0)