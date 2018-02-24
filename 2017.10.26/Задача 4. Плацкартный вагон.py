n = int (input ())

A = [0] * 9
for i in range (9): A [i] = [0] * 6
for i in range (n):
    a = int (input ())
    if a < 37: A [(a - 1) // 4][(a - 1) % 4] = 1
    else: A [(54 - a) // 2][5 - a % 2] = 1

S = []
for i in range (9):
    if sum (A [i]) == 6: S.append (i)
#print (S)

P = [0] * 9
for i in range (len (S)): P [S [i]] = 1
#print (P)

x = 0
m = 0
for i in range (9):
    if P [i] == 1: x += 1
    else:
        m = max (m, x)
        x = 0

print (max (m, x))