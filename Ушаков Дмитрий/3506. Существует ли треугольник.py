a=int(input())
b=int(input())
c=int(input())
if a>=b+c:
 print('NO')
elif b>=a+c:
  print('NO')
elif c>=a+b:
   print('NO')
else:
    print('YES')