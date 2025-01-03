class student:
    @staticmethod
    def clgname():
        print("abc collage----!")
    @classmethod
    def writeexams(self):
        print("enjoy exams-----!") 
    #accessor method
    def show_name(self):
        return self.studentname
    def show_id(self):
        return self.id
    def show_email(self):
        return self.email
    #mutator method
    def set_name(self):
        self.studentname="scott"     
    def __init__(self,studentname,id,email):
        print("object is created--------!")
        self.studentname=studentname
        self.id=id
        self.email=email

student.clgname()
student.writeexams()
std1=student("tabbu",1,"tabbu@gmail.com")
print(std1.show_name())
print(std1.show_id())
print(std1.show_email())
 