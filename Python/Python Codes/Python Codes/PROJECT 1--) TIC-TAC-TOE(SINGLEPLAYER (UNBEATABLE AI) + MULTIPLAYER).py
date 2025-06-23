'''
PROJECT 1: TIC-TAC-TOE (SINGLEPLAYER (UNBEATABLE AI) + MULTIPLAYER)
MADE ON 22/5/2023
AT 3.30 AM

'''

import random

def ai(lst,sym):
    osym="X" if sym=="O" else "O"
    pi=[1,2,3,4,5,6,7,8,9]
    n=""
    m=""
    po=False
    r1=lst[0]
    r2=lst[1]
    r3=lst[2]
    c1=[lst[0][0],lst[1][0],lst[2][0]]
    c2=[lst[0][1],lst[1][1],lst[2][1]]
    c3=[lst[0][2],lst[1][2],lst[2][2]]
    d1=[lst[0][0],lst[1][1],lst[2][2]]
    d2=[lst[0][2],lst[1][1],lst[2][0]]
    lstc=[r1,r2,r3,c1,c2,c3,d1,d2]
    for sy in [sym,osym]:
        for j in lstc:
            if(" " in j and j.count(sy)==2):
                po=True
                m=lstc.index(j)
                n=j.index(" ")
                break
        if(po):
            break
    if(lst[1][1]==" "and po==False):
        po=True
        m=1
        n=1
    if(po==False):
        lchk=[lst[0][0],lst[0][2],lst[2][0],lst[2][2]]
        lchks=[[0,0],[0,2],[2,0],[2,2]]
        if(" " in lchk):
            po=True
            yu=lchk.index(" ")
            yu=lchks[yu]
            m=yu[0]
            n=yu[1]
            
    if (po==False):
        lra=[]

        rt=[]
        for p in lst:
            for w in p:
                rt.append(w)
                
        rts=list(range(1,(len(rt)+1)))
        for j in range(0,len(rt)):
            
            if (rt[j]==" "):
                lra.append(rts[j])
                
        random.shuffle(lra)
        random.shuffle(lra)
        random.shuffle(lra)
        nom=lra[0]
        an=pi.index(nom)
        return an
            
    r1=[1,2,3]
    r2=[4,5,6]
    r3=[7,8,9]
    c1=[1,4,7]
    c2=[2,5,8]
    c3=[3,6,9]
    d1=[1,5,9]
    d2=[3,5,7]
    lstc=[r1,r2,r3,c1,c2,c3,d1,d2]
    fini=lstc[m][n]
    fini=pi.index(fini)
    return fini
                               
def box_printer(lst):
    '''
 __________________
|     |     |     |
|  1  |  2  |  3  |
|_____|_____|_____|
|     |     |     |
|  4  |  5  |  6  |
|_____|_____|_____|
|     |     |     |
|  7  |  8  |  9  |
|_____|_____|_____|

    '''
    s1="  |  ".join(lst[0])
    s1="|  "+s1+"  |"
    s2="  |  ".join(lst[1])
    s2="|  "+s2+"  |"
    s3="  |  ".join(lst[2])
    s3="|  "+s3+"  |"
    
    print(" _________________",end='\n')
    print("|     |     |     |",end='\n')
    print(s1,end='\n')
    print("|_____|_____|_____|",end='\n')
    print("|     |     |     |",end='\n')
    print(s2,end='\n')
    print("|_____|_____|_____|",end='\n')
    print("|     |     |     |",end='\n')
    print(s3,end='\n')
    print("|_____|_____|_____|",end='\n')
    print('\n')
   
def winner(mo,lst,p1,p1s,p2s,p2="AI"):
    ls=[p1s,p2s,p1,p2]
    r1=lst[0]
    r2=lst[1]
    r3=lst[2]
    c1=[lst[0][0],lst[1][0],lst[2][0]]
    c2=[lst[0][1],lst[1][1],lst[2][1]]
    c3=[lst[0][2],lst[1][2],lst[2][2]]
    d1=[lst[0][0],lst[1][1],lst[2][2]]
    d2=[lst[0][2],lst[1][1],lst[2][0]]
    lstc=[r1,r2,r3,c1,c2,c3,d1,d2]
    for i in ls[0:2]:
        for j in lstc:
            if(j.count(i)==3):
                print("THE WINNER IS {}".format(ls[ls.index(i)+2]),end='\n')
                print('\n')
                if(ls[ls.index(i)+2]=="AI"and mo=="s"):
                   print("BETTER LUCK NEXT TIME!",end='\n')
                else:
                    print("CONGRATULATIONS {} !!".format(ls[ls.index(i)+2]),end='\n')
                return 0
    if(" "not in r1 and " " not in r2 and " " not in r3):
        print("IT IS A DRAW",end='\n')
        if(p2=="AI" and mo=="s"):
            print("\n")
            print("BETTER LUCK NEXT TIME!",end='\n')    
        return 1
    else:
        return 2

def notvalid(pos,lst):
    if (pos>=1 and pos<=9):
        pa=[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
        pi=[1,2,3,4,5,6,7,8,9]
        k=pa[pi.index(pos)]
        if(lst[k[0]][k[1]]==" "):
               return False
        else:
            return True
    return True
    
def gameplay(mod,p1,s1,s2,p2="AI"):
    fl=[[" "," "," "],[" "," "," "],[" "," "," "]]
    pa=[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    pi=[1,2,3,4,5,6,7,8,9]
    if (mod=="m"):
        for z in range(1,10):
            if(z%2==1):
                print("{}'S TURN".format(p1),end='\n')
                print("")
                pl=-1
                while(notvalid(pl,fl)):
                    print("ENTER THE POSITION TO PLACE YOUR SYMBOL",end='\n')
                    pl=int(input("").strip())
                    if(notvalid(pl,fl)):
                        print("PLEASE ENTER A VALID POSITION",end='\n')
                pl=pa[pi.index(pl)]
                fl[pl[0]][pl[1]]=s1
                box_printer(fl)
                if(winner("m",fl,p1,s1,s2,p2)<2):
                    return 0
                print("")
                print("")
            else:
                print("{}'S TURN".format(p2),end='\n')
                print("")
                pl=-1
                while(notvalid(pl,fl)):
                    print("ENTER THE POSITION TO PLACE YOUR SYMBOL",end='\n')
                    pl=int(input("").strip())
                    if(notvalid(pl,fl)):
                        print("PLEASE ENTER A VALID POSITION",end='\n')
                pl=pi.index(pl)
                pl=pa[pl]
                fl[pl[0]][pl[1]]=s2
                box_printer(fl)
                if(winner("m",fl,p1,s1,s2,p2)<2):
                    
                    return 0
    elif(mod=="a"):
        for z in range(1,10):
            if(z%2==1):
                print("{}'S TURN".format(p1),end='\n')
                print("")
                pl=-1
                while(notvalid(pl,fl)):
                    print("ENTER THE POSITION TO PLACE YOUR SYMBOL",end='\n')
                    pl=int(input("").strip())
                    if(notvalid(pl,fl)):
                        print("PLEASE ENTER A VALID POSITION",end='\n')
                pl=pa[pi.index(pl)]
                fl[pl[0]][pl[1]]=s1
                box_printer(fl)
                if(winner("s",fl,p1,s1,s2,p2)<2):
                    return 0
                print("")
                print("")
            else:
                print("{}'S TURN".format(p2),end='\n')
                print("")
                pl=ai(fl,s2)
                pl=pa[pl]
                fl[pl[0]][pl[1]]=s2
                box_printer(fl)
                if(winner("s",fl,p1,s1,s2,p2)<2):
                    return 0
                       
def maingame():
    mode=""
    gamemodes=["m","a"]
    
    while(mode not in gamemodes):
        print("ENTER GAMEMODE, M FOR MULTIPLAYER ,A FOR AI MATCH",end='\n')
        mode=input("").strip().lower()
        if(mode not in gamemodes):
            print("PLEASE ENTER PROPER GAMEMODE",end='\n')
    print('\n')
            
    if(mode=="m"):
        p1=""
        p2=""
        s1=""
        s2=""
        while (len(p1)<=0):
            print("ENTER PLAYER 1'S NAME",end='\n')
            p1=input("").strip()
            if(len(p1)<=0):
                print("PLEASE ENTER PROPER NAME",end='\n')
        print('\n')
        while (len(p2)<=0):
            print("ENTER PLAYER 2'S NAME",end='\n')
            p2=input("").strip()
            if(len(p2)<=0):
                print("PLEASE ENTER PROPER NAME",end='\n')
        print('\n')
        while (len(s1)<=0):
             print("ENTER {}'S SYMBOL".format(p1),end='\n')
             s1=input("").strip().upper()
             if(len(s1)<=0):
                 print("PLEASE ENTER PROPER SYMBOL",end='\n')
        print('\n')
        s2="X" if (s1=="O") else "O"
        nl=gameplay(mode,p1,s1,s2,p2)
        return 0
    
    elif(mode=="a"):
        p1=""
        s1=""
        s2=""
        while (len(p1)<=0):
            print("ENTER PLAYER 1'S NAME",end='\n')
            p1=input("").strip()
            if(len(p1)<=0):
                print("PLEASE ENTER PROPER NAME",end='\n')
        print('\n')
        while (len(s1)<=0):
             print("ENTER {}'S SYMBOL".format(p1),end='\n')
             s1=input("").strip().upper()
             if(len(s1)<=0):
                 print("PLEASE ENTER PROPER SYMBOL",end='\n')
        print('\n')
        s2="X" if (s1=="O") else "O"
        nl=gameplay(mode,p1,s1,s2)
        nl=nl
        return 0
    else:
        print("SOME UNEXPECTED ERROR HAS OCCURED",end='\n')
            
print("============",end='\n') 
print("TIC-TAC-TOE",end='\n')
print("============",end='\n')
print("HOW TO PLAY--",end='\n')
print("===============",end='\n')
print(">>Choose your gamemode first, then player names and preffered symbols,",end='\n')
print(">>When it is your turn, select the preffered box's number to fill it with your symbols",end='\n')
print(">>To win, form a three character consequetive line of your symbol",end='\n')
print(">>THE AI MODE IS UNBEATABLE!!ONLY DRAW IS POSSIBLE!!",end='\n')
print('\n')

while True:
    a=maingame()
    print('\n')
    print('\n')
    pc=["y","n"]
    inp="bl"
    while inp not in pc:
        print("DO YOU WANT TO CONTINUE(YES=Y/NO=N)",end='\n')
        inp=input("").strip().lower()
        if(inp not in pc):
            print("PLEASE PROVIDE PROPER INPUT",end='\n')
    if(inp=="n"):
        print("")
        print("")
        print("THANKS FOR PLAYING TIC-TAC-TOE")
        print("~~ MADE BY ABHIRUP BANIK")
        break
            
    
