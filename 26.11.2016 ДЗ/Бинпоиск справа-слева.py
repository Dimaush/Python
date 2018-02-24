lenn, lenm = map (int, input ().split ())
N = list (map (int, input ().split ()))
M = list (map (int, input ().split ()))
for i in range (lenm):
    a = 0
    b = len (N) - 1
    while N [a] < M [i]: a += 1
    while N [b] > M [i]: b -= 1
    print (a, b)
    #a1 = max (A [a], K [i]) - min (A [a], K [i])
    #b1 = max (A [b], K [i]) - min (A [b], K [i])
    #if b1 < a1: print (A [b])
    #else: print (A [a])