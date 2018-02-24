N, M = map (int, input ().split ())
A = [0] * N
for i in range (N): A [i] = [0] * N
for i in range (M):
    p, q = map (int, input ().split ())
    A [p - 1][q - 1] = 1
    A [q - 1][p - 1] = 1

Color = [0] * N
x = 'YES'

def DFS (start):
    for u in range (N):
        if Color [u] == 0 and A [start][u] == 1:
            Color [u] = 3 - Color [start]
            DFS (u) 
        elif Color [u] == Color [start]: x = 'NO'

for i in range (N):
    if Color [i] == 0:
        Color [i] = 1
        DFS (i)

print (x)
if x == 'YES':
    for i in range (N):
        if Color [i] == 1: print (i + 1, end = ' ')