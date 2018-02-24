n = int (input ())
A = []
for i in range (n):
    A.append (list ('0' * n))
for i in range (n):
    A [i][n - i - 1] = 1
    for j in range (n):
        if n - j < i + 1:
            A [i][j] = 2

for i in range (n):
    for j in range (n):
        print (A [i][j], end = ' ')
        if j == n - 1:
            print ()