"""class student:
    no_of_student=45
    def study(self):
        inquary=f"name of student:{self.name}.total percentage in class{self.classs}:{self.mark}"
        print(inquary)

vishnu=student()
rahul=student()
vishnu.name= "vishnu"
vishnu.classs=5
vishnu.mark= "65 percentage"
vishnu.study()
rahul=student()
rahul.name= "rahul"
rahul.classs=5
rahul.mark= "65 percentage"
rahul.study()"""
#print(rahul.no_of_student)
'''class student:
    def __init__(self,name,age,cla,mark):
        self.name=name
        self.age=age
        self.classs=cla
        self.mark=mark
        print(f"name of student:{self.name}.total percentage in class{self.classs}:{self.mark} and age is {self.age}")

student_name=student("vishnu",20,"btech",65)
student_name=student("rahul",20,"btech",65)'''
class public:
    def __init__(self,name,age,role,language):
        self.name=name
        self.age=age
        self.role=role
        self.language=language
        def detail(self):
            result=f"name of employ is {self.name}.\nage is {self.age}.\nrole is {self.role}\n and language is {self.language}."
            #return result
            print(result)
vishnu=public("vishnu",20,"software engineer",["c",'python',"javascript"])
#print(vishnu.detail())