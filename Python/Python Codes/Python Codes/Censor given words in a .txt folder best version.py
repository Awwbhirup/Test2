def corr(wor,st):
    c=''
    f=''
    col=[",", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", "\\", ";", ":", "'", "\"", "<", ">", "/", "?", "`", "~"]
    for i in wor:
        if i not in col:
            f=f+i
    if f in st:
        c=wor.replace(f,("*"*len(f)))
    else:
        c=wor
    return c           
w=input("Enter the words to be censored seperated with comma\
        ====>").strip().lower()
w=w.replace(" ","")
w=w.split(",")     
lo=[]
lf=[]
with open(r"H:\abc.txt","r") as a:
    lo=a.readlines()
for i in lo:
    y=i.strip('\n').strip().lower().split(" ")
    for j in y:
       y[y.index(j)]=corr(j,w)  
    st=" ".join(y)
    lf.append(st)   
with open(r"H:\abc.txt","w") as b:
    b.write("")
with open(r"H:\abc.txt","a") as c:
    for k in lf:
        c.write(k)
        c.write('\n')
