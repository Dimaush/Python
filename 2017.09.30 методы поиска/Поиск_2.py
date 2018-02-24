def f (x):
    y = x - (x ** 2) * 0.01
    return y

a, b = map (int, input ().split ())
e = float (input ())

if f (a) == 0: print (a)
elif f (b) == 0: print (b)
else:
    flag = 0
    while b - a > e:
        c = (a + b) / 2
        if f (c) == 0:
            flag = 1
            break
        elif f (c) * f (a) > 0: a = c
        else: b = c

if flag == 0: print (a, b)
else: print (c)