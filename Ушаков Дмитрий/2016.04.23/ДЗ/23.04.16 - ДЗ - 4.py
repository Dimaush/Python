A = input (). split ()
for a in range (len (A)):
    A [a] = int(A [a])
b1 = A [0]
b2 = A [1]
for i in range (len (A)):
    if A[i] > b1:
        b2 = b1
        b1 = A [i]
m1 = A[0]
m2 = A[1]
for j in range (len (A)):
    if A[j] < m1:
        m2 = m1
        m1 = A [j]
if b1 * b2 > m1 * m2:
    print (b2, b1)
else:
    print (m1, m2)