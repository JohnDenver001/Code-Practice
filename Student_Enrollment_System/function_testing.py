students = [
    {
        "student_name": "john",
        "student_age": 19,
        "student_id": 100,
    },
    {
        "student_name": "denver",
        "student_age": 20,
        "student_id": 101,
    },
    {
        "student_name": "cahutay",
        "student_age": 21,
        "student_id": 102,
    }
]

course = "BSIT"

find_id = int(input("Enter student's ID: "))
# Check if student id exists
for student in students:
    if find_id == student["student_id"]:
        print(student["student_name"])
        student["Course"] = "BSIT"
        break
else:
    print(f"{find_id} can't be found!")


print(students)