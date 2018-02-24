N = int (input ())
A = []
for i in range (N): A.append (list (map (int, input ().split ())))
p = input ()
S = list (map (int, input ().split ()))
x = 0
for i in range (N):
     for j in range (N):
          if A [i][j] == 1 and S [i] != S [j]: x += 1
print (x // 2)