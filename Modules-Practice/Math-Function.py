import math

def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please Enter Number Only!")
            print()

def user_continue():
    print("Do you still want to continue?")
    cont = input("YES or NO: ").upper()

    if cont == "YES":
        print()
        return True
    else:
        print("Thank You!")
        return False

def main_menu():
    user_cont = True
    while user_cont:
        x = get_number("Enter the first number: ")
        y = get_number("Enter the second number: ")

        print("===================================")
        print("             MAIN MENU             ")
        print("          MATH FUNCTION            ")
        print("[1] copysign (x, y) \n"
              "[2] fabs (x) \n"
              "[3] factorial (x) \n"
              "[4] fmod (x, y) \n"
              "[5] pow (x, y) \n"
              "[6] sqrt (x) \n"
              "[7] ceil (x) \n"
              "[8] floor () \n"
              "[9] exp (x)")
        print("====================================")
        user_input = get_number("Please Select an Operation (1-9): ")

        if user_input == 1:
            print("copysign(x,y)")
            print(f"Result: {math.copysign(x,y)}")
        elif user_input == 2:
            print("fabs(x)")
            print(f"Result: {math.fabs(x)}")
        elif user_input == 3:
            print("factorial(x)")
            print(f"Result: {math.factorial(x)}")
        elif user_input == 4:
            print("fmod(x,y)")
            print(f"Result: {math.fmod(x,y)}")
        elif user_input == 5:
            print("pow(x,y)")
            print(f"Result: {math.pow(x,y)}")
        elif user_input == 6:
            print("sqrt(x)")
            print(f"Result: {math.sqrt(x)}")
        elif user_input == 7:
            print("ceil(x)")
            print(f"Result: {math.ceil(x)}")
        elif user_input == 8:
            print("floor(x)")
            print(f"Result: {math.floor(x)}")
        elif user_input == 9:
            print("exp(x)")
            print(f"Result: {math.exp(x)}")

        print()
        user_cont = user_continue()
main_menu()