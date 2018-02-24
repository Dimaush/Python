N = int (input ())
A = []
for i in range (N): A.append (list (map (int, input ().split ())))
S, F = map (int, input ().split ())
S, F = S - 1, F - 1

INF = 10 ** 9
dist = [INF] * N
dist [S] = 0
q = [S]
pred = [N + 1] * N
while q:
    x = q.pop (0)
    for i in range (N):
        if A [x][i] == 1 and dist [i] == INF:
            q += [i]
            pred [i] = x
            dist [i] = dist [x] + 1

#print (pred)
k = dist [F]
c = F
P = []
if k == 0: print (k)
elif pred [c] == N + 1: print (-1)
else:
    print (k)
    for i in range (k):
        P.append (pred [c] + 1)
        c = pred [c]
    print (* P [::-1], end = ' ')
    print (F + 1)