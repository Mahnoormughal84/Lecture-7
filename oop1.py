class Student:
    name : str = "Noor"
    student_id =1234
    age=18
    marks=10



    def pay(self):
        print("salary")

    def fee(self):
        print("payment")  

    def study(self):
            print("topics")


Student1 = Student()
Student2 = Student()
            
Student1.fee()

print(Student1.marks)
print(Student2.name)

Student2.fee()
Student1.study()
Student1.pay()
        