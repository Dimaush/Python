A = ' '+'!'+'"#$%&'+"'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
B = input()
c = ''
for i in B:
    x = A.find(i)
    if x in range (33,59):
        c = c + A[x+32]
    else:
        c = c + i
d=c[::-1]
if c == d:
    print('YES')
else:
    print('NO')