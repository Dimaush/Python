k = int (input ())
s = input ()
x = s.count ('1')
X = [s.find ('1')]
for i in range (x - 1):
    s1 = s [X [i] + 1:]
    X.append (s1.find ('1') + X [i] + 1)
for i in range (len (X) - 1):
    if i + k > len (X) - 1:
        #print ((len (s) - X [i] - 1) * 2, end = ' ')
        print (2 * (X [-1] - X [i]), end = ' ')
    else:
        #print ((X [i + k] - X [i]) * 2, end = ' ')
        print (2 * (X [i + k] - X [i]), end = ' ')
print (0)