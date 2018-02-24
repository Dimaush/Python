l=list(map(int,input().split()))
#l2=[]
#for j in range(len(l)):
    #max=l[0]
    
    #for i in l:
        #if i>max: max=i
    #l.remove(max)
    #l2+=[max]
l.sort()
print(' '.join(map(str,l)))