students = []

name = input("What is the student's name? ")
while True:
    try:
        math_grade = float(input("What is the student's grade in math subject? "))
        science_grade = float(input("What is the student's grade in science subject? "))
        english_grade = float(input("What is the student's grade in english subject?" ))
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

for student in students:
    print(student["name"])