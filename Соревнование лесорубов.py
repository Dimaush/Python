n = int (input ())
N = [0] * n
for i in range (n): N [i] = [0]
for i in range (n):
    N [i] = [input ()]
    t, p = map (int, input ().split ())
    N [i].append (t)
    N [i].append (p)
for i in range (n):
    N [i][0], N [i][1], N [i][2] = N [i][1], N [i][2], N [i][0]
N.sort ()
x = N [-1][0]
k = 0
while N [k][0] < x: k += 1
print (N [k][2])