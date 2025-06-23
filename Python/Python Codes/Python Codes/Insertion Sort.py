l=[2,4,56,56,34,23,2,7,8,9,4,5]
for i in range(1,len(l)):
    k=l[i]
    j=i-1
    while(j>=0 and k<l[j]):
        l[j+1]=l[j]
        j-=1
    else:
        l[j+1]=k
        

print("THE SORTED LIST IS = ",l)