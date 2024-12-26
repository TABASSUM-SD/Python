num=int(input("enter a integer"))
DigitCount=0
while(num!=0):
    num=num//10
    DigitCount= DigitCount+1
print(DigitCount,'digit')