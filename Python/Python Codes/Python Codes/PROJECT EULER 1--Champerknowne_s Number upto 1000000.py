#Champernowne's Constant
prod=1
cnt=0
num=1
valto=[1,10,100,1000,10000,100000,1000000]
while cnt<=1000000:
    nums=str(num)
    if ((cnt+len(nums))>=valto[0]):
        ind=valto[0]-cnt
        ind=ind-1
        prod=prod*int(nums[ind])
        valto=valto[1:]
    cnt=cnt+len(nums)
    num=num+1

print("THE PRODUCT OF THE DIGITS IN CHAMPERNOWNE'S CONSTANT IS = ",prod)