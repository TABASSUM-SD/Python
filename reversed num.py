num=int(input("enter a num:"))
rem=0
reverse=0
while(num!=0):
    rem=num%10
    reverse=reverse*10+rem
    num=num//10
print("reverse num",reverse)