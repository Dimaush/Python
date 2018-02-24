A = ' '+'!'+'"#$%&'+"'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
B = input()
c = ''
for i in B:
    x = A.find(i)
    if x in range (16,26):
        c = c + A[x]
print(c)