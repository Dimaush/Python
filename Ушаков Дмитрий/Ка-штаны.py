M,N = map(int,input().split())

s=list(map(int,input().split()))
k=1
for i in range(len(s)):
    for j in range(s[i]):
        print(k, end=' ')
        k+=1
        if k > M: k = 1
    print('')