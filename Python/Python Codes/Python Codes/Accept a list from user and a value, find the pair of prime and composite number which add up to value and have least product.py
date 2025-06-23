#accept a list from user and a value, find the pair of prime and composite 
#number which add up to value and have least product
def dup(lst):
    for i in range(0,len(lst)):
        f=lst[0]
        c=lst.count(f)
        for j in range(0,c):
            lst.remove(f)
        lst.append(f)
    lst.sort()
    return lst
def isprm(m):
    for i in range(2,(int(m**0.5)+1)):
        if m%i==0:
            return False
    return True
l=input("Enter a list of numbers seperated by comma\
        ==> ").strip().split(",")
l=dup(list(l))
li=[int(h) for h in l]
n=int(input("Enter the destination number==> ").strip())
prm=[x for x in li if (isprm(x)and(x>1))]
com=[y for y in li if ((not isprm(y))and(y>0))] 
prm.sort()
com.sort() 
data=[]   
for pv in prm:
    for cv in com:
        data.append([pv,cv,(pv+cv),(pv*cv)])
edata=[]
for j in data:
    if(j[2]==n):
        edata.append(j)
min=edata[0][3]
ind=-1
for g in edata:
    if g[3]<=min:
        min=g[3]
        ind=edata.index(g)
print("The prime digit {} and the composite digit {} add to form {} and have least product of {}".format(edata[ind][0],edata[ind][1],n,edata[ind][3]))
 

 
        
    


          
