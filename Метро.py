N = int (input ())
M = int (input ())
S = []
l = [0] * M
for i in range (M):
    l [i] = set (list (map (int, input ().split ())) [1:])
A, B = map (int, input ().split ())
lin = [0] * M
for i in range (M):
    lin [i] = [0] * M
for i in range (M - 1):
    for j in range(i + 1,M):
        if len (l [i] & l [j]) > 0:
            lin [i] [j] = 1
            lin [j] [i] = 1

m = 21
a = [21] * M
queue = []
b = set ()
for i in range (M):
    if A in l [i]:
        a [i] = 0
        queue += [i]
    if B in l [i]: b.add (i)
while queue != []:
    q = queue.pop(0)
    for i in range (M):
        if lin [q][i] > 0 and  a[i] > a [q] + 1:
            a [i] = a [q] + 1
            queue += [i]
for i in b:
    m = min (m, a [i])
if m == 21: print (-1)
else: print (m)

#a = []
#b = []
#for i in range (M):
    #if A in l [i]: a.append (i)
    #if B in l [i]: b.append (i)
#q = a
#flag = 0
#k = -1
#x = 0
#for i in range (M):
    #k += 1
    #for j in range (len (b)):
        #if q != []:
            #p = 0
            #while q [p] != b [j] and p < len (q) - 1: p += 1
        #else:
            #x = 1
            #break
        #if q [p] == b [j]: flag = 1
    #if flag == 1: break
    #for j in range (len (q)):
        #for z in range (M):
            #if lin [q [j]][z] == 1: q += [z]
        #q = q [1:]
#if x == 1: print (-1)
#else:
    #if k == M - 1:
        #for j in range (len (b)):
            #p = 0
            #while q [p] != b [j] and p < len (q) - 1: p += 1
            #if q [p] == b [j]: flag = 1
    #print (k)