num=int(input("enter a num:"))
count=0
for i in range(1,num+1):
    if(num%i==0):
        count+=1
if(count==2):
    print("prime num")
else:
    print("not a prime num")            