def validate_integer(word):
    while True:
        try:
            valid = int(input(word))
            return valid
        except ValueError:
            print("Enter number only!\n")

def user_option():
    while True:
        user_choice = validate_integer("What would you like to do?\n"
              "[1] View Product Info\n"
              "[2] Add to Cart\n"
              "[3] View Cart \n"
              "[4] Remove from Cart\n"
              "[5] Checkout\n"
              "[6] Exit\n"
              "Enter Choice (1-6): ")

        if user_choice < 1 or user_choice > 6:
            print("Enter 1-6 only!")
            print()
        else:
            print()
            return user_choice

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
