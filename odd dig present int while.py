num=int(input("enter a integer"))
OddDigitCount=0
Rem=0
while(num!=0):
    Rem=num%10
    if(Rem%2!=0):
      OddDigitCount= OddDigitCount+1
    num=num//10
print("Number of odd digits:", OddDigitCount)