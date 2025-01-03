#duck example
class duck:
    def walk(self):
        print("thapak thapak")
class horse:
    def walk(self):
        print("thbdak thbdak")   
def myfunction(obj):
    obj.walk()
d=duck()
myfunction(d)
h=horse()
myfunction(h)    

print("*******************************************")

#another example
class father:
    def work(self):
        print("hardworking father")
class son:
    def work(self):
        print("graduate son")   
def result(self):
     self.work()
f=father()
result(f)
s=son()
result(s)  