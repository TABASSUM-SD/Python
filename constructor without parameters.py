class Student:
    def __init__(self):
        print("object is created")
        self.name="tabbu"
        self.age=19
std1=Student()
print("student name:",std1.name)
print("student age:",std1.age)
print("-------------------")
std2=Student()
print("student name:",std2.name)
print("student age:",std2.age)
