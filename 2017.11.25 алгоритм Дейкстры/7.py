k = 10 ** 10
N = int (input ())
cost = list (map (int, input ().split ()))

A = [0] * N
for i in range (N): A [i] = [k] * N

M = int (input ())
for i in range (M):
    i, j = map (int, input ().split ())
    i, j = i - 1, j - 1
    A [i][j], A [j][i] = cost [i], cost [j]

S, F = 0, N - 1
dist = [k] * N
dist [S] = 0
used = [False] * N
min_dist = 0
min_vertex = S
while min_dist < k:
    i = min_vertex
    used [i] = True
    for j in range (N):
        if min_dist + A [i][j] < dist [j]: dist [j] = min_dist + A [i][j]
    min_dist = k
    for j in range (N):
        if not used [j] and dist [j] < min_dist:
            min_dist = dist [j]
            min_vertex = j

if dist [F] == k: print (-1)
else: print (dist [F])