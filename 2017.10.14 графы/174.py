N = int (input ())
R = []
x = 0
for i in range (N): x += sum (list (map (int, input ().split ())))
print (x // 2)