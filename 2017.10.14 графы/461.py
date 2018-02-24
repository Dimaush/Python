n = int (input ())
A = []
for i in range (n): A.append (list (map (int, input ().split ())))
flag = 1
for i in range (n):
     if A [i][i] == 1: flag = 0
if flag == 1: print ('NO')
else: print ('YES')