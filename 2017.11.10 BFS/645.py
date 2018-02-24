N = int (input ())
A = [0] * N
for i in range (N): A [i] = [0] * N
B = [0] * N
for i in range (N): B [i] = [0] * N
INF = 10 ** 10
pred = [0] * N
for i in range (N): pred [i] = [0] * N
P = []
for i in range (N):
    l = input ()
    for j in range (N):
        x = l [j]
        B [i][j] = x
        if x == '@':
            x0, y0 = i, j
            A [i][j] = 0
        elif x == 'O':
            P.append ((i, j))
            A [i][j] = INF
        elif x == '.': A [i][j] = INF
        elif x == 'X':
            x1, y1 = i, j
            A [i][j] = INF

q = [(x0, y0)]
while len (q) > 0:
    i, j = q.pop (0)
    if not (i, j - 1) in P and j - 1 >= 0:
        if A [i][j - 1] > A [i][j] + 1:
            A [i][j - 1] = A [i][j] + 1
            pred [i][j - 1] = (i, j)
            q += [(i, j - 1)]
    if not (i, j + 1) in P and j + 1 < N:
        if A [i][j + 1] > A [i][j] + 1:
            A [i][j + 1] = A [i][j] + 1
            pred [i][j + 1] = (i, j)
            q += [(i, j + 1)]
    if not (i - 1, j) in P and i - 1 >= 0:
        if A [i - 1][j] > A [i][j] + 1:
            A [i - 1][j] = A [i][j] + 1
            pred [i - 1][j] = (i, j)
            q += [(i - 1, j)]
    if not (i + 1, j) in P and i + 1 < N:
        if A [i + 1][j] > A [i][j] + 1:
            A [i + 1][j] = A [i][j] + 1
            pred [i + 1][j] = (i, j)
            q += [(i + 1, j)]

if A [x1][y1] == INF: print ('N')
else:
    print ('Y')
    F = (x1, y1)
    while F != (x0, y0):
        i, j = F
        if j - 1 >= 0 and A [i][j - 1] < A [i][j]:
            B [i][j] = '+'
            #B [i][j - 1] = '+'
            F = (i, j - 1)
        elif j + 1 < N and A [i][j + 1] < A [i][j]:
            B [i][j] = '+'
            #B [i][j + 1] = '+'
            F = (i, j + 1)
        elif i - 1 >= 0 and A [i - 1][j] < A [i][j]:
            B [i][j] = '+'
            #B [i - 1][j] = '+'
            F = (i - 1, j)
        elif i + 1 < N and A [i + 1][j] < A [i][j]:
            #B [i + 1][j] = '+'
            B [i][j] = '+'
            F = (i + 1, j)
    for i in range (N):
        for j in range (N): print (B [i][j], end = '')
        print ()