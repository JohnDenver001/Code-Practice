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
