x1 = int (input ())
y1 = int (input ())
x2 = int (input ())
y2 = int (input ())
x = int (input ())
y = int (input ())
if x < x1 and y < y1:
    print ('SW')
if x < x1 and y > y1 and y < y2:
    print ('W')
if x < x1 and y > y2:
    print ('NW')
if x > x1 and x < x2 and y > y2:
    print ('N')
if x > x2 and y > y2:
    print ('NE')
if x > x2 and y > y1 and y < y2:
    print ('E')
if x > x2 and y < y1:
    print ('SE')
if x > x1 and x < x2 and y < y1:
    print ('S')