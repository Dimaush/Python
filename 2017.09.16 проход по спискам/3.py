M = list (map (int, input ().split ()))
n = int (input ())
l = len (M)
s = sum (M [0:n])
p = -1
for i in range (l):
    s -= M [i]
    s += M [(i + n) % l]
    if s == 0: p = i + 1
print (p)