def listik (i):
    if i < min (x, y): n = 0
    elif i == min (x, y): n = 1
    else: n = i // min (x, y) + (i - (min (x, y))) // max (x, y)
    return (n)

N, x, y = map (int, input ().split ())
a = 0
b = N * min (x, y)
while b - a > 1:
    if listik ((b + a) // 2) >= N: b = (b + a) // 2
    else: a = (b + a) // 2
if listik (a) >= N: print (a)
else: print (b)