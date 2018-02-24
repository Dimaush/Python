r, c = map (int, input ().split ())
A = []
for i in range (r):
    l = input ()
    L = []
    for j in range (len (l)):
        if l [j] == 'S': y0, x0 = i, j
        elif l [j] == 'F': y1, x1 = i, j
        L.append (l [j])
    A.append (L)

print (y0, x0)
print (y1, x1)
for i in range (r): print (* A [i])

q = []
q.append ([y0, x0, 0])
ARR = [[0, 1], [-1, 0], [0, -1], [1, 0]]
while flag == 0:
    x = q.pop (0)
    y, x, a = x [0], x [1], x [2]
    b = (a + 1) % 4
    if A [y + ARR [a][0]][x + ARR [a][1]] != 'X': q.append ([y + ARR [a][0], x + ARR [a][1], a])
    if q [-1][0] == y1 and q [-1][1] == x1: flag = 1
    if A [y + ARR [b][0]][x + ARR [b][1]] != 'X': q.append ([y + ARR [b][0], x + ARR [b][1], b])
    if q [-1][0] == y1 and q [-1][1] == x1: flag = 1
