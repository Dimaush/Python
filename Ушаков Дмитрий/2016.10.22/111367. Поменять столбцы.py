n, m = map (int, input().split())
A = []
for i in range (n):
    A.append (list (map (int, input ().split ())))
k, l = map (int, input().split())
for i in range (n):
    x, y = A [i][k], A [i][l]
    A [i][k], A [i][l] = y, x
for i in range (n):
    for j in range (m):
        print (A [i][j], end = ' ')
        if j == m - 1:
            print ()