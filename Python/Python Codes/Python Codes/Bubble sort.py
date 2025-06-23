l=[3,1,2,5,567,4,3,4,3,4,4,5,6,7,8,9,8,7,6,5,4,3,2,21]
for j in range(0,len(l)):
    for i in range(0,len(l)-j-1):
        if l[i]>l[i+1]:
            l[i] , l[i+1]=l[i+1],l[i]
            
            
print("THE SORTED LIST IS =",l)