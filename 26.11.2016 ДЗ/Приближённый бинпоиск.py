lena, lenk = map (int, input ().split ())
A = list (map (int, input ().split ()))
K = list (map (int, input ().split ()))
for i in range (len (K)):
    a = 0
    b = len (A) - 1
    while b - a > 1:
        m = (a + b) // 2
        if A [m] > K [i]: b = m
        else: a = m
    a1 = max (A [a], K [i]) - min (A [a], K [i])
    b1 = max (A [b], K [i]) - min (A [b], K [i])
    if b1 < a1: print (A [b])
    else: print (A [a])