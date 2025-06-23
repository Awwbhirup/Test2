l=[4,5,6,7,8,9,11,23,34,54,64,67,69,544]
rv=int(input("ENTER THE ELEMENT TO BE SEARCHED"))
a,n=0,(len(l)-1)   
while(a<=n):
    cv=(a+n)//2
    if(l[cv]==rv):
        print("THE REQUIRED ELEMENT {} WAS FOUND AT INDEX {} ".format(rv,cv))
        break
    elif(l[cv]<rv):
        a=cv+1
    elif(l[cv]>rv):
        n=cv-1
else:
    print("ELEMENT NOT FOUND")