N = int (input ())
a0 = 1
a1 = 1
a2 = 0
for i in range (N):
    a0, a1, a2 = a0 + a1 + a2, a0, a1
print (a0)