M = list (map (int, input ().split ()))
n = 0
l = len (M)
p = 0

#while p > -1:
    #p = -1
    #n += 1
    #s = sum (M [0:n])
    #for i in range (l):
        #s -= M [i]
        #s += M [(i + n) % l]
        #if s == 0:
            #p = i + 1
    #if p > -1: u = p

#print (n - 1, u)

x = 0
m = 0
p = -1
for i in range (l):
    if M [i] == 0: x += 1
    else:
        if x > m:
            m = x
            p = i - x
        x = 0
if m == 0: print (0)
else: print (m, p)