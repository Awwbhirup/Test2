import random
s="----------█----------"
while(True):
    c=random.randint(1,3)
    if(c==1):
        l=random.randint(4,10)
        for i in range(0,l):
            print(s)
    elif(c==2):
        posmaxl=s.find("█")
        if posmaxl==0:
            continue
        nl=random.randint(1,posmaxl)
        for i in range(0,nl):
            s=s.replace("-█","█-")
            print(s)
    else:
        posmaxr=(len(s)-1)-(s.find("█"))
        if posmaxr==0:
            continue
        nr=random.randint(1,posmaxr)
        for i in range(0,nr):
            s=s.replace("█-","-█")
            print(s)