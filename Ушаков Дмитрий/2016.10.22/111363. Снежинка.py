n = int (input ())
A = []
for i in range (n):
    A.append (list ('.' * n))
for i in range (n):
    A [i][n // 2] = '*'
for i in range (n):
    A [n // 2][i] = '*'
for i in range (n):
    A [i][i] = '*'
for i in range (n):
    A [i][n - i - 1] = '*'
for i in range (n):
    for j in range (n):
        print (A [i][j], end = ' ')
        if j == n - 1:
            print ()