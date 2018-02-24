x0, y0, x, y = map (int, input ().split ())
dx = abs (x - x0)
dy = abs (y - y0)
kx, ky = 0, 0
while 3 ** kx < dx: kx += 1
while 3 ** ky < dy: ky += 1
kx1, ky1 = kx, ky
X, Y = [], []
while dx > 0:
    if 3 ** kx1 <= dx:
        X.append (kx1)
        dx -= 3 ** kx1
    kx1 -= 1
while dy > 0:
    if 3 ** ky1 <= dy:
        Y.append (ky1)
        dy -= 3 ** ky1
    ky1 -= 1
print (X, Y)
X, Y = set (X), set (Y)
S = X.intersection (Y)
if len (S) > 0: print ('NO')
else:
    print ('YES')
    K = []
    for i in range (max (kx, ky) + 1): K.append (i)
    for i in range (len (K)):
        if K [i] in X:
            if x > x0: print ('R', end = '')
            else: print ('L', end = '')
        elif K [i] in Y:
            if y > y0: print ('U', end = '')
            else: print ('D', end = '')
        else: print ('S', end = '')