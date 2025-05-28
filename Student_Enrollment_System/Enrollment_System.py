students = []
courses = []
available_courses = ["BSIT", "BSIS", "BSCS", "BSCPE"]

#validate if integer as input is valid
def validate_integer(word):
    while True:
        try:
            number = int(input(word))
            return number
        except ValueError:
            print("Enter number only!")
            print()

#ask if user wants to cotinue
def user_continue():
    while True:
        user_cont = input("Do you want to continue? (YES or NO)\n"
                          "Enter choice: ").upper()
        if user_cont == "YES":
            return True
        elif user_cont == "NO":
            return False
        else:
            print("Enter YES or NO only!")
            print()

#gets the user choice
def user_choice():
    choice = validate_integer("======MAIN MENU=======\n"
          "[1] Add student\n" #Name, age, ID, course
          "[2] Enroll student in courses\n"
          "[3] Drop student in courses \n"
          "[4] View student's profile\n"
          "[5] View all students enrolled in a specific course\n"
          "[6] Remove a student completely\n"
            "Input choice: ")
    print()
    if choice > 6 or choice < 1:
        print("Enter number 1-6 only!")
        print()
    else:
        return choice

#add a new student
def add_student():
    name = input("Enter student's name: ")
    age = validate_integer("Enter student's age: ")
    identification = validate_integer("Enter student's ID: ")
    print()

    student_info = {
        "student_name": name,
        "student_age": age,
        "student_id": identification,
    }
    students.append(student_info)

def enroll_student():
    find_id = validate_integer("Enter student's ID: ")
    #Check if student id exists
    for student in students:
        if find_id == student["student_id"]:
            id_name = student["student_name"]
            break
    else:
        print(f"{find_id} can't be found!")
        return

    course = input("Enter course: ")
    #Check if course is available
    if course not in available_courses:
        print(f"{course} is not available\n"
              f"Available courses are: {", ".join(available_courses)}")
        return

    #Enroll student
    course_info = {
        "student_name": id_name,
        "student_id": find_id,
        "student_courses": course
    }

    courses.append(course_info)
    print(f"{id_name} is now enrolled to {course}")

def drop_student():
    drop_course = input("Enter a course: ")
    #Check if course is available
    if drop_course not in available_courses:
        print(f"{drop_course} is not available\n"
              f"Available courses are: {", ".join(available_courses)}")
        return

    student_drop_name = input("Enter student you want to drop: ")
    #Check if the student exists
    for student in courses:
        if student_drop_name == student["student_name"]:
            courses.remove(student)
            break
    else:
        print(f"{student_drop_name} can't be found!")
        return


user_cont = True
while user_cont:
    if user_choice() == 1:
        add_student()
    elif user_choice() == 2:
        enroll_student()
    elif user_choice() == 3:
        drop_student()
    user_cont = user_continue()

print(students)
print()
print(courses)