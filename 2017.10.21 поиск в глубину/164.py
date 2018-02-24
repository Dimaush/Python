N, S = map (int, input ().split ())
S -= 1
A = []
for i in range (N): A.append (list (map (int, input ().split ())))

visited = [0] * N

def DFS (S):
    global visited
    visited [S] = 1
    for M in range (N):
        if A [S][M] == 1 and visited [M] == 0: DFS (M)

DFS (S)
print (sum (visited))