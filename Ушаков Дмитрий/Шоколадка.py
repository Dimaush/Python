m=int(input())
n=int(input())
k=int(input())
if k>m*n:
    print('NO')
elif k%m==0:
    print('YES')
elif k%n==0:
    print('YES')
else:
    print('NO')