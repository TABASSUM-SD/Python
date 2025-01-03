class engineer:
    def __init__(self):
        print("hey...! iam the engineer class constructor....!")
e1=engineer()
print("-----------------------------------------------------------------")
class softwareengineer(engineer):
    def __init__(self):
        super().__init__()
        print("hey...! iam the software engineer class constructor....!")
s1=softwareengineer()
print("---------------------------------------------------------------")       
class civilengineer(engineer):
    def __init__(self):
        super().__init__()
        print("hey...! iam the civil engineer class constructor....!")
c1=civilengineer()
print("--------------------------------------------------------------------")
class mechanicalenginner(engineer):
    def __init__(self):
        super().__init__()
        print("hey....! iam mechanical engineer class constructor....!")
m1=mechanicalenginner()  
     