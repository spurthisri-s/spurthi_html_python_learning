class Person:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)


class Student(Person):

    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

    def show_marks(self):
        print("Marks:", self.marks)


student = Student("Spurthi", 95)

student.display()
student.show_marks()