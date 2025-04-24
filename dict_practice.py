def get_user_operation():
    is_user_input_valid = False
    while not is_user_input_valid:
        try:
            choices = int(input("============================ \n"
                        "What would you like to do? \n"
                        "============================ \n"
                        "1. Add a student and their grade \n"
                        "2. View all student and their grade \n"
                        "3. View student's specific grade \n"
                        "4. View student's GWA\n"
                        "5. Update a grade \n"
                        "6. Delete a student \n"
                        "7. Show class average \n"
                        "8. Show student average \n"
                        "9. Exit \n"
                        "Input: "))
            print()
            if choices < 1 or choices > 9:
                print("Please enter number 1-7 only!")
                print()
            else:
                is_user_input_valid = True
                return choices

        except ValueError:
            print("Please enter number only!")
            print()

def user_continue():
    is_user_continue = True
    while is_user_continue:
        cont = input("Do you still want to continue? ").upper()
        if cont == "YES":
            print()
            return True
        elif cont == "NO":
            print("Thank You!")
            return False
        else:
            print("Please Enter YES or NO only!")

def add_student_and_grade():
    name = input("What is the student's name? ")
    while True:
        try:
            math_grade = float(input("What is the student's grade in math subject? "))
            science_grade = float(input("What is the student's grade in science subject? "))
            english_grade = float(input("What is the student's grade in english subject? " ))
            student_info = {
                "name": name,
                "math": math_grade,
                "science": science_grade,
                "english": english_grade
            }
            students.append(student_info)
            break
        except ValueError:
            print("Please Enter Number Only!")
            print()

def view_all_students_grade():
    for i in range(len(students)):
        print(f"Student {i + 1}'s info:")
        print(f"Name: {students[i].get("name")}")
        print(f"Math Grade: {students[i].get("math")}")
        print(f"Science Grade: {students[i].get("science")}")
        print(f"English Grade: {students[i].get("english")}")
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
        print("Student or subject is nout found")

def student_gwa():
    found = False
    gwa_name = input("Which student's GWA you want to view? ")
    for student in students:
        if student["name"] == gwa_name:
            gwa = (student["math"] + student["science"] + student["english"]) / 3
            print(f"{student["name"]}'s GWA is: {gwa}")
            found = True
            break
    if not found:
        print("Student not found")

def update_student_grade():
    name_update = input("Which student's grade you want to update? ")
    subject_update = input("Which subject you want to update? ")
    is_input_valid = False
    student_found = False

    while not is_input_valid:
        try:
            updated_grade = float(input("Updated Grade: "))
            is_input_valid = True
        except ValueError:
            print("Please enter number only!")

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
    delete_name = input("Which student you want to delete? ").lower()
    for student in students:
        if student["name"].lower() == delete_name:
            print()


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
    user_continuation = user_continue()
