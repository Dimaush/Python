n, m = map (int, input ().split ())
A = []
for i in range (n):
    A.append (list ('.' * m))
for i in range (n):
    for j in range ((m + i % 2) // 2):
        A [i][j * 2 - i % 2 + 1] = '*'
for i in range (n):
    for j in range (m):
        print (A [i][j], end = ' ')
        if j == m - 1:
            print ()