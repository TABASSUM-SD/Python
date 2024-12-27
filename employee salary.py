empname=input("enter a name :")
designation=input("enter a designation :")
salary=int(input("enter a salary:"))
sep_allow=int(input("enter a special allowances :"))
bonus=int(input("enter a bonus :"))
gross_monthsal=salary+sep_allow
print("gross monthly salary :",gross_monthsal)
gross_annual=((gross_monthsal * 12) + bonus)
print("annual salary :",gross_annual)
if(gross_monthsal>500000):
    tax=((gross_monthsal*15/100))
    print('tax income',gross_monthsal-tax)
elif(gross_monthsal>400000):
    tax=((gross_monthsal*10)/100) 
    print("tax income",gross_monthsal-tax)
else:
    tax=((gross_monthsal*12)+bonus) 
    print("tax income",gross_monthsal-tax)      

