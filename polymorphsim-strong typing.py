# strong typing example
class duck:
    def walk(self):
        print("thapak thapak")
class horse:
    def walk(self):
        print("thbdak thbdak") 
class cat:
    def talk(self):
        print("meow mewo")          
def myfunction(obj):
    if hasattr(obj,'walk'):
     obj.walk()
    if hasattr(obj,'talk'):
         obj.talk() 
d=duck()
myfunction(d)
h=horse()
myfunction(h)    
c=cat()
myfunction(c)