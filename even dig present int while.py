num=int(input("enter a integer"))
EvenDigitCount=0
Rem=0
while(num!=0):
    Rem=num%10
    if(Rem%2==0):
      EvenDigitCount= EvenDigitCount+1
    num=num//10
print("Number of even digits:", EvenDigitCount)