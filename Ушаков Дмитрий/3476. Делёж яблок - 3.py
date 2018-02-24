n=int(input())
k=int(input())
x=n-k%n
if x==n:
    x=0
print(x)