def validate_integer(word):
    while True:
        try:
            valid = int(input(word))
            return valid
        except ValueError:
            print("Enter number only!\n")

def limit_choice(choice, number_one, number_two):
    if choice < number_one or choice > number_two:
        print(f"Please enter {number_one}-{number_two} only!")
        return
    return choice

def user_logout():
    while True:
        log_out = input("Confirm logout (YES or NO): ").upper()

        if log_out == "YES":
            return False
        elif log_out == "NO":
            return True
        else:
            print("Enter 'YES' or 'NO' only!\n")

def welcome_user():
    print("=====================================\n"
          "  WELCOME TO PERSONAL FINANCE APP\n"
          "=====================================")
    while True:
        welcome_choice = validate_integer("[1] Register\n"
                                          "[2] Login\n"
                                          "Choice: ")

        return limit_choice(welcome_choice, 1, 3)

def user_action_choice(username):
    if not username:
        return

    print("===========================\n"
          f"    WELCOME {username}\n"
          "==========================")
    while True:
        user_choice = validate_integer("Please choose your action\n"
                                       "[1] Add Income\n"
                                       "[2] Add Expense Transaction\n"
                                       "[3] Logout\n"
                                       "Choice: ")

        print()
        return limit_choice(user_choice, 1, 3)

def add_income():
    type_of_income = validate_integer("===================================\n"
                                      "Please select the type of income\n"
                                      "[1] Work Income (Monthly)\n"
                                      "[2] Side Hustle Income\n"
                                      "Choice: ")

    return limit_choice(type_of_income, 1, 2)

def add_expense():
    type_of_expense = validate_integer("Please select the type of expense\n"
                                       "[1] Food Expense\n"
                                       "[2] Rent Expense\n"
                                       "[3] Clothing Expense\n"
                                       "[4] Other Expense\n"
                                       "Choice: ")
    return limit_choice(type_of_expense, 1, 4)


def get_expense_info():
    print("Please enter the following expense infos")
    expense_date = input("Enter transaction date (e.g., Feb. 8, 2006:")
    expense_amount = validate_integer("Enter the amount: ")

    expense_info = {
        "expense_date": expense_date,
        "expense_amount": expense_amount
    }
    return expense_info