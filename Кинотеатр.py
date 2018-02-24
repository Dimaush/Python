X, Y = map (int, input ().split ())
if X * 2 < Y or Y * 2 < X:
    print ('NO SOLUTION')
else:
    x = X
    y = Y
    if x > y:
        while x > y:
            print ('BGB', end = '')
            x -= 2
            y -= 1
        print ('GB' * x)
    else:
        while y > x:
            print ('GBG', end = '')
            x -= 1
            y -= 2
        print ('BG' * x)