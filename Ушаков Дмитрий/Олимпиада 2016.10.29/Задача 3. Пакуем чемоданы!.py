S = int (input ())
N = int (input ())
A = []
for i in range (N):
    A.append (int (input ()))
r = 0
c = 0
for i in range (len (A)):
    if r + A [i] <= S:
        r += A [i]
    else:
        c += A [i]
print (r)
print (c)