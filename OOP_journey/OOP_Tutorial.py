class Parent:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def introduce(self):
        print()
        print(f"Hi I am {self.first} {self.second}")

class Child(Parent):
    def __init__(self, first, second, year, section):
        super().__init__(first, second)
        self.year = year
        self.section = section

    def introduce(self):
        super().introduce()
        print(f"I came from section {self.section} and was born in {self.year}")

class Employee(Parent):
    def __init__(self, first, second, salary):
        super().__init__(first,second)
        self.salary = salary

    def introduce(self):
        super().introduce()
        print(f"My salary is {self.salary}")


parent_one = Parent("John", "Denver")
child_one = Child("Mary", "Grace", 2006, 3)
employee_one = Employee("Irish", "Anne", 50000)

parent_one.introduce()
child_one.introduce()
employee_one.introduce()

#=========================================================

class Student:
    def __init__(self, name, course, year, section):
        self.name = name
        self.course = course
        self.year = year
        self.section = section

    def introduce(self):
        print(f"Name   : {self.name}")
        print(f"Course : {self.course}")
        print(f"Year   : {self.year}")
        print(f"Section: {self.section}")

def user_cont():
    user_choice = input("DO you still want to add another student? (YES or NO): ").upper()
    if user_choice == "YES":
        return True
    elif user_choice == "NO":
        return False
    else:
        print("Enter only YES or NO!")

student_list = []

user_conti = True
while user_conti:
    student_name = input("Enter student name: ")
    student_course = input("Enter student course: ")
    student_year = int(input("Enter student year: "))
    student_section = input("Enter student section: ")

    student = Student(student_name, student_course, student_year, student_section)
    student_list.append(student)

    user_conti = user_cont()

for student in range(len(student_list)):
    print(f"Student number {student + 1} profile:")
    student_list[student].introduce()
    print()