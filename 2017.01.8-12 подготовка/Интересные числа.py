a, b, k = map (int, input ().split ())
x = 0
for i in range (a, b + 1):
    #a = str (i).find ('0' * k)
    #b = str (i).find ('1' * k)
    #c = str (i).find ('2' * k)
    #d = str (i).find ('3' * k)
    #e = str (i).find ('4' * k)
    #f = str (i).find ('5' * k)
    #g = str (i).find ('6' * k)
    #h = str (i).find ('7' * k)
    #y = str (i).find ('8' * k)
    #z = str (i).find ('9' * k)
    n = str (i) [0]
    if a + b + c + d + e + f + g + h + y + z > -10: x += 1
print (x)