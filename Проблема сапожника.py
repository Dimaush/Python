N, k = map (int, input ().split ())
K = list (map (int, input ().split ()))
K1 = K
L = []
while len (L) < len (K1):
    m = K [0]
    for i in range (len (K)):
        if K [i] <= m:
            m = K [i]
            x = i
    L.append (K [x])
    K = K [:x] + K [x + 1:]
S = 0
i = 0
while N >= S and i < len (L):
    S += L [i]
    if N >= S: i += 1
print (i)