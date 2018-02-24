def skolko (i):
    x = (i // w) * (i // h)
    return (x)
 
w, h, n = map (int, input ().split ())
a = 1
b = n * max (w, h)
while b - a > 1:
    m = (a + b) // 2
    if skolko (m) < n: a = m
    else: b = m
if skolko (a) >= n: print (a)
else: print (b)