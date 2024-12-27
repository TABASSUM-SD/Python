num=int(input("enter a num:"))
rem=0
reverse=0
temp=num
while(num!=0):
    rem=num%10
    reverse=reverse*10+rem
    num=num//10
if(temp==reverse):
    print(temp,"is a palindrome")
else:
    print(temp,"is not a palindrome")    
