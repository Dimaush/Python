M = list (map (int, input ().split ()))
n = int (input ())
l = len (M)
s = sum (M [0:n])
k = s
p = 0
for i in range (l):
    s -= M [i]
    s += M [(i + n) % l]
    if s < k:
        k = s
        p = i + 1
print (k, p)