n = int (input ())
A = list (map (int, input ().split ()))
M = 0
for i in range (n):
    M += abs (A [i] - A [0])
q = 0
w = 0
a = 100
for i in range (-a, a):
    for j in range (-a, a):
        m = 0
        for p in range (n):
            m += abs (A [0] + i + j * p - A [p])
        if m < M:
            M = m
            q = i
            w = j
print (A [0] + q, w)