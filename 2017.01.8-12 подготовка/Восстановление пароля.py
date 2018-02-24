s = input ()
flag = 0
for i in range (len (s)):
    for j in range (len (s)):
        if i != j:
            if i < j: s1 = s [:i] + s [j] + s [i + 1:j] + s [i] + s [j + 1:]
            else: s1 = s [:j] + s [i] + s [j + 1:i] + s [j] + s [i + 1:]
            #print (i, j, s1)
            flag1 = 0
            k = 0
            for k in range (len (s1) // 2):
                if s1 [k] != s1 [len (s1) - k - 1]: flag1 = 1
            if flag1 == 0: flag = 1
if flag == 0: print ('No')
else: print ('Yes')