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

#ask if user wants to continue
def user_continue():
    while True:
        user_conti = input("Do you want to continue? (YES or NO)\n"
                          "Enter choice: ").upper()

        if user_conti == "YES":
            print()
            return True
        elif user_conti == "NO":
            print()
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

    for student in students:
        if identification == student["student_id"]:
            print(f"{identification} already enrolled")
            break
    else:
        student_info = {
            "student_name": name,
            "student_age": age,
            "student_id": identification,
            "student_course": []
        }
        students.append(student_info)
        print(f"{name} Added!")

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
            student["student_course"].append(course)
            break
    else:
        print(f"{find_id} can't be found!")
        return

    print(f"{id_name} is now enrolled to {course}")

#drop specific student in a course
def drop_student():
    drop_course = input("Enter a course: ")
    #Check if course is available
    if drop_course.upper() not in available_courses:
        print(f"{drop_course} is not available\n"
              f"Available courses are: {", ".join(available_courses)}")
        return

    student_drop_name = input("Enter student you want to drop: ")
    #Check if the student exists

    for student in students:
        if drop_course.upper() in student["student_course"]:
            student["student_course"].remove(drop_course.upper())
            print(f"{student_drop_name} is now dropped in {drop_course.upper()}")
            break
    else:
        print(f"{student_drop_name} is not enrolled in {drop_course}!")
        return

def view_student_profile():
    view_student_name = input("Enter student name you want to view:") #Get student_name user wants to view
    for student in students:
        if view_student_name.title() == student["student_name"]:
            print(f"\n{view_student_name} Profile: \n"
                  f"Student name: {student["student_name"]} \n"
                  f"Student age: {student["student_age"]} \n"
                  f"Student ID: {student["student_id"]} \n"
                  f"Student Course: {', '.join(student['student_course'])}")

            break
    else:
        print(f"{view_student_name} can't be found! \n")

def view_students_in_course():
    view_course = input("Enter Course: ")
    if view_course.upper() not in available_courses:
        print(f"{view_course} is not available\n"
              f"Available Courses are: \n"
              f"{', '.join(available_courses)}")
        return

    student_in_course = []
    for student in students:
        for course in student["student_course"]:
            if view_course.upper() == course:
                student_in_course.append(student["student_name"])

    print(f"List of students enrolled in {view_course.upper()}:\n"
          f"{'\n'.join(student_in_course)}")


def remove_student():
    remove_id = validate_integer("Enter student ID: ")

    for student in students:
        if remove_id == student["student_id"]:
            remove_student_id = student
            students.remove(remove_student_id)
            print(f"{student["student_name"]} is now removed!")
            break

    else:
        print(f"{remove_id} can't be found!")
        return

def main():
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
        elif choice == 5:
            view_students_in_course()
        elif choice == 6:
            remove_student()
        user_cont = user_continue()

main()