def calc (N):
    A = [100] * N
    A [0] = 0
    for i in range (N):
        if i + 1 < N: A [i + 1] = min (A [i + 1], A [i] + 1)
        if (i + 1) * 2 - 1 < N: A [(i + 1) * 2 - 1] = min (A [(i + 1) * 2 - 1], A [i] + 1)
        if (i + 1) * 3 - 1 < N: A [(i + 1) * 3 - 1] = min (A [(i + 1) * 3 - 1], A [i] + 1)
    print (A [-1])
 
X = int (input ())
calc (X)