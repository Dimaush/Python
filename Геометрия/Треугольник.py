d = int (input ())
x, y = map (int, input ().split ())
if d - x >= y and x >= 0 and y >= 0: print (0)
else:
    a = x ** 2 + y ** 2
    b = (x - d) ** 2 + y ** 2
    c = x ** 2 + (y - d) ** 2
    if a <= b and a <= c: print (1)
    elif b <= a and b <= c: print (2)
    else: print (3)