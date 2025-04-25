def validate_number(function):
    while True:
        try:
            inputs = input(function)
            return float(inputs)
        except ValueError:
            print("Please Input numbers only!")

def get_user_operation():
    while True:
        choices = validate_number("============================ \n"
                    "What would you like to do? \n"
                    "============================ \n"
                    "1. Add a student and their grade \n"
                    "2. View all student and their grade \n"
                    "3. View student's specific grade \n"
                    "4. View student's GWA\n"
                    "5. Update a grade \n"
                    "6. Delete a student \n"
                    "7. Show class average \n"
                    "8. Exit \n"
                    "Input: ")
        if choices < 1 or choices > 8:
            print("Please enter number 1-8 only!")
        else:
            print()
            return choices

def user_continue():
    while True:
        print()
        cont = input("Do you still want to continue? ").upper()
        print()
        if cont == "YES":
            return True
        elif cont == "NO":
            print("Thank You!")
            return False
        else:
            print("Please Enter YES or NO only!")

def add_student_and_grade():
    name = input("What is the student's name? ")
    math_grade = validate_number("What is the student's grade in math subject? ")
    science_grade = validate_number("What is the student's grade in science subject? ")
    english_grade = validate_number("What is the student's grade in english subject? " )
    student_info = {
        "name": name,
        "math": math_grade,
        "science": science_grade,
        "english": english_grade
    }
    students.append(student_info)

def view_all_students_grade():
    for i in range(len(students)):
        print(f"Student {i + 1}'s info:")
        print(f"Name: {students[i].get('name')}")
        print(f"Math Grade: {students[i].get('math')}")
        print(f"Science Grade: {students[i].get('science')}")
        print(f"English Grade: {students[i].get('english')}")
        print()

def view_student_specific_grade():
    find_name = input("Please enter student's name you want to view: ").lower()
    find_subject = input("Please enter the subject you want to view: ").lower()

    found = False
    for student in students:
        if student["name"].lower() == find_name:
            if find_subject in student:
                print(f"{student['name']}'s grade in {find_subject} is: {student[find_subject]}")
                found = True
                break
    if not found:
        print("Student or subject is not found")

def student_gwa():
    found = False
    gwa_name = input("Which student's GWA you want to view? ")
    for student in students:
        if student["name"] == gwa_name:
            gwa = (student["math"] + student["science"] + student["english"]) / 3
            print(f"{student['name']} GWA is: {gwa}")
            found = True
            break
    if not found:
        print("Student not found")

def update_student_grade():
    name_update = input("Which student's grade you want to update? ")
    subject_update = input("Which subject you want to update? ")
    student_found = False

    while True:
        updated_grade = validate_number("Updated Grade: ")
        break

    for student in students:
        if student["name"].lower() == name_update.lower():
            student_found = True
            if subject_update in student:
                student[subject_update] = updated_grade
                subject_found = True
                print("Grade updated successfully!")
                break
            else:
                print("Subject not found!")

    if not student_found:
        print("Student not found!")

def delete_student():
    delete_name = input("Which student you want to delete? ")
    student_delete = None
    for student in students:
        if student["name"].lower() == delete_name.lower():
            student_delete = student
            print("Successfully Deleted!")
            students.remove(student_delete)
            break
    if student_delete is None:
        print("Student not found!")

def class_average():
    if len(students) == 0:
        print("There are no students found!")
        return

    total_gwa = 0
    for student in students:
        gwa = (student["math"] + student["science"] + student["english"]) / 3
        total_gwa += gwa

    average = total_gwa/len(students)
    print(f"The overall average of the class is: {average:.2f}")


students = []

user_continuation = True
while user_continuation:
    operation = get_user_operation()
    if operation == 1:
        add_student_and_grade()
    elif operation == 2:
        view_all_students_grade()
    elif operation == 3:
        view_student_specific_grade()
    elif operation == 4:
        student_gwa()
    elif operation == 5:
        update_student_grade()
    elif operation == 6:
        delete_student()
    elif operation == 7:
        class_average()
    elif operation == 8:
        print("Thank you for using my system!")
        break
    user_continuation = user_continue()
