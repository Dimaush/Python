N = int (input ())
n = str (N)
if len (n) == 2:
    if int (n [0]) < int (n [1]): print (0)
    elif min (int (n [0]), int (n [1])) == 0:
        print (1, end = '')
        print (max (int (n [0]), int (n [1])) - 1, end = '')
        print ('00')
    else:
        print (1, end = '')
        print (min (int (n [0]), int (n [1])) - 1, end = '')
        print (0, end = '')
        print (max (int (n [0]), int (n [1])))
elif len (n) == 3:
    x = int (n [0]) * 10 + int (n [1])
    if x > 18: print (0)
    elif n [2] == '0':
        print (1, end = '')
        print (x - 1, end = '')
        print ('00')
    else:
        print (1, end = '')
        print (int (n [2]) - 1, end = '')
        print (x - 9, end = '')
        print (9)
else:
    x = int (n [0]) * 10 + int (n [1])
    y = int (n [2]) * 10 + int (n [3])
    if x > 18 or y > 18: print (0)
    else:
        print (min (int (x), int (y)) - 9, end = '')
        print (9, end = '')
        print (max (int (x), int (y)) - 9, end = '')
        print (9)