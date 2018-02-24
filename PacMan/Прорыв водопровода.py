m, n = map (int, input ().split ())
m += 2
n += 2
A = [0] * n
for i in range (n): A [i] = [-2] * m
A [0] = ['-'] * m
A [-1] = ['-'] * m
for i in range (n - 2):
    A [i + 1][0] = '-'
    A [i + 1][-1] = '-'
x, y = map (int, input ().split ())
x1, y1 = map (int, input ().split ())
A [x][y] = 0
q = []
q += [(x, y)]
while len (q) > 0:
    i, j = q.pop (0)
    if A [i][j - 1] == -2:
        A [i][j - 1] = A [i][j] + 1
        q += [(i, j - 1)]
    if A [i][j + 1] == -2:
        A [i][j + 1] = A [i][j] + 1
        q += [(i, j + 1)]
    if A [i - 1][j] == -2:
        A [i - 1][j] = A [i][j] + 1
        q += [(i - 1, j)]
    if A [i + 1][j] == -2:
        A [i + 1][j] = A [i][j] + 1
        q += [(i + 1, j)]
for i in range (n): print (* A [i])
print (A [x1][y1])

xt, yt = x1, y1
S = [(xt, yt)]
while A [xt][yt] > 0:
    if A [xt][yt - 1] < A [xt][yt]:
        xt, yt = xt, yt - 1
        S += [(xt, yt)]
    if A [xt][yt + 1] < A [xt][yt]:
        xt, yt = xt, yt + 1
        S += [(xt, yt)]
    if A [xt - 1][yt] < A [xt][yt]:
        xt, yt = xt - 1, yt
        S += [(xt, yt)]
    if A [xt + 1][yt] < A [xt][yt]:
        xt, yt = xt + 1, yt
        S += [(xt, yt)]
S = S [::-1]
print (* S)