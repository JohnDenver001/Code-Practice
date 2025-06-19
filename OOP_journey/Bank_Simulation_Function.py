def validate_integer(word):
    while True:
        try:
            valid = int(input(word))
            return valid
        except ValueError:
            print("Enter number only!\n")

def user_cont():
    while True:
        cont = input("Would you like to continue?\n"
                     "(YES or NO): ").upper()
        print()
        if cont == "YES":
            return True
        elif cont == "NO":
            print("Thank You!")
            return False
        else:
            print("Please enter YES or NO only!")

def user_choice():
    print("=========================================")
    print("        WELCOME TO BANK SIMULATION")
    print("=========================================")
    print("[1] Register User")
    print("[2] Register User Bank Account")
    print("[3] Show User Info")
    print("[4] Show User Bank Status")
    print("[5] Deposit")
    print("[6] Withdraw")
    print("[7] Transfer")
    print("[8] Exit")
    print("=========================================")
    while True:
        choice = validate_integer("What would you like to do (1-9): ")

        if choice < 1 or choice > 8:
            print("Enter 1-9 only!\n")
        else:
            return choice