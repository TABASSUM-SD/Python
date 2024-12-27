studentname=input("enter a name:")
sub1=int(input("enter sub1 marks"))
sub2=int(input("enter sub2 marks"))
sub3=int(input("enter sub3 marks"))
total=0
average=0
print("student report:")
print("---------------------------")
print("student name",studentname)
print("sub1",sub1)
print("sub2",sub2)
print("sub3",sub3)
if(sub1>=35 and sub2>=35 and sub3>=35):
    total=sub1+sub2+sub3
    print("total",total)
    average=total/3
    print("average:",average)
    if(average>=90):
        print("congratulation you qualified in 1st class...!")
    elif(average>=75):
        print("congratulation you qualified in 2nd class...!")
    else:
        print("congratulation you qualified in 3rd class...!")
else:
   print("better luck next time")   

          
    

