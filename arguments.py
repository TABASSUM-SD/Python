#positional arguments
def pw(x,y):
    z=x**y
    print(z)
pw(5,2) 

#keyword arguments
def show(name,age):
    print(name,age)
show(name="tabbu", age=19)   

#default argument
def hello(name,age=10):
    print(name,age)
hello(name="arshe",age=11)    


#variable length argument
def add(*num):
    z=num[0]+num[1]+num[2]
    print(z)
add(5,2,4)

#keyword variable length argument
def exp(**num):
    z=num['a']+num['b']+num['c']
    print(z)
exp(5,2,4,1,2,3)