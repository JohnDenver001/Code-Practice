import hashlib

def validate_integer(word):
    while True:
        try:
            validate = int(input(word))
            return validate
        except ValueError:
            print("Enter number only! \n")

def user_cont():
    while True:
        cont = input("Would you like to continue?\n"
                     "(YES or NO): ").upper()

        if cont == "YES":
            return True
        elif cont == "NO":
            print("THANK YOU!")
            return False
        else:
            print("Enter 'YES' or 'NO' only!")

def user_choice():
    print("=============================================\n"
                   "  WELCOME TO LOGIN AND REGISTRATION SYSTEM!\n"
                   "=============================================\n"
                   "Please enter the action you would like to take:\n"
                   "[1] Register\n"
                   "[2] Login\n"
                    "[3] Show User Credentials\n"
                    "[4] Change Password\n"
                    "[5] Delete Account\n"
                   "[5] Exit")
    while True:
        choice = validate_integer("Choice (1-3): ")

        if choice > 6 or choice < 1:
            print("Please enter number 1 - 3 only!")
        else:
            return choice

def check_password_len(word):
    while True:
        password = input(word)
        if len(password) < 8:
            print("Password too weak!\n")
        else:
            return password

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()