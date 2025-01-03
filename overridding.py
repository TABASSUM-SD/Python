class engineer:
    def work(self):
        print(" the engineer is working...... !")

class softwareengineer(engineer):
    def work(self):
        
        print("the software engineer is working....!")
class meachinalengineer(engineer):
    def work(self):
        print("meachinal engineer is workig.................!")        
e=engineer()
e.work()
s=softwareengineer()
s.work()
m=meachinalengineer()
m.work()