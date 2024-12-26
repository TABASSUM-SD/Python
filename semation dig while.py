num=int(input("enter a integer :"))
sum_Digits=0
while(num!=0):
    rem=num%10
    sum_Digits+=rem 
    num//=10
print("sum of digits:",sum_Digits)