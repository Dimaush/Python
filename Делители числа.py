n = int (input ())
D = []
k = 2
while n > 1:
    if n % k == 0: 
        n = n // k
        D.append (k)
    else: k += 1
print (D)