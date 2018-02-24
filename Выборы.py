n = int(input())
A = list(map(int, input().split()))
a = ''
for i in range (len(A)):
    a = a + str(A[i])
print(a)
m = int(input())
for i in range(1,m + 1):
    X = list(map(int, input().split()))
    x = X[0]
    y = X[1]
    for s in range (len(a)):
        a[x - 1 : y - 1].find(a[s - 1])