A = [0] * 10
a = int (input ())
while a > 0:
    a = int (input ())
    A[a - 1] += 1
for i in range (9):
    print(A[i + 1], end = ' ')