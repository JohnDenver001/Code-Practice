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

find_id = 101
for student in students:
    if find_id == student["student_id"]:
        #Proceed
        print(student["student_id"])
        print(student["student_name"])
    else:
        #Print student cannot find
        print("WALA")