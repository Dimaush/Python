n = int (input ())
A = []
for i in range (n): A.append (list (map (int, input ().split ())))
flag = 1
x = 0
for i in range (n):
     if A [i][i] == 1: flag = 0
for i in range (n):
     for j in range (i + 1, n): x += A [i][j]
print (x)