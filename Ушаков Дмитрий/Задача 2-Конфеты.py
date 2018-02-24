A = int(input())
B = int(input())
C = int(input())
x=A
y=B
z=C
while A>0 and B>0 and C>0:
    A=A-1
    B=B-1
    C=C-1
    if B>0:
        B=B-1
n=x+y+z-A-B-C
print(n)