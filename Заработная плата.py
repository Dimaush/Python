A = int (input ())
B = int (input ())
C = int (input ())
N = int (input ())
x = 0
y = 0
z = 0
f = 0
while f == 0:
    y = (A + x - 2 * B) // 2
    z = (A + x - 2 * C) // 2
    if x + y + z > N:
        f = 1
    x += 1
if x > -1 and y > -1 and z > -1:
    print (x - 2, y, z)
else:
    print (0)