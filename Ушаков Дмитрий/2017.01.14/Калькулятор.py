N = int (input ())
A = [[100, []]] * N
print (A)
A [0] [0] = 0
print (A)
for i in range (N):
    if i + 1 < N:
        if A [i + 1][0] > A [i][0] + 1: A [i + 1][1] = A [i][1] + [1]
        A [i + 1][0] = min (A [i + 1][0], A [i][0] + 1)
    if (i + 1) * 2 - 1 < N:
        if A [(i + 1) * 2 - 1][0] > A [i][0] + 1: A [(i + 1) * 2 - 1][1] = A [i][1] + [2]
        A [(i + 1) * 2 - 1][0] = min (A [(i + 1) * 2 - 1][0], A [i][0] + 1)
    if (i + 1) * 3 - 1 < N:
        if A [(i + 1) * 3 - 1][0] > A [i][0] + 1: A [(i + 1) * 3 - 1][1] = A [i][1] + [3]
        A [(i + 1) * 3 - 1][0] = min (A [(i + 1) * 3 - 1][0], A [i][0] + 1)