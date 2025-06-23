def validate_integer(word):
    while True:
        try:
            valid = int(input(word))
            return valid
        except ValueError:
            print("Enter number only!\n")

def get_choice(prompt, min_num, max_num):
    while True:
        user_choice = validate_integer(prompt)
        if user_choice is None:
            continue
        if min_num <= user_choice <= max_num:
            return user_choice
        print(f"Please enter number {min_num}-{max_num} only!")

def welcome_user():
    print("=====================================\n"
          "  WELCOME TO PERSONAL FINANCE APP\n"
          "=====================================")
    while True:
        welcome_choice = get_choice("[1] Register\n"
                                          "[2] Login\n"
                                          "Choice: ", 1, 3)

        return welcome_choice

def user_action_choice(username):
    if not username:
        return

    print("===========================\n"
          f"    WELCOME {username}\n"
          "==========================")
    while True:
        user_choice = get_choice("Please choose your action\n"
                                       "[1] Add Income\n"
                                       "[2] Add Expense Transaction\n"
                                       "[3] Logout\n"
                                       "Choice: ", 1, 3)

        print()
        return user_choice

def add_income():
    type_of_income = get_choice("===================================\n"
                                      "Please select the type of income\n"
                                      "[1] Work Income (Monthly)\n"
                                      "[2] Side Hustle Income\n"
                                      "Choice: ", 1, 2)

    return type_of_income

def add_expense():
    type_of_expense = get_choice("Please select the type of expense\n"
                                       "[1] Food Expense\n"
                                       "[2] Rent Expense\n"
                                       "[3] Clothing Expense\n"
                                       "[4] Other Expense\n"
                                       "Choice: ", 1, 4)
    return type_of_expense


def get_expense_info():
    print("Please enter the following expense infos")
    expense_date = input("Enter transaction date (e.g., Feb. 8, 2006: ")
    expense_amount = validate_integer("Enter the amount: ")

    expense_info = {
        "expense_date": expense_date,
        "expense_amount": expense_amount
    }
    return expense_info