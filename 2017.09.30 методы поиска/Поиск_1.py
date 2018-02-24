def f (x):
    y = x - (x ** 2) * 0.01
    return y

a, b = map (int, input ().split ())
e = float (input ())
m = abs (f (a))
flag = 0
x0 = a
while flag == 0 and x0 <= b:
    x0 += e
    n = abs (f (x0))
    if n < m:
        m = n
        s = x0
print (s)