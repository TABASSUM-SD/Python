class Employee:
    def __init__(self,empname,empage,empid,designation,salary,location,special_allo):
        print("object is created")
        self.empname=empname
        self.empage=empage
        self.empid=empid
        self.designation=designation
        self.salary=salary
        self.location=location
        self.special_allo=special_allo

emp1=Employee("Tabbu",19,101,"software",50000,"hyd","car")
print("emp name:",emp1.empname)
print("emp age:",emp1.empage)
print("emp id",emp1.empid)
print("designation:",emp1.designation)
print("salary:",emp1.salary)
print("special allowlance:",emp1.special_allo)
print("--------------------------------------------------")
emp2=Employee("Arshe",11,102,"collector",60000,"vij","bike")
print("emp name:",emp2.empname)
print("emp age:",emp2.empage)
print("emp id:",emp2.empid)
print("designation:",emp2.designation)
print("salary:",emp2.salary)
print("special allowlance:",emp2.special_allo)
print("----------------------------------------------------")
emp3=Employee("Akbari",18,103,"engneering",70000,"chennai","bike")
print("emp name:",emp3.empname)
print("emp age:",emp3.empage)
print("emp id:",emp3.empid)
print("designation:",emp3.designation)
print("salary:",emp3.salary)
print("special allowlance:",emp3.special_allo)

