s = '0'
x = 0
print ('Сколько девяток?')
a = int (input ())
print ()
d = int ('1' * a)
a = d * 9
while int (s) < a:
    s = str (int (s) + 1)
    flag = 0
    for i in range (len (s)):
        m = int (s [i])
        if m == 0: flag = 1
        else:
            s1 = s [i + 1:]
            for j in range (len (s1)):
                n = int (s1 [j])
                if m == n: flag = 1
    if flag == 0:
        print (int (s))
        x += 1
print ()
print (x)