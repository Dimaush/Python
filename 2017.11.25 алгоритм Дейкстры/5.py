N, S, F = map (int, input ().split ())
S, F = S - 1, F - 1
A = [0] * N
k = 10 ** 10
for i in range (N):
    l = list (map (int, input ().split ()))
    for j in range (N):
        if l [j] == -1: l [j] = k
    A [i] = l
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