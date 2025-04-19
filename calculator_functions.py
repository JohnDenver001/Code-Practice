def add(*number):
    total = 0
    for num in number:
        total += num
    return total

def sub(*number):
    total = number[0]
    for num in number[1:]:
        total -= num
    return total

def mult(*number):
    total = 1
    for num in number:
        total *= num
    return total

def div(numOne, numTwo):
    return numOne / numTwo

def is_count_valid(operation_name):
    try:
        count = int(input(f"Enter How Many Numbers You Want to {operation_name}: " ))
        if count > 0:
            return count
        else:
            print("Numbers Must be Greater than 0.")
            print()
            return None
    except ValueError:
        print("Please Input Numbers Only")
        print()
        return None

def is_number_valid(prompt):
    number_valid = False
    while not number_valid:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Please Enter Numbers Only!")
            print()

def cont_calculating():
    check = True
    while check:
        con = input("Do You Still Want To Cotinue? ").upper()
        if con == "YES":
            return True
        elif con == "NO":
            print("Thank You!")
            return False
        else:
            print("Please Enter YES or NO only!")

def get_user_operation():
    is_operation_valid = False
    while not is_operation_valid:
        try:
            user = int(input("Input: "))
            if user <= 0 or user >= 5:
                print("Please Enter Number 1-4 Only!")
                print()
            else:
                is_operation_valid = True
                return user
        except ValueError:
            print("Please Input Number Only!")
            print()
