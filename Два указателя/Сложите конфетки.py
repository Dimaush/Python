K = int (input ())
N = []
for i in range (K):
    a, n = map (int, input ().split ())
    N += [a] * n
while len (N) > 2:
    m = min (N [0], N [len (N) - 1])
    if N [0] == 0: N = N [1:len (N)]
    else: N [0] -= m

    N [len (N) - 1] -= m

    if N [-1] == 0: N = N [0:len (N) - 1]
    else:N [1] += m
    N [len (N) - 2] += m
print (len (N))
if len (N) == 2: print (N [0], N [1])
else: print (N [0])