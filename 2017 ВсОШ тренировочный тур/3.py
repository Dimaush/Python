N = int (input ())
k = int (input ())
A = 0
x = (k + 5) % 7
for i in range (N):
    if x == 5: A += 1
    x = (x + 2) % 7
print (A)