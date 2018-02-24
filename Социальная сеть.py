n = int (input ())
N = []
for i in range (n):
    N.append (list (map (int, input ().split ())))
X = [0] * n
D = []
for i in range (n):
    D.append (X)
print (N)
print (D)
for k in range (len (N [0])):
    D [0][N [0][k] - 1] = 1
print (D)
for k in range (len (N [1])):
    D [1][N [1][k] - 1] = 1
print (D)
for k in range (len (N [2])):
    D [2][N [2][k] - 1] = 1
print (D)
for k in range (len (N [3])):
    D [3][N [3][k] - 1] = 1
print (D)
for k in range (len (N [4])):
    D [4][N [4][k] - 1] = 1
print (D)
#for i in range (n):
    #for k in range (len (N [i])):
        #D [i] [N [i] [k] - 1] = 1
        #print (D)