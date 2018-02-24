n, k = map (int, input ().split ())
for i in range (k):
    if i != k - 1: print (i + 2, end = ' ')
    else: print (1, end = ' ')
for i in range (n - k):
    print (i % k + 1, end = ' ')