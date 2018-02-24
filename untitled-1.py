def coorx (mx):
    sx = 0
    for k in range (N):
        sx += max (mx - X [k], X [k] - mx)
    return (sx / N)

def coory (my):
    sy = 0
    for k in range (N):
        sy += max (my - Y [k], Y [k] - my)
    return (sy / N)

N = int (input ())
A = []
for i in range (N):
    A.append (list (map (int, input ().split ())))
X = []
Y = []
for i in range (len (A)):
    X.append (A [i][0])
for i in range (len (A)):
    Y.append (A [i][1])
x0 = sum (X) / N
y0 = sum (Y) / N

print (A)

for i in range (-1000, 1000):
    if coorx (x0) >= coorx (i):
        x0 = i
for j in range (-1000, 1000):
    if coory (y0) >= coory (j):
        y0 = j
print (x0, y0)
i = 0
while N [i][0] != x0 and N [i][1] != y0: i += 1