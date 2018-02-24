def D (S, F):
    global N, A
    dist = [INF] * N
    roads = [0] * N
    for i in range (N): roads [i] = []
    used = [False] * N
    dist [S] = 0
    roads [S] = [S + 1]
    min_dist = 0
    min_vertex = S
    
    while min_dist < INF:
        i = min_vertex
        used [i] = True
        for j in range (N):
            if min_dist + A [i][j] < dist [j]:
                dist [j] = min_dist + A [i][j]
                roads [j] = roads [i] + [j + 1]
        min_dist = INF
        for j in range (N):
            if not used [j] and dist [j] < min_dist:
                min_dist = dist [j]
                min_vertex = j
    return roads [F]

N, K, M = map (int, input ().split ())
INF = 10 ** 9
A = [0] * N
for i in range (N): A [i] = [INF] * N
for i in range (M):
    s, f, l = map (int, input ().split ())
    s, f = s - 1, f - 1
    A [s][f] = min (l, A [s][f])
    A [f][s] = min (l, A [f][s])
#for i in range (N): print (* A [i])

ans0 = []
ans1 = D (K - 1, N - 1)

if ans1 == []: print (-1)
else:
    x = 0
    for i in range (len (ans1) - 1):
        x += A [ans1 [i] - 1][ans1 [i + 1] - 1]
        A [ans1 [i] - 1][ans1 [i + 1] - 1] = INF
        A [ans1 [i + 1] - 1][ans1 [i] - 1] = INF
    ans0.append (x)
    
    ans2 = D (N - 1, K - 1)
    
    if ans2 == []: print (-1)
    else:
        x = 0
        for i in range (len (ans2) - 1):
            x += A [ans2 [i] - 1][ans2 [i + 1] - 1]
        ans0.append (x)
        print (ans0 [0], ans0 [1])
        print (* ans1)
        print (* ans2)