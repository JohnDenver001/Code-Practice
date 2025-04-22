def get_user_operation():
    is_user_input_valid = False
    while not is_user_input_valid:
        try:
            choices = int(input("============================ \n"
                        "What would you like to do? \n"
                        "============================ \n"
                        "1. Add a student and their grade \n"
                        "2. View all student and their grade \n"
                        "3. Update a grade \n"
                        "4. Delete a student \n"
                        "5. Show class average \n"
                        "6. Show student average \n"
                        "7. Exit \n"
                        "Input: "))

        except ValueError:
            print("Please enter number only!")
            print()

        if choices < 1 or choices > 7:
            print("Please enter number 1-7 only!")
            print()
        else:
            is_user_input_valid = True
            return choices

def add_student_and_grade():
    name = input("What is the student's name? ")
    grade = float(input("What is the student's grade? "))

    student_info = {
        "name": name,
        "grade": grade
    }
    students.append(student_info)

def user_continue():
    try:
        cont = input("Do you still want to continue? ").upper()
        if cont == "YES":
            print()
            return True
        else:
            print("Thank You!")
            return False
    except ValueError:
        print("Please Enter YES or NO only!")

students = []

while True:
    if get_user_operation() == 1:
        add_student_and_grade()

for i in range(len(students)):
    print("Student " + str(int((i + 1))) + "'s name is: " + students[i].get("name"))
    print("Student " + str(int((i + 1))) + "'s grade is: " + str(students[i].get("grade")))
    print()