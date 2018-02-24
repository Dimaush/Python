L = input ()
x = 0
P = [0] * len (L)
for i in range (len (P)): P [i] = [[0],[0]]
P [0][1] = 1
for i in range (1, len (P)):
    
#if L [0] != 'R': P [0] = 1
#for i in range (1, len (L)):
    #if x == 0:
        #if L [i] == 'R': P [i] = P [i - 1]
        #else:
            #P [i] = P [i - 1] + 1
            #x = 1
    #else:
        #if L [i] == 'L': P [i] = P [i - 1]
        #else:
            #P [i] = P [i - 1] + 1
            #x = 0
print (P)