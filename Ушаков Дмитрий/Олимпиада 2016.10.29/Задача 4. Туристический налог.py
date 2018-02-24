N = int (input ())
A = []
for i in range (N):
    A.append (int (input ()))
k = 2
x = 0
while x == 0 and k < len (A):
    k += 1
    for i in range (len (A) - k + 1):
        B = A [i:i + k]
        C = B [1:-1]
        for j in range (len (C)):
            if C [j] > B [0] and C [j] > B [-1]:
                x = 1
                i1 = i
if x == 0:
    print (0)
else:
    print (i1 + 1)
    print (i1 + k)