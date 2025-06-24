from datetime import datetime
import hashlib

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
                                        "[3] Show Dashboard\n"
                                        "[4] Recommend a Budget Plan\n"
                                       "[5] Logout\n"
                                       "Choice: ", 1, 5)

        print()
        return user_choice

def add_income():
    type_of_income = get_choice("===================================\n"
                                      "Please select the type of income\n"
                                      "[1] Work Income (Monthly)\n"
                                      "[2] Side Hustle Income (Weekly)\n"
                                      "Choice: ", 1, 2)

    return type_of_income

def add_expense():
    type_of_expense = get_choice("=================================\n"
                                        "Please select the type of expense\n"
                                       "[1] Food Expense\n"
                                       "[2] Rent Expense\n"
                                       "[3] Clothing Expense\n"
                                       "[4] Other Expense\n"
                                       "Choice: ", 1, 4)
    return type_of_expense

def get_expense_info():
    print("=========================================\n"
          "Please enter the following expense infos")
    while True:
        date_str = input("Enter transaction date (YYYY-MM-DD) ")
        try:
            expense_date = datetime.strptime(date_str, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid Date -- Use the format (YYYY-MM-DD)")

    expense_amount = validate_integer("Enter the amount: ")
    expense_info = {
        "expense_date": expense_date,
        "expense_amount": expense_amount
    }
    return expense_info

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

#STRPTIME = String -> Object datetime
#STRFTIME = Object datetime -> String

def date_strp_expense(data_list):
    return [{
            "expense_date": datetime.strptime(expense["expense_date"], "%Y-%m-%d"),
            "expense_amount": expense["expense_amount"]
            } for expense in data_list]

def date_strf_expense(account, expense_name):
    return [{
        "expense_date": expense["expense_date"].strftime("%Y-%m-%d"),
        "expense_amount": expense["expense_amount"]}
        for expense in getattr(account, expense_name)]

