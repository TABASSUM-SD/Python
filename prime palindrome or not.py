n=int(input("enter a num:"))
rem=0
reverse=0
num=n
while(n!=0):
    rem=n%10
    reverse=reverse*10+rem
    n//=10
if(reverse==num):
    for i in range(2,num):
            if(num%i==0):
             print(num,"is not prime but palindrome")
             break
    else:
       
        print(num,"a prime palindrome")   
else:
  print(num,"is not prime or palindrome")
        
        
     