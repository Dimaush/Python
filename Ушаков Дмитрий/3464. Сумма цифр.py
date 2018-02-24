x=int(input())
a=x%10
b=(x%100-a)//10
c=(x-10*b-a)//100
m=a+b+c
print(m)