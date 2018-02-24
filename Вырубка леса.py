def cutrees (i):
    global A, K, B, M
    n = i // K * (K - 1) * A + (i % K) * A + i // M * (M - 1) * B + (i % M) * B
    return n

A, K, B, M, X = map (int, input ().split())
a = 0
b = X
while b - a > 1:
    if cutrees ((a + b) // 2) < X: a = (a + b) // 2
    else: b = (a + b) // 2
if cutrees (a) == X: print (a)
else: print (b)