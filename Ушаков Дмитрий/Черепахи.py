N = int(input())
A = [0] * N
t = 0
for i in range(1,N+1):
    x,y = input().split()
    x = int(x)
    y = int(y)
    if x + y + 1 == N and x>=0 and y>=0 and A[x] < 1:
            A[x] = 1
            t = t + 1
print(t)