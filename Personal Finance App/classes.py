import json
from helper_function import *

class User:
    def __init__(self, username, password, main_income, side_income, food_expense, rent_expense, clothing_expense, other_expense):
        self.username = username
        self.password = password
        self.main_income = main_income
        self.side_income = side_income
        self.food_expense = food_expense
        self.rent_expense = rent_expense
        self.clothing_expense = clothing_expense
        self.other_expense = other_expense

class System:
    def __init__(self):
        self.accounts = []

    def save_data_json(self):
        data = []
        for account in self.accounts:
            account_data = {
                "username": account.username,
                "password": account.password,
                "income": {
                    "main_income": account.main_income,
                    "side_income": account.side_income
                },
                "expense": {
                    "food_expense": account.food_expense,
                    "rent_expense": account.rent_expense,
                    "clothing_expense": account.clothing_expense,
                    "other_expense": account.other_expense
                }
            }
            data.append(account_data)

        with open("Finance_App_Data.json", "w") as file:
            json.dump(data, file, indent = 4)

    def reload_data_from_json(self):
        try:
            with open("Finance_App_Data.json", "r") as file:
                data = json.load(file)

            for account in data:
                account_credentials = User(username = account["username"],
                                           password = account["password"],
                                           main_income = account["income"]["main_income"],
                                           side_income = account["income"]["side_income"],
                                           food_expense = account["expense"]["food_expense"],
                                           rent_expense = account["expense"]["rent_expense"],
                                           clothing_expense = account["expense"]["clothing_expense"],
                                           other_expense = account["expense"]["other_expense"]
                                           )

                self.accounts.append(account_credentials)

        except FileNotFoundError:
            print("File not found! -- Starting Fresh!\n")

    def register(self):
        print("========================")
        print("        REGISTER")
        username = input("Enter username: ")
        password = input("Enter password: ")

        for account in self.accounts:
            if username == account.username:
                print("Account is already registered!\n")
                return

        if len(password) < 8:
            print("Password too weak!\n")
            return

        account_credentials = User(username, password, None, None, [], [], [], [])
        self.accounts.append(account_credentials)
        print("Account created successfully!\n"
              f"Welcome {username}")
        return username

    def login(self):
        print("========================")
        print("        LOGIN")
        username = input("Enter username: ")
        password = input("Enter password: ")

        for account in self.accounts:
            if username == account.username:
                current_account = account
                break
        else:
            print("Account is not registered!\n"
                  "Please register first!\n")
            return None, None, False

        if current_account.password != password:
            print("Password don't match!\n")
            return None, None, False

        print("Account login successfully!\n")
        return username, current_account, True

def add_main_income(log_on_account):
    main_income_amount = validate_integer("Enter your main income amount: ")
    log_on_account.main_income = main_income_amount
    print("Your main income has been updated successfully!\n")

def add_side_income(log_on_account):
    side_income_amount = validate_integer("Enter your side income amount: ")
    log_on_account.side_income = side_income_amount
    print("Your side income has been updated successfully!\n")

def add_food_expense(log_on_account):
    expense_info = get_expense_info()
    log_on_account.food_expense.append(expense_info)
    print("Your Expense has been updated\n")

def add_rent_expense(log_on_account):
    expense_info = get_expense_info()
    log_on_account.rent_expense.append(expense_info)
    print("Your Expense has been updated\n")

def add_clothing_expense(log_on_account):
    expense_info = get_expense_info()
    log_on_account.clothing_expense.append(expense_info)
    print("Your Expense has been updated\n")

def add_other_expense(log_on_account):
    expense_info = get_expense_info()
    log_on_account.other_expense.append(expense_info)
    print("Your Expense has been updated\n")