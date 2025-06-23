s=input("Enter a string").strip().lower().split(" ")
for w in range(0,len(s)):
    c=True
    wo=list(s[w])
    for l in range(0,len(wo)):
        if not wo[l].isalpha():
            continue
        if c:
            wo[l]=wo[l].upper()
            c=False
        else:
            wo[l]=wo[l].lower()
            c=True
    s[w]="".join(wo)
str=" ".join(s)
print("THE FINAL STRING IS = ",str)
            
            
