x1 = int (input ())
y1 = int (input ())
x2 = int (input ())
y2 = int (input ())
if x2 > x1: h = 'E'
else: h = 'W'
if y2 > y1: v = 'N'
else: v = 'S'
print (h * abs (x2 - x1), end = '')
print (v * abs (y2 - y1))