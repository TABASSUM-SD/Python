num=(int(input("enter the number")))
print("mul table of",num,":")
for i in range (1,num+1):
     print("--------------")
     for j in range(1,11):
      print(i,"x",j,"=",i*j)