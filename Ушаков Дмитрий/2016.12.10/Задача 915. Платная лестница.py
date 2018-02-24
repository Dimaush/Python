N = int (input ())
A = list (map (int, input ().split ()))
if N == 1: print (A [0])
elif N == 2: print (A [1])
else:
    a0 = 0
    a1 = A [0]
    for i in range (N - 1):
        a0, a1 = a1, min (a0, a1) + A [i + 1]
    print (a1)