# single arguments
result=lambda num:print(num)
result(100)

#multi- arguments
result=lambda a,b:print(a*b)
result(25,7)

#muliple arguments
add=lambda x,y : (x+y, x-y)
a,s= add (5,2)
print(a)
print(s)