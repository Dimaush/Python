def f (x):
    y = x - (x ** 2) * 0.01
    return y

def f1 (x):
    y1 = 1 - 0.02 * x
    return y1

x0 = int (input ())
e = float (input ())

delta = e + 1

#while abs (f (x0)) > e:
while abs (delta) > e:
    x1 = x0 - f (x0) / f1 (x0)
    delta = x1 - x0
    x0 = x1

print (x0)