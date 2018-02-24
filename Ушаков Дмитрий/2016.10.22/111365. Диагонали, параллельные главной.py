n = int (input ())
A = []
for i in range (n):
    A.append (list ('0' * n))
for i in range (n):
    for j in range (n):
        A [i][j] = max (i - j, j - i)
for i in range (n):
    for j in range (n):
        print (A [i][j], end = ' ')
        if j == n - 1:
            print ()