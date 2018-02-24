A = input ().split ()
B = input ().split ()
for i in range (len (A)):
    A [i] = int(A [i])
for j in range (len (B)):
    B [j] = int(B [j])
C = []
for k in range (len (A)):
    s = B.count (A [k])
    if s > 0:
        C.append(A [k])
for x in range (len (C)):
    print(C [x], end = ' ')