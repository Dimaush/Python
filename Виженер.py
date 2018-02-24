text = list (input ().split ())
word = input ()
word = word.split ('_')
for i in range (len (word)):
    word [i] = int (word [i])
t = []
for i in range (len (text)):
    t.append (list (text [i].split ('_')))
x = []
for i in range (len (t)):
    x.append (len (t [i]))
t1 = []
for i in range (len (t)):
    for j in range (len (t [i])):
        t1.append (int (t [i][j]))
for i in range (len (t1)):
    t1 [i] += word [i % len (word)]
for i in range (len (x)):
    for j in range (x [i]):
        print (t1 [j], end = ' ')
    print ()
    t1 = t1 [x [i] + 1:]