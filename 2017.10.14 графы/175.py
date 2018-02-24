N, M = map (int, input ().split ())
A = [0] * N
for i in range (M):
    i, j = map (int, input ().split ())
    A [i - 1] += 1
    A [j - 1] += 1
for k in range (N): print (A [k], end = ' ')