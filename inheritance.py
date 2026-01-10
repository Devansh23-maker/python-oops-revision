
class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name:", self.name)


class Student(Person):   
    def __init__(self, name, roll_no):
        super().__init__(name)   
        self.roll_no = roll_no

    def show_details(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}")



s1 = Student("Devansh", 23)
s1.show_name()
s1.show_details()

Added inheritance example in Python

