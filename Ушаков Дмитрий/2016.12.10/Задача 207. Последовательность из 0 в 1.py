N = int (input ())
a0 = 1
a1 = 1
for i in range (N):
    a0, a1 = a0 + a1, a0
print (a0)