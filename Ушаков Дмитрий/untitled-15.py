a=input()
A='!'+'"#$%&'+"'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
x = A.find(a)
if x in range (64,90):
    print(A[x-32])
elif x in range (32, 58):
    print(A[x+32])
else:
    print(a)