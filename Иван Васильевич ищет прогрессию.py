a, b = map (int, input ().split ())
m = 0
for j in range (a, b):
    for i in range (j + 1, b + 1):
        x = i
        k = 1
        while x <= b and x % 1 == 0:
            x = x * (i / j)
            k += 1
        m = max (m, k)
print (m)