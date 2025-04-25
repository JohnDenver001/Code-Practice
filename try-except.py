students = [
    {
        "name": "john",
        "course": "BSIT",
        "age": 19
    },
    {
        "name": "denver",
        "course": "BSIS",
        "age": 20
    }
]

def validate_number(function):
    while True:
        try:
            input(function)

            return function
        except ValueError:
            print("Please Input numbers only!")

def get_user_operation():
    is_user_input_valid = False
    while not is_user_input_valid:
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
                    "8. Show student average \n"
                    "9. Exit \n"
                    "Input: ")
        print()

        if choices < 1 or choices > 9:
            print("Please enter number 1-7 only!")
            print()
        else:
            is_user_input_valid = True
            return choices

get_user_operation()