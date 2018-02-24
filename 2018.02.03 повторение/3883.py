def DFS (S):
    global visited, p
    visited [S] = 1
    p.append (S)
    for k in range (len (M [i])):
        if visited [M [i][k]] == 0: DFS (M [i][k])

n = int (input ())
m = int (input ())
M = [0] * n
for i in range (n): M [i] = []
for i in range (m):
    a, b = map (int, input ().split ())
    M [a - 1].append (b - 1)

V = []
for i in range (n):
    visited = [0] * n
    p = []
    DFS (i)
    V.append (p [1:])
#print (V)
