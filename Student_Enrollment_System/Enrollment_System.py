students = []
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
        user_conti = input("Do you want to continue? (YES or NO)\n"
                          "Enter choice: ").upper()
        if user_conti == "YES":
            return True
        elif user_conti == "NO":
            return False
        else:
            print("Enter YES or NO only!")
            print()

#gets the user choice
def user_choice():
    choices = validate_integer("======MAIN MENU=======\n"
          "[1] Add student\n" #Name, age, ID, course
          "[2] Enroll student in courses\n"
          "[3] Drop student in courses \n"
          "[4] View student's profile\n"
          "[5] View all students enrolled in a specific course\n"
          "[6] Remove a student completely\n"
            "Input choice: ")
    print()
    if choices > 6 or choices < 1:
        print("Enter number 1-6 only!")
        print()
    else:
        return choices

#add a new student
def add_student():
    name = input("Enter student's name: ").title()
    age = validate_integer("Enter student's age: ")
    identification = validate_integer("Enter student's ID: ")
    print()

    student_info = {
        "student_name": name,
        "student_age": age,
        "student_id": identification,
        "student_course": None
    }
    students.append(student_info)

def enroll_student():
    course = input("Enter course: ").upper()
    #Check if course is available
    if course not in available_courses:
        print(f"{course} is not available\n"
              f"Available courses are: {", ".join(available_courses)}")
        return

    find_id = validate_integer("Enter student's ID: ")
    #Check if student id exists
    for student in students:
        if find_id == student["student_id"]:
            id_name = student["student_name"]
            student.update({"student_course": course})
            break
    else:
        print(f"{find_id} can't be found!")
        return

    print(f"{id_name} is now enrolled to {course}")

def drop_student():
    drop_course = input("Enter a course: ").upper()
    #Check if course is available
    if drop_course not in available_courses:
        print(f"{drop_course} is not available\n"
              f"Available courses are: {", ".join(available_courses)}")
        return

    student_drop_name = input("Enter student you want to drop: ")
    #Check if the student exists
    for student in students:
        if student_drop_name.title() == student["student_name"]:
            students.remove(student)
            print(f"{student_drop_name} is now dropped in {drop_course}")
            break
    else:
        print(f"{student_drop_name} is not enrolled in {drop_course}!")
        return

def view_student_profile():
    view_student_name = input("Enter student name you want to view:") #Get student_name user wants to view
    for student in students:
        if view_student_name.title() == student["student_name"]:
            print(f"\n{view_student_name.title()} Profile: \n"
                  f"Student name: {student["student_name"]} \n"
                  f"Student age: {student["student_age"]} \n"
                  f"Student ID: {student["student_id"]} \n"
                  f"Student Course: {student["student_course"]}")

            break
    else:
        print(f"{view_student_name} can't be found! \n")



user_cont = True
while user_cont:
    choice = user_choice()

    if choice == 1:
        add_student()
    elif choice == 2:
        enroll_student()
    elif choice == 3:
        drop_student()
    elif choice == 4:
        view_student_profile()

    user_cont = user_continue()

print(students)
