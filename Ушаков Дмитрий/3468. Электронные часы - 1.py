n=int(input())%1440
y=n%60
x=(n-y)//60
print(x,y)