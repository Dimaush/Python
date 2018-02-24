n=int(input())
a=int(input())
b=int(input())
print (min (a + b - n + 1, min (a + 1, b + 1, n + 1)))