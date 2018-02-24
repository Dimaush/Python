A = list (map (int, input ().split ()))
N = int (input ())
a = 0
b = len (A) - 1
while b - a > 1:
    if A [(b + a) // 2] >= N: a = (b + a) // 2
    else: b = (b + a) // 2
if A [a] < N: print (a + 1)
elif A [b] < N: print (b + 1)
else: print (-1)