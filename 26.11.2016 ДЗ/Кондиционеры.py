#def proga ():
    #global n, m, A, M, s
    #for i in range (n):
        #k = 0
        #while M [k][0] < A [i]: k += 1
        #w = M [k][0]
        #c = M [k][1]
        #for j in range (m):
            #if M [j][0] >= A [i] and M [j][1] < c:
                #w = M [j][0]
                #c = M [j][1]
                #k = j
        #s += M [k][1]
    #return (s)

#n = int (input ())
#A = list (map (int, input ().split ()))
#m = int (input ())
#M = []
#for i in range (m):
    #M.append (list (map (int, input ().split ())))
#s = 0
#proga ()
#print (s)





n = int (input ())
a = list (map (int, input ().split ()))
m = int (input ())
c = []
for i in range (m):
    c.append (list (map (int, input ().split ())))
c.sort ()
k = c [-1][1]
for j in range (m):
    c[m - j - 1] += [[]]
k = min (k, c [m - j - 1][1])
c[m - j - 1][2] = k
s = 0
for l in range(n):
    p=-1
q=m-1
while q-p>1:
    d=(p+q)//2
    if c[d][0]>=a[l]: q=d
    else: p=d
    s+=c[q][2]
print(s)