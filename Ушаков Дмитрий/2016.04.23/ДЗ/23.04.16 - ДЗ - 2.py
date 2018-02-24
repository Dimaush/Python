N = int (input ())
A = [0] * N
a = int (input ())

while a > 0:
    if a < N + 1:
        A[a - 1] += 1
    a = int (input ())

X = []
m = 0
for j in range (len (A)):
    if A[j] > m:
        m = A[j]
X = []
for k in range (len (A)):
    if m == A[k]:
        X.append (k + 1)

for g in range (len (X)):
    print (X[g], end = ' ')