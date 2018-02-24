def f (x):
    y = x - (x ** 2) * 0.01
    return y

x1, x2 = map (int, input ().split ())
e = float (input ())

y1, y2 = f (x1), f (x2)

a = y2 - y1
#b = x1 - x2
c = x1 * y2 - x2 * y1

while abs (f (x1)) > e:
    x1 = c / a
    y1 = f (x1)
    a = y2 - y1
    #b = x1 - x2
    c = x1 * y2 - x2 * y1

print (x1)